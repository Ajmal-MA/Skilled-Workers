from django.db import models
from django.contrib.auth.models import User
from workers.models import WorkerProfile
from django.utils import timezone 

class Booking(models.Model):
    STATUS_CHOICES = (
         ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('ongoing', 'Ongoing'),
        ('underprocess', 'UnderProcess'),
        ('completed', 'Completed'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    booking_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("accepted", "Accepted"),("ongoing","Ongoing"),("underprocess","Underprocess"),("completed","Completed")],
        default="pending"
    )
    customer_confirmed = models.BooleanField(default=False)
    worker_confirmed = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)

        


    def __str__(self):
        return f"{self.customer.username} → {self.worker.user.username} ({self.service_type})"


class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)  # one review per booking
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)  # 1 to 5 stars
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.customer.username}'s review for {self.worker.user.username}"

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    address = models.TextField()
    profile_photo = models.ImageField(upload_to='customer_photos/', blank=True, null=True) 

    def __str__(self):
        return self.full_name
