from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices


def index(request):

    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)[:3]
    # paginator = Paginator(listings, 3)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

# temporary for testing working
# return HttpResponse("<h1>Home Page</h1>")


def about(request):
    # List out all the Realtors
    realtors = Realtor.objects.all().order_by('-hire_date')[:3]

    # Top Realtor of the Month
    mvp_realtors = Realtor.objects.all().order_by(
        'name').filter(is_mvp=True)[:2]

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)


# def search(request):
#     listings = Listing.objects.all().order_by(
#         '-list_date').filter(is_published=True)
#     context = {
#         "listings": listings,
#         "state_choices": state_choices,
#         "bedroom_choices": bedroom_choices,
#         "price_choices": price_choices
#     }
#     return render(request, 'pages/search.html', context)
