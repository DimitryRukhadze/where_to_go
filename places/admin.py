from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
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

        return format_html(f'<img src="{obj.img_file.url}" width="{width / 2}" height={height / 2} />')

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