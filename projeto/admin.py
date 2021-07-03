from django.contrib import admin
from .models import *
# Register your models here.

# models registered to show in admin panel
admin.site.register(Contact)
admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(Comment)
admin.site.register(Suggestions)
