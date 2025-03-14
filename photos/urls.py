from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
    path('image/<int:pk>/delete/', views.delete_image, name='delete_image'),
    
    # API endpoints
    path('api/images/', views.ImageListAPI.as_view(), name='api_images_list'),
    path('api/images/<int:pk>/', views.ImageDetailAPI.as_view(), name='api_image_detail'),
]