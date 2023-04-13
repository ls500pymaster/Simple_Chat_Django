from django.contrib import admin

from accounts.models import CustomUser


@admin.register(CustomUser)
class AdminClient(admin.ModelAdmin):
	list_display = ("first_name", "last_name")
	list_filter = ("age", "gender")
	search_fields = ("email", "last_name")

