from django.contrib import admin

from apps.users.models import User

admin.site.register(User)

admin.site.site_header = 'KUTARAMO'
admin.site.site_title = "KUTARAMO Admin Portal"
