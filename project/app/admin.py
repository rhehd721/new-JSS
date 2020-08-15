from django.contrib import admin
from .models import Jasoseol, Comment


# admin에 model내용들 나오도록
admin.site.register(Jasoseol)
admin.site.register(Comment)