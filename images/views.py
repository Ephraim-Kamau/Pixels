from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.

def images_of_day(request):
    images = Image.objects.all()

    return render(request, 'today-images.html', {"images":images})


def search_results(request):

    if 'categories' in request.GET and request.GET["categories"]:
        search_term = request.GET.get("categories")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})        