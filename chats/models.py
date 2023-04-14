from django.db import models
from accounts.models import CustomUser
from django.core.exceptions import ValidationError


class Thread(models.Model):
    title = models.CharField(max_length=100)
    participants = models.ManyToManyField(CustomUser, related_name="threads")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Thread, self).save(*args, **kwargs)  # Save the instance to the database
        if self.participants.count() > 2:
            raise ValidationError("A thread can have a maximum of 2 participants")


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="messages")
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username}"
