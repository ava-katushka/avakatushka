from django.contrib import admin

# Register your models here.

from blog.models import ImageBlock, Citate
from blog.models import Post, PostPreview, TextBlock, Tag


class TextBlockInline(admin.StackedInline):
    model = TextBlock
    extra = 3


class ImageBlockInline(admin.StackedInline):
    model = ImageBlock
    extra = 3


class PostPreviewInline(admin.StackedInline):
    model = PostPreview
    fields = ['title', 'catching_text', 'image', 'tags', 'slug', 'post']
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    inlines = [PostPreviewInline, TextBlockInline, ImageBlockInline]
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    pass


class CitateAdmin(admin.ModelAdmin):
    extra = 3


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Citate, CitateAdmin)
