import hashlib
from io import BytesIO
from django.db import models
from django.urls import reverse
from PIL import Image as PILImage
from django.core.files.base import ContentFile
import os
import logging
logger = logging.getLogger(__name__)


FORMAT_MAPPING = {
            'jpg': 'JPEG',
            'jpeg': 'JPEG',
            'png': 'PNG',
            'gif': 'GIF',
            }


class Image(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('image_detail', args=[str(self.id)])
    
    def _is_equal_img_hash(self, old_image_instance):
        if not hasattr(self, 'photo') or  not self.photo:
            return False

        new_data = self.photo.read()
        self.photo.seek(0)

        old_data = old_image_instance.photo.read()
        old_image_instance.photo.seek(0)

        return hashlib.sha256(new_data).hexdigest() == hashlib.sha256(old_data).hexdigest()
    
    def save(self, *args, **kwargs):
        
        # i add this logic to prevent reupload the same image when make a PUT request with the same img
        if self.pk:
            original = type(self).objects.get(pk=self.pk)
            if not self._is_equal_img_hash(original):
                original.thumbnail.delete(save=False)
                original.photo.delete(save=False)
            else:
                return

        super().save(*args, **kwargs)
        
        if self.photo:
            img = PILImage.open(self.photo.path)
            img.thumbnail((300, 300))

            thumbnail_name = os.path.basename(self.photo.name)
            thumbnail_extension = os.path.splitext(thumbnail_name)[-1][1:]
            stream = BytesIO()

            thumbnail_format = FORMAT_MAPPING.get(thumbnail_extension, 'JPEG')
            
            img.save(stream, format=thumbnail_format)

            stream.seek(0)

            thumbnail = ContentFile(stream.getvalue(), thumbnail_name)

            self.thumbnail.save(thumbnail_name, thumbnail, save=False)

            super().save(update_fields=['thumbnail'])

        
        # or you can use this verbose code to create the thumbnail, for me i prefer 1st one above :) 
        # if self.photo:
        #     img = PILImage.open(self.photo.path)
        #     img.thumbnail((300, 300))

        #     img_basename = os.path.basename(self.photo.name)

        #     thumb_dir = os.path.join('media', 'thumbnails')
        #     os.makedirs(thumb_dir, exist_ok=True)
            
        #     thumb_path = os.path.join(thumb_dir, img_basename)
        #     img.save(thumb_path)
        #     self.thumbnail = 'thumbnails/' + img_basename
        #     super().save(update_fields=['thumbnail'])