from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quest/<int:pk>/", views.quest, name="quest"),
    path("results/", views.result, name="results"),

]