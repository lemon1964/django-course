from django.shortcuts import render
from django.views import View
from .forms import Gallery_Upload_Forms
from django.http import HttpResponseRedirect
from .models import Gallery
from django.views.generic.edit import CreateView
from django.views.generic import ListView


# Create your views here.
#
# def storage_file(file):
#     with open(f'gallery_tmp/{file.name}', 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)


# class GalleryViev(View):
#
#     def get(self, request):
#         form = Gallery_Upload_Forms()
#         return render(request, 'gallery/load_file.html', {'form': form})
#
#     def post(self, request):
#         form = Gallery_Upload_Forms(request.POST, request.FILES)
#         if form.is_valid():
#             # temp = request.FILES['image']  # можно и так оставить
#             temp = form.cleaned_data['image']
#             # storage_file(temp)
#             new_image = Gallery(image=temp)
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/load_file.html', {'form': form})

class GalleryViev(CreateView):
    model = Gallery
    fields = "__all__"
    template_name = 'gallery/load_file.html'
    success_url = '/load_image'


class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'


