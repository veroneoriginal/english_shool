from django.contrib import admin
from user_app.models import User, Role, Course

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Course)
