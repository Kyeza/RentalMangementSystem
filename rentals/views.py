from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from rentals.models import Property
from users.models import LandLord


def index(request):
    properties = Property.objects.all()
    context = {
        'title': 'Properties for rent',
        'properties': properties
    }
    return render(request, 'rentals/index.html', context)


def owned_property(request, username):
    landlord = LandLord.objects.filter(user__username=username).first()
    user_property = landlord.property_set.all()

    context = {
        'user_property': user_property
    }
    return render(request, 'rentals/my_properties.html', context)


class PropertyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Property
    fields = ['name', 'image', 'description', 'address', 'price', 'category']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List a Property'
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user.landlord
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_landlord:
            return True
        return False


class PropertyDetailView(DetailView):
    model = Property


class PropertyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Property
    fields = ['name', 'image', 'description', 'address', 'price', 'category']

    def form_valid(self, form):
        form.instance.owner = self.request.user.landlord
        return super().form_valid(form)

    def test_func(self):
        user_property = self.get_object()
        if self.request.user == user_property.owner.user:
            return True
        return False


class PropertyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Property
    success_url = '/'

    def test_func(self):
        user_property = self.get_object()
        if self.request.user == user_property.owner.user:
            return True
        return False
