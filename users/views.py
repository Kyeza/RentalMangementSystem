import logging

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from users.forms import TenantRegistrationForm, LandlordRegistrationForm
from users.models import User

log = logging.getLogger('custom')


def signup_page(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'tenant':
            return redirect('users:tenant_signup')
        elif user_type == 'landlord':
            return redirect('users:landlord_signup')
    else:
        return render(request, 'users/authentication/landing_page.html', {'title': 'Sign Up'})


class TenantSignUpView(CreateView):
    model = User
    form_class = TenantRegistrationForm
    template_name = 'users/authentication/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Sign Up'
        kwargs['user_type'] = 'Tenant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        log.info(f'Tenant {user.username} has successfully signed up')
        login(self.request, user)
        return redirect('login')


class LandlordSignUpView(CreateView):
    model = User
    form_class = LandlordRegistrationForm
    template_name = 'users/authentication/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Sign Up'
        kwargs['user_type'] = 'Landlord'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        log.info(f'Landlord {user.username} has successfully signed up')
        login(self.request, user)
        return redirect('login')


@login_required
def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    else:
        if request.method == 'POST':
            pass
        else:
            context = {
                'title': f'{user.username.capitalize()} Profile',
            }

        return render(request, 'users/authentication/profile.html', context)
