from django.contrib import admin
from apps.newsletters.models import MessageNewsletter, GetEmail


admin.site.register(GetEmail)
admin.site.register(MessageNewsletter)
