from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase

class ImagesInLine(SortableTabularInline):
    model = Image
    readonly_fields = ['img_preview']
    ordering = ['queue_position']

    def img_preview(self, obj):
        height = obj.img_file.height
        width = obj.img_file.width
        while height > 200:
            height /= 2
            width /= 2

        img_html = format_html('<img src="{}" width="{}" height={} />', obj.img_file.url, width, height)

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