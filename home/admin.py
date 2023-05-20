from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Contact
# from .models import Registration
# Register your models here.
# admin.site.register(Contact)

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Contact, ContactAdmin)


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(User, UserAdmin)