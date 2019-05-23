from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, LandLord, Tenant


admin.site.register(User, UserAdmin)
admin.site.register(LandLord)
admin.site.register(Tenant)