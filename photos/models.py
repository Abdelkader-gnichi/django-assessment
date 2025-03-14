from io import BytesIO
from django.db import models
from django.urls import reverse
from PIL import Image as PILImage
from django.core.files.base import ContentFile
import os

class Image(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('image_detail', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        
        if self.pk:
            original = type(self).objects.get(pk=self.pk)
            if original.photo != self.photo:
                original.thumbnail.delete(save=False)
                original.photo.delete(save=False)

        super().save(*args, **kwargs)
        
        if self.photo:

            img = PILImage.open(self.photo.path)
            img.thumbnail((300, 300))

            thumbnail_name = os.path.basename(self.photo.name)
            thumbnail_extension = os.path.splitext(thumbnail_name)[-1][1:]
            stream = BytesIO()

            print("####", thumbnail_name, os.path.splitext(thumbnail_name)[-1][1:])
            
            img.save(stream, format=thumbnail_extension)

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