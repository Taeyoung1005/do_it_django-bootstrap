from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import *

admin.site.register(Post, MarkdownxModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

class TagAmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAmin)
admin.site.register(Comment)