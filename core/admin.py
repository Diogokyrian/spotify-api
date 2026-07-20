from django.contrib import admin
from .models import Singer, Album


# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "singer", "created_at", "updated_at")
    search_fields = ("title", "singer__name")
    readonly_fields = ("created_at", "updated_at")
