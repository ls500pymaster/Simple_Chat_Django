from django.contrib import admin
from .models import Thread, Message

admin.site.site_header = "Simple Chat - Django Rest Framework"
admin.site.site_title = "Simple Chat"


@admin.register(Thread)
class AdminThread(admin.ModelAdmin):
	list_display = ["participants_names", "created", "updated"]
	search_fields = ["title",]

	"""
	:return: The participants_names() method concatenates the string representation of the participants in a thread,
	 and the short_description attribute sets the column title in the list view.
	"""
	def participants_names(self, obj):
		return ", ".join([str(participant) for participant in obj.participants.all()])
	participants_names.short_description = "Participants"


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
	list_display = ["sender", "thread", "created", "is_read"]
	search_fields = ["thread", "sender"]
	list_filter = ["sender",]