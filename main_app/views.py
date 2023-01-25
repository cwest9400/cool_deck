from django.shortcuts import render
from django.views.generic.base import TemplateView
# from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response

 #adds artist class for mock database data
class Deck:
    def __init__(self,commander, image, play_style, primer):
        self.commander = commander
        self.image = image
        self.play_style = play_style
        self.primer = primer


decks = [
      Deck(
        "Vaevitis Asmadi",
        "https://cards.scryfall.io/art_crop/front/2/2/22ea73ec-1325-4437-a23f-dcda1767c713.jpg?1562858215",
        "Johnny",
        "This deck is built from premodern cards(1993-2003, pre-8th Edition). This deck makes the most of mana ramp and graveyard plays with big flashy creatures."),
      Deck(
        "Vaevitis Asmadi",
        "https://cards.scryfall.io/art_crop/front/2/2/22ea73ec-1325-4437-a23f-dcda1767c713.jpg?1562858215",
        "Johnny",
        "This deck is built from premodern cards(1993-2003, pre-8th Edition). This deck makes the most of mana ramp and graveyard plays with big flashy creatures."),
      Deck(
        "Vaevitis Asmadi",
        "https://cards.scryfall.io/art_crop/front/2/2/22ea73ec-1325-4437-a23f-dcda1767c713.jpg?1562858215",
        "Johnny",
        "This deck is built from premodern cards(1993-2003, pre-8th Edition). This deck makes the most of mana ramp and graveyard plays with big flashy creatures."),
]
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class DeckList(TemplateView):
    template_name = "deck_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["decks"] = decks # this is the context key to use in views
        return context