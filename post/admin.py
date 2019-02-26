from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(post)
admin.site.register(comment)
admin.site.register(supplier)
admin.site.register(plan)
admin.site.register(plan_group)
admin.site.register(plan_plan_group_manage)