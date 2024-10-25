from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Stock)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "symbol", "price", "lastupdate", "status")
    prepopulated_fields = {"slug": ("title",),}

admin.site.register(models.Category)