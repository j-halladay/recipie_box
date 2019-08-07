from django.shortcuts import render
from recipie_box.models import Recipie, Author, RecipieForm
from recipie_box.forms import AddAuthor, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied


def index(request, *args, **kwargs):
    html = 'index.html'
    items = Recipie.objects.all()
    return render(request, html, {"recipies": items})


def recipie(request, id, *args, **kwargs):
    html = 'recipie.html'
    item = Recipie.objects.get(id=id)
    return render(request, html, {'recipie': item})


def author(request, id, *args, **kwargs):
    html = 'author.html'
    item = Author.objects.get(id=id)
    items = Recipie.objects.all().filter(author=item)
    return render(request, html, {'author': item, "recipies": items})


# def staff_required(login_url=None):
#     return user_passes_test(lambda u: u.is_staff, login_url=login_url)


@login_required
def addauthor(request, *args, **kwargs):
    html = 'genericform.html'
    if request.user:

        if not request.user.is_staff:
            raise PermissionDenied
    if request.method == "POST":
        form = AddAuthor(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['username'], password=data['password'],
                is_staff=data['is_staff'])
            a = Author.objects.create(
                user=u, name=data['name'], bio=data['bio'])
            login(request, u)
            return HttpResponseRedirect(reverse('index'))
    form = AddAuthor()

    return render(request, html, {'form': form})


@login_required
def addrecipie(request, *args, **kwargs):
    html = 'genericform.html'

    if request.method == "POST":

        form = RecipieForm(request.POST)
        if form.is_valid():

            new_recipie = form.save()

    form = RecipieForm()

    return render(request, html, {'form': form})


def loginpage(request, *args, **kwargs):
    html = 'genericform.html'

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(
                username=data['username'], password=data['password'])
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('login'))
            destination = request.GET.get('next')
            if destination is not None:
                return HttpResponseRedirect(destination)
            else:
                return HttpResponseRedirect(reverse('index'))
    form = LoginForm()

    return render(request, html, {'form': form})


def logoutpage(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
