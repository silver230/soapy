from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import *
from django.contrib import messages
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
# Create your views here.
def index (request):
    date = dt.date.today()
    photos = Post.get_all()     
    return  render (request,'soap.html',{"date": date,"photos":photos})

def testimony (request):
         
    return  render (request,'testimony.html')    

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def search(request):

    if 'post' in request.GET and request.GET["image"]:
        search_term = request.GET.get(" image")
        searched_images =  image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message," images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    


  
def profile(request):
    profile =Profile.get_all()
    photos = Post.get_all()
    # commented = CommentForm()
    return render(request, 'profile.html', {"profile": profile})

# @login_required(login_url='/accounts/login/')
def edit(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'edit.html' , {"form": form} )

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have editted your profile' ))
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form }
    return render(request, 'edit_profile.html',context)

# def search(request):

#     if 'post' in request.GET and request.GET["post"]:
#         search_term = request.GET.get("post")
#         searched_neighbor = Post.search_by_name(search_term)
#         # message=f'{search_term}'
#         return render(request, 'search.html',{"post": searched_post})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})
 
def create(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.post=current_user
            update.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'create.html' , {"form": form} )


class ProfileUpdate(UpdateView):
   model= Profile
   template_name = 'edit.html'
   fields = ['contact','bio','picture']

class ProfileDelete(DeleteView):
   model=Profile
   success_url = reverse_lazy('profile')



