from django.urls import path

from rentals import views


app_name = 'rentals'
urlpatterns = [
    path('', views.index, name='home_page'),
]