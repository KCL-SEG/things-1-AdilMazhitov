from django.contrib import admin
from .models import Thing
# Register your models here.
@admin.register(Thing)
class UserAdmin(admin.ModelAdmin):
    list_display = [
                'name', 'description', 'quantity'
                  ]