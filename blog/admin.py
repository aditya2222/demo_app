from django.contrib import admin
from blog.models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','published_date')


admin.site.register(Post,PostAdmin)