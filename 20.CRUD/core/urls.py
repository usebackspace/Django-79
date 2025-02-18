from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('marvel-delete/<int:id>',views.marvel_delete,name='marveldelete'),
    path('marvel-update/<int:id>',views.marvel_update,name='marvelupdate'),
]
