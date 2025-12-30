from django.db import models
import uuid


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    person_name = models.CharField(max_length=200)  # 通过name关联，不使用外键
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title