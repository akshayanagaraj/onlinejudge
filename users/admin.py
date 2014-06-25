from django.contrib import admin
from users.models import OjUser

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(OjUser,UserAdmin)

# Register your models here.
