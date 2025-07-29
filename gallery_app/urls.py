from django.urls import path
from gallery_app import views


urlpatterns = [
    path("", views.GalleryList.as_view(), name = "gallery-list"),
    path("image-detail/<int:pk>/", views.ImageDetail.as_view(), name="image-detail"),
    path("image-create/", views.ImageCreate.as_view(), name="image-create"),
    path("image-delete/<int:pk>", views.ImageDelete.as_view(), name="image-delete"),
]

