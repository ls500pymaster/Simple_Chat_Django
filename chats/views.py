from rest_framework import generics, permissions, status, response
from rest_framework.response import Response

from accounts.models import CustomUser
from .models import Thread, Message
from .serializers import CustomUserSerializer
from .serializers import ThreadSerializer, MessageSerializer


class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomUserSerializer


class ThreadListCreate(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ThreadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ThreadListDelete(generics.DestroyAPIView):
    queryset = Thread.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ThreadSerializer

    def delete(self, request, *args, **kwargs):
        thread = self.get_object()
        if request.user in thread.participants.all():
            thread.delete()
            return Response({"detail": "Successfully deleted."},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "You are not authorized to delete this thread."},
                            status=status.HTTP_403_FORBIDDEN)


class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer


class UserThreadList(generics.ListAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        user_pk = self.kwargs["pk"]
        return Thread.objects.filter(participants__pk=user_pk)


class UnreadMessagesCountView(generics.GenericAPIView):
    queryset = Message.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        unread_messages_count = self.queryset.filter(thread__participants=request.user.id, is_read=False).count()
        return response.Response({"unread": unread_messages_count})