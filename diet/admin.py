from django.contrib import admin
from diet.models import *


class DietAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at', 'openid', 'food', 'deleted')

admin.site.register(Diet, DietAdmin)
