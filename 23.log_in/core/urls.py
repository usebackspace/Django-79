from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.log_in,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
]
