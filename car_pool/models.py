from django.db import models
from django.utils import timezone

class Car(models.Model):
    title = models.CharField(max_length=200)
    driver = models.ForeignKey('auth.User')
    origin = models.TextField()
    destination = models.TextField()
    available_seats = models.SmallIntegerField()
    departing_date = models.DateTimeField(
            default=timezone.now)
    arrival_date = models.DateTimeField(
            blank=True, null=True)

    def book_seat(self):
        self.available_seats = self.available_seats - 1
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
