from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('decks/', views.DeckList.as_view(), name="deck_list"),
    path('decks/new/', views.DeckCreate.as_view(), name="deck_create"),
    path('decks/<int:pk>/', views.DeckDetail.as_view(), name="deck_detail"),
    path('decks/<int:pk>/update',views.DeckUpdate.as_view(), name="deck_update"),
    path('decks/<int:pk>/delete',views.DeckDelete.as_view(), name="deck_delete"),
]