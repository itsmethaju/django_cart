

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.


def home(request, c_slug=None):
        c_page = None
        prodt = None
        if c_slug!=None:
            c_page = get_object_or_404(category,slug=c_slug)
            prodt = product.objects.filter(categ=c_page, available=True)
        else:
            prodt = product.objects.all().filter(available=True)
        cat=category.objects.all()
        paginator=Paginator(prodt,1)
        try:
            page=int(request.GET.get('page','1'))
        except:
            page=1
        try:
            pro=paginator.page(page)
        except(EmptyPage,InvalidPage):
            pro=paginator.page(Paginator.num_pages)

        return render(request, 'index.html', {'pt':prodt,'ct':cat,'pg':pro})

def ProdCatDetail(request,c_slug,product_slug):
    try:
        prodt=product.objects.get(categ__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'podet.html',{'pr':prodt})
def search(request):
    prodt= None
    query= None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prodt=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'qr':query,'pr':prodt})

