from django.contrib import admin
from .models import Image, Gallery, Room
from django.utils.html import mark_safe


class InlineImage(admin.TabularInline):
    model = Image


class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_image')
    list_display_links = ('title',)
    readonly_fields = ('get_image', )

    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="80" height="80">')

    get_image.short_description = 'Изображение'
    

admin.site.register(Room, RoomAdmin)
admin.site.register(Gallery)
admin.site.register(Image)


admin.site.site_title = 'Панель администратора'
admin.site.site_header = 'Панель администратора'
