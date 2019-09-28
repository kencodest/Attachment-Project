from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choice import price_choices, category_choices, gate_choices


from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    
    queryset_list = Listing.objects.order_by('-list_date')
    
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    #Location
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            queryset_list = queryset_list.filter(location__iexact=location)
            
    #Gate
    if 'gate' in request.GET:
        gate = request.GET['gate']
        if gate:
            queryset_list = queryset_list.filter(gate__iexact=gate)
            
    #Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__iexact=category)
            
     #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    
    context = {
        'price_choices': price_choices,
        'category_choices': category_choices,
        'gate_choices': gate_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
    
