from django.contrib import admin
from .models import Little
# Register your models here.


class LittleAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight','user')


admin.site.register(Little, LittleAdmin)
