from imageboard.models import Image, Tag, ImageTag
from django.contrib import admin

class ImageTagInline(admin.StackedInline):
    model = ImageTag
    extra = 3

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['uploaded_date']}),
        (None,               {'fields': ['uploaded_by']}),
        (None,               {'fields': ['path_name']}),
        ('Optional', {'fields': ['description', 'author', 'translated_by'], 'classes': ['collapse']}),
        ('Dowload Links', {'fields': ['download_link1', 'download_link2', 'download_link3'], 'classes': ['collapse']}),
        (None,               {'fields': ['image']}),
    ]
    inlines = [ImageTagInline]
    list_display = ('name', 'description', 'author', 'translated_by', 'uploaded_date')
    list_filter = ['uploaded_date']

admin.site.register(Image, ImageAdmin)
admin.site.register(Tag)
admin.site.register(ImageTag)
