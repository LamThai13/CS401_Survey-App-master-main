from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homeRating/', views.homeRating, name='homeRating'),
    path('create/',views.create, name='create'),
    path('createRating/',views.createRatingQuestion, name='createRating'),
    path('vote/<entity_id>/',views.vote, name='vote'),
    path('rating/<rate_id>/',views.rating, name='rating'),
    path('result/<entity_id>/',views.result, name='result'),
    path('register/',views.register, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
]