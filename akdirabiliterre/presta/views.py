from django.shortcuts import render
from . models import Ville,Prestataire,Category
# Create your views here.


def index(request):
    if request.method=='POST':
        pass
    else:
        context={
        'prestatires':Prestataire.objects.filter(validate=True)
        }
        return render(request,'presta/index.html',context)

def presta_detail(request,slug,category,ville):
    return render(request,'presta/presta_detail.html')
