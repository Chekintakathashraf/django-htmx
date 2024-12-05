from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Posts)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LikedPost)
admin.site.register(LikedComment)
admin.site.register(LikedReply)