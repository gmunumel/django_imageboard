from imageboard.models import Image, Tag, ImageTag, File
from django.contrib import admin

class ImageTagInline(admin.StackedInline):
    model = ImageTag
    extra = 3

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        #(None,               {'fields': ['path_name']}),
        ('Optional', {'fields': ['uploaded_date', 'uploaded_by', 'description', 'author', 'translated_by']}),
        #('Dowload Links', {'fields': ['download_link1', 'download_link2', 'download_link3']}),
    ]
    inlines = [ImageTagInline]
    list_display = ('name', 'description', 'author', 'translated_by', 'uploaded_date')
    list_filter = ['uploaded_date']
    

admin.site.register(Image, ImageAdmin)
admin.site.register(Tag)
admin.site.register(ImageTag)
admin.site.register(File)
