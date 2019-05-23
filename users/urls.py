from django.urls import path

from users.views import TenantSignUpView, LandlordSignUpView, ApplicationCreateView, ApplicationDetailView, \
    ApplicationListView
from users import views


app_name = 'users'
urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('signup/tenant/', TenantSignUpView.as_view(), name='tenant_signup'),
    path('signup/landlord/', LandlordSignUpView.as_view(), name='landlord_signup'),
    path('<username>/profile/', views.user_profile, name='user_profile'),
    path('application/new/', ApplicationCreateView.as_view(), name='application_create'),
    path('application/<int:pk>', ApplicationDetailView.as_view(), name='application_detail'),
    path('applications/', ApplicationListView.as_view(), name='application_list'),
]