from django.contrib import admin

from authentication.models import *

admin.site.register(Profile)
admin.site.register(Note)
admin.site.register(Song)