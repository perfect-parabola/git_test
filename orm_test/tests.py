from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
import django
django.setup()
from orm_test.models import *
# Create your tests here.
from django.db.models import Q

a= pet.objects.filter(owner__name='류승준')
print(a)

b= person.objects.all().values('country').distinct().order_by('country')
print(b)

c = country.objects.filter(pk__in=person.objects.all().values('country').distinct().order_by('country'))
print(c)