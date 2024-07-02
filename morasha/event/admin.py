from django.contrib import admin

from .models import Questions, Answers, EventUsers

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(EventUsers)