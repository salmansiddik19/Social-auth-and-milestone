from django.db import models
from django.contrib.auth.models import User


class Milestone(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class MilestoneImage(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    image = models.FileField(blank=True)
