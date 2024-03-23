from django.urls import path
from . import views

#URLConf
urlpatterns = [
  path("", views.get_foreclosure, name="get_foreclosure"),
  path("scrape/<str:location>", views.scrape, name="scrape")
]