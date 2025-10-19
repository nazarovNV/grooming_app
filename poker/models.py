from django.db import models
import uuid


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_voting_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    VOTE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('☕', 'Кофе-брейк'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    final_score = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.title


class Vote(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='votes')
    voter_name = models.CharField(max_length=100)
    score = models.CharField(max_length=10)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['task', 'voter_name']

    def __str__(self):
        return f"{self.voter_name}: {self.score}"