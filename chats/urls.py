from django.urls import path
from .views import CustomUserCreate, ThreadListCreate, MessageListCreate, UnreadMessagesCountView, ThreadListDelete, UserThreadList

urlpatterns = [
    path("register/", CustomUserCreate.as_view(), name="register"),
    path("threads/", ThreadListCreate.as_view(), name="threads"),
    path("messages/", MessageListCreate.as_view(), name="messages"),
    path("unread/", UnreadMessagesCountView.as_view(), name="unread"),

    path("threads/<int:pk>/delete/", ThreadListDelete.as_view(), name="thread_delete"),
    path("threads/<int:pk>/", UserThreadList.as_view(), name="user_threads")
]