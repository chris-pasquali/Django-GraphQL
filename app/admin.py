from dataclasses import fields
from django.contrib import admin
from django.contrib import admin
from .models import Person, Address

class PersonAdmin(admin.ModelAdmin):
  fields = ('email', 'name', 'address')

class AddressAdmin(admin.ModelAdmin):
  fields = ('number', 'street', 'city', 'state')

admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)