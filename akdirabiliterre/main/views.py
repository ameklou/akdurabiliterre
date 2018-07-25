from django.shortcuts import render
from zoom.models import Zoom
from blog.models import Post
# Create your views here.

def index(request):
    zooms=Zoom.objects.filter(main=True)[:3]
    
    context={
        'posts':Post.objects.all()[:3],
        'zoom1':zooms[0]

    }
    return render(request, 'main/index.html',context)
