from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listing, Bid, Comment
from .forms import CreateListingForm, CommentForm


def index(request):
    return render(request, "auctions/index.html", {
        'listings': Listing.objects.all()
    })

# Not working, need to handle incorrect form entries!
@login_required(login_url='/login')
def comment(request):
    form = CommentForm(request.POST)

    if form.is_valid():
        id = form.cleaned_data['id']
        commentText = form.cleaned_data['comment']

        if request.user.is_authenticated:
                user = request.user
        else:
            return render(request, "auctions/listing.html", {
                'message': ' Please login and try again'
            })

        item = Listing.objects.get(id=id)
        c = Comment(user=user, item=item, comment=commentText)
        c.save()

        return redirect('listing', id=id)

    else:
        return render(request, "auctions/listing.html", {
            'message': 'Something went wrong, please try again'
        })

@login_required(login_url='/login')
def create(request):
    if request.method == "POST":
        form = CreateListingForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']

            if request.user.is_authenticated:
                user = request.user
            else:
                return render(request, "auctions/create.html", {
                    'message': ' Please login and try again',
                    'form': form
                })

            i = Listing(user=user, title=title, description=description, price=price, image_url=image, category=category)
            i.save()

            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "auctions/create.html", {
                'message': "Please fill out name, description and price and try again",
                'form': form
            })
    else:
        form = CreateListingForm()
        return render(request, "auctions/create.html", {
            'form': form
        })

def listing(request, id):
    item = Listing.objects.get(id=id)
    comments = item.comments.all()

    return render(request, "auctions/listing.html", {
        'item': item,
        'comments': comments,
        'watchlist': False
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
