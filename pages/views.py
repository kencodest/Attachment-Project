from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choice import price_choices, category_choices, gate_choices

from listings.models import Listing
from sellers.models import Seller

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context ={
        'listings': listings,
        'price_choices': price_choices,
        'category_choices': category_choices,
        'gate_choices': gate_choices
        
    }
    return render(request, 'pages/index.html', context)

def about(request):
    sellers = Seller.objects.order_by('-start_date')
    
    som_seller = Seller.objects.all().filter(is_som=True)
    
    paginator = Paginator(sellers, 3)
    page = request.GET.get('page')
    paged_sellers = paginator.get_page(page)
    
    context = {
        'sellers': paged_sellers,
        'som_seller': som_seller
    }
    return render(request, 'pages/about.html', context)
