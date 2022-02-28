from django.contrib import admin
from .models import Kid, Image
from django_object_actions import DjangoObjectActions


class ImageAdmin(admin.ModelAdmin, DjangoObjectActions):
    readonly_fields = ('image_tag','approved_by')
    fields = ['kid', 'image_url','image_tag', 'food_group', 'is_approved', 'approved_by']

    def image_tag(self, obj):
        return obj.image_tag()

    print(dir(image_tag))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Media:
        js = ('/static/js/admin.js',)

print(dir(admin))

admin.site.register(Image, ImageAdmin)
admin.site.register(Kid)
