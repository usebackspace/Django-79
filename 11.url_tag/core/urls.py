from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    # path('about/',views.about),
    path('about1234/<int:id>',views.about,name='about'),
    path('aboutshoes/<str>/<int:id>',views.aboutshoes,name='aboutshoes'),
]
