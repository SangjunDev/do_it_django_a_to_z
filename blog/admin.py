from django.contrib import admin
from .models import Post, Category, Tag, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}  
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}   
  
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Tag, TagAdmin)
 