from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username"]

@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name"]