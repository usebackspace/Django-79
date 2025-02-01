from django.urls import path
# from marvel import views
from . import views
urlpatterns = [
    path('spiderman/',views.spiderman),
    path('ironman/',views.ironman),
]
