import logging

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from users.forms import TenantRegistrationForm, LandlordRegistrationForm
from users.models import User, Application, Tenant, LandLord

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


class ApplicationCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Application

    def get_initial(self):
        initial_data = super().get_initial()
        tenant = Tenant.objects.filter(user=self.request.user)
        initial_data['applicant'] = tenant
        return initial_data

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Apply'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        application = form.save(commit=False)
        tenant = Tenant.objects.filter(user=self.request.user)
        application.applicant = tenant
        application.save()
        log.info(f'Tenat {self.request.user.username} has successfully applied for property {application.property}')
        return redirect('rentals:home_page')

    def test_func(self):
        if self.request.user.is_tenant:
            return True
        return False


class ApplicationDetailView(DetailView):
    model = Application


class ApplicationListView(ListView):
    model = Application
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_tenant:
            tenant = Tenant.objects.filter(user=self.request.user).first()
            applications = Application.objects.filter(applicant=tenant).order_by('-date_applied')
            return applications
        elif self.request.user.is_landlord:
            landlord = LandLord.objects.filter(user=self.request.user).first()
            applications = Application.objects.filter(applicant=landlord).order_by('-date_applied')
            return applications
