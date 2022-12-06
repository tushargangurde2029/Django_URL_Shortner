from django.shortcuts import render,redirect
import uuid
from .models import Url_Model
from django.http import HttpResponse

# Create your views here.
def index(request):     
    if request.method=="POST":
        url=request.POST.get("url")
        short_url = str(uuid.uuid4())[:5]
        save_url = Url_Model(url=url,short_url=short_url)
        save_url.save()
        print(short_url)
        context ={
            'url':short_url,
            'completeurl':url
        }
        return render(request,"shortner_app/index.html",context)
    return render(request,"shortner_app/index.html")

def short_link(request, link):
    get_url = Url_Model.objects.get(short_url=link)
    return redirect('https://'+get_url.url)

def get_link(request):
    get_url = Url_Model.objects.get(short_url=link)
    return HttpResponse()