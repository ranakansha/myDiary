from django.contrib import admin
from blogpost.models import Post,Blogcomment

# Register your models here.
admin.site.register((Post,Blogcomment))