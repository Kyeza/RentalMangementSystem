from django.urls import path

from users.views import TenantSignUpView, LandlordSignUpView
from users import views


app_name = 'users'
urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('signup/tenant/', TenantSignUpView.as_view(), name='tenant_signup'),
    path('signup/landlord/', LandlordSignUpView.as_view(), name='landlord_signup'),
    path('profile/', views.user_profile, name='user_profile')
]