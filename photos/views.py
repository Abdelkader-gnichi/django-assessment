# photos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Image
from .forms import ImageForm
from rest_framework import generics
from .serializers import ImageSerializer

# Web views
def home(request):
    images = Image.objects.all().order_by('-upload_date')
    return render(request, 'photos/home.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'photos/upload.html', {'form': form})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'photos/detail.html', {'image': image})

def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.photo.delete()
        if image.thumbnail:
            image.thumbnail.delete()
        image.delete()
        return redirect('home')
    return render(request, 'photos/confirm_delete.html', {'image': image})

# API views
class ImageListAPI(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer