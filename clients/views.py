from email import message
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from listings.views import listing
from .models import Client

from django.contrib import messages


def client(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Client.objects.all().filter(
                user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.info(
                    request, "You have already made an inquiry of this listing")
                return redirect('/listings/')

        client = Client(listing=listing, listing_id=listing_id, name=name,
                        email=email, phone=phone, message=message, user_id=user_id)
        client.save()
        send_mail(
            'Inquiry on property '+listing,
            'Dear Realtor, You have an inquiry for '+listing+' on the website.',
            'dharmendranagaraj8091@gmail.com',
            [realtor_email],
            fail_silently=False,)
        messages.success(
            request, "Your inquiry has been submitted, we will get back to you shortly.")

    return redirect('/listings/'+listing_id)
