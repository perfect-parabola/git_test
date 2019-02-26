from django.contrib import admin
from .models import *

# Register your models here.

class country_admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class person_admin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'country')
    search_fields = ('name', 'gender', 'age', 'country')

class relationship_admin(admin.ModelAdmin):
    list_display = ('person1', 'person2', 'type', 'created_at', 'updated_at')
    search_fields = ('person1', 'person2', 'type', 'created_at', 'updated_at')

class animal_admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class pet_admin(admin.ModelAdmin):
    list_display = ('name', 'animal', 'owner')
    search_fields = ('name', 'animal', 'owner')



admin.site.register(country, country_admin)
admin.site.register(person, person_admin)
admin.site.register(relationship, relationship_admin)
admin.site.register(animal, animal_admin)
admin.site.register(pet, pet_admin)

