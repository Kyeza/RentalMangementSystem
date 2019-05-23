from django.urls import path

from rentals import views
from rentals.views import PropertyCreateView, PropertyDetailView, PropertyUpdateView, PropertyDeleteView


app_name = 'rentals'
urlpatterns = [
    path('', views.index, name='home_page'),
    path('property/new/', PropertyCreateView.as_view(), name='create_property'),
    path('property/<int:pk>', PropertyDetailView.as_view(), name='property_detail'),
    path('property/<int:pk>/update', PropertyUpdateView.as_view(), name='property_update'),
    path('property/<int:pk>/delete', PropertyDeleteView.as_view(), name='property_delete'),
    path('<username>/property/', views.owned_property, name='owned_property'),
]