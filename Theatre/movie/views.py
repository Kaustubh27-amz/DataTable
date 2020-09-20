from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,
                                  ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Movies,Theatre
from django.contrib.auth.models import User

from django.urls import reverse_lazy

# Create your views here.

class about(TemplateView):
    template_name='movie/about.html'

class Movies_list(ListView):
    model=Movies

class Movies_create(LoginRequiredMixin,CreateView):
    model=Movies

class Movies_update(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='movie/movie_list.html'
    fields=('name','characters','tags','IMDb_rating','ticket_price','duration')
    model=Movies

class Movies_delete(LoginRequiredMixin,DeleteView):
    model=Movies
    success_url=reverse_lazy('movie_list')
