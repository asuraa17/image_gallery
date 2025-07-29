from django.shortcuts import render, redirect
from gallery_app.models import Image
from gallery_app.forms import ImageForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from django.urls import reverse


# Create your views here.
class GalleryList(ListView):
    model = Image
    template_name = "gallery_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        posts = Image.objects.all() #- means latest
        return posts
    
class ImageDetail(DetailView):
    model = Image
    template_name = "image_detail.html"
    context_object_name = "image"

    def get_queryset(self):
        queryset = Image.objects.filter(pk=self.kwargs["pk"])
        return queryset
    

class ImageCreate(LoginRequiredMixin, CreateView):
    model = Image
    template_name = "gallery_create.html"
    form_class = ImageForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("gallery-list")


class ImageDelete(LoginRequiredMixin, DeleteView):
    def get(self, request, pk):
        post = Image.objects.get(pk=pk)
        post.delete()
        return redirect("gallery-list")
        