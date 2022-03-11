from django.db.models import query
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404

from .models import Listing
from listings.choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'listings':  page_obj
    }
    return render(request, 'listings/listings.html', context)

    # contact_list = Contact.objects.all()
    # paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'list.html', {'page_obj': page_obj})


def listing(request, listing_id):
    listing_id_data = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing_id_data
    }
    return render(request, 'listings/listing.html', context)


def search(request):

    query_listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_listings = query_listings.filter(
                description__icontains=keywords)

    # iexact - exact but ignore case
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_listings = query_listings.filter(city__iexact=city)

    if 'state' in request.GET:
        if request.GET['state'] != 'State (All)':
            state = request.GET['state']
            if state:
                query_listings = query_listings.filter(state=state)

    if 'bedrooms' in request.GET:
        if request.GET['bedrooms'] != 'Bedrooms (Any)':
            bedrooms = request.GET['bedrooms']
            if bedrooms:
                query_listings = query_listings.filter(bedrooms=bedrooms)

    # __lte - less than or equal to the price
    if 'price' in request.GET:
        if request.GET['price'] != 'Max Price (All)':
            price = request.GET['price']
            if price:
                query_listings = query_listings.filter(price__lte=price)

    context = {
        'listings': query_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
