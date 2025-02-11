from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('formpost/',views.form_post),
    path('success/',views.success)
]
