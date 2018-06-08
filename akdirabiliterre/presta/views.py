from django.shortcuts import render , get_object_or_404
from . models import Ville,Prestataire,Category
from .forms import SearchForm
# Create your views here.


def index(request):
    if request.method=='POST':
        pass
    else:
        context={
        'prestatires':Prestataire.objects.filter(validate=True),
        'form':SearchForm()
        }
        return render(request,'presta/index.html',context)

def presta_detail(request,slug,category,city):
    category=Category.objects.get(slug=category)
    city=Ville.objects.get(slug=city)
    presta = get_object_or_404(Prestataire, slug=slug,
                                   validate=True,
                                   category=category,
                                   city=city
                                  )
    context={
    'presta':presta,
    'form':SearchForm()
    }
    return render(request,'presta/presta_detail.html',context)
