from django.db import models
from django.contrib.auth.models import User


class DoraUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=40)
    INTEREST_CHOICES = (
		('ai', 'Artificial Intelligence'),
        ('w3', 'Web 3.0'),
        ('dsg', 'Design'),
        ('iv', 'Investment'),
        ('si', 'Self-Improvement'),
        )
    interest = models.CharField(max_length=100, choices=INTEREST_CHOICES)


class Article(models.Model):
    ar_author = models.ForeignKey(DoraUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField()
    dora = models.DecimalField(decimal_places=10, max_digits=10)
    created_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    c_author = models.ForeignKey(DoraUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
    q_author = models.ForeignKey(DoraUser, on_delete=models.CASCADE, related_name='q_author')
    title = models.CharField(max_length=100)
    content = models.TextField()
    dora = models.DecimalField(decimal_places=10, max_digits=10)
    expert = models.ForeignKey(DoraUser, on_delete=models.CASCADE, null=True, related_name='expert')
    STATUS_CHOICES = (
        ('p', 'proceeding'),
        ('a', 'adopted'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now=True)

class Answer(models.Model):
    content = models.TextField()
    an_author = models.ForeignKey(DoraUser, on_delete=models.CASCADE)
    dora = models.DecimalField(decimal_places=10, max_digits=10)
    STATUS_CHOICES = (
        ('a', 'adopted'),
        ('r', 'rejected'),
        ('p', 'pending'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now=True)