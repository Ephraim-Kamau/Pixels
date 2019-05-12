from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render (request, 'welcome.html')

def images_of_day(request):
    date = dt.date.today()
    images = Image.objects.all()

    return render(request, 'all-images/today-images.html', {"date": date, "images":images})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day    

 # View Function to present images from past days
def past_days_images(request,past_date):
   
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404() 
        assert False   

    if date == dt.date.today():
        return redirect(images_of_day)
  
    return render (request, 'all-images/past-images.html', {"date": date})

def search_results(request):

    if 'categories' in request.GET and request.GET["categories"]:
        search_term = request.GET.get("categories")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})    

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})        