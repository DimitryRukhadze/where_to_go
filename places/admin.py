from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import (
    SortableTabularInline,
    SortableAdminBase
)


class ImagesInLine(SortableTabularInline):
    model = Image
    readonly_fields = ['img_preview']
    ordering = ['queue_position']

    def img_preview(self, obj):
        img_html = format_html(
            '<img src="{}" style="max-height: 200px" />',
            obj.img_file.url,
        )

        return mark_safe(img_html)

    fields = ('queue_position', 'img_file', 'img_preview')


@admin.register(Place)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = [
        'title',
        'description_short'
    ]
    inlines = [
        ImagesInLine
    ]


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['img_file', 'place']
