from django.contrib import admin
from .models.user import user_login,user,education_detail,graduation
from .models.admin import admin_login,admindata

admin.site.register(user_login)
admin.site.register(user)
admin.site.register(education_detail)
admin.site.register(graduation)
admin.site.register(admin_login)
admin.site.register(admindata)
# Register your models here.
