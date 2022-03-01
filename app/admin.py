from django.contrib import admin
from .models import Kid, Image


class ImageAdmin(admin.ModelAdmin):
    fields = [
        'kid', 'image_url','image_tag', 'food_group', 
        'is_approved', 'approved_by']

    readonly_fields = ['image_tag',]


    def image_tag(self, obj):
        return obj.image_tag()
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Media:
        js = ('/static/js/admin.js',)


admin.site.register(Image, ImageAdmin)
admin.site.register(Kid)
