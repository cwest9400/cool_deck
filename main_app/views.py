from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.urls import reverse
# import models
from .models import Decks


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class DeckList(TemplateView):
    template_name = "deck_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #####Database connected
        context["decks"] = Decks.objects.all()
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["decks"] = Decks.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        
        else:
            context["decks"] = Decks.objects.all()
            context["header"] = "Cool decks"

        return context

class DeckCreate(CreateView):
    model = Decks
    fields = ['name', 'img', 'bio']
    template_name = "deck_create.html"
    def get_success_url(self):
        return reverse('deck_detail', kwargs={'pk': self.object.pk})
    # success_url = "/decks/"

class DeckDetail(DetailView):
    model = Decks
    template_name = "deck_detail.html"

class DeckUpdate(UpdateView):
    model = Decks
    fields = ['name', 'img', 'bio']
    template_name = "deck_update.html"
    success_url = "/decks/"
    # def get_success_url(self):
    #     return reverse('deck_detail', kwargs={'pk': self.object.pk})

class DeckDelete(DeleteView):
    model = Decks
    template_name = "deck_delete_confirmation.html"
    success_url = "/decks/"