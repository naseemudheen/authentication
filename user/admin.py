from django.contrib import admin
from user.models import MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MyUserAdmin(UserAdmin):
	list_display = ('pk', 'email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('pk', 'email','username',)
	readonly_fields=('pk', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(MyUser,MyUserAdmin)
