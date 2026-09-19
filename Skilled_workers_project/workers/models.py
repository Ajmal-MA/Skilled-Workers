from django.db import models
from django.contrib.auth.models import User

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkerProfile(models.Model):
    WORKER_TYPES = [
        ("plumber", "Plumber"),
        ("painter", "Painter"),
        ("electrician", "Electrician"),
        ("fabricator", "Fabricator"),
        ("welder", "Welder"),
        ("carpenter", "Carpenter"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    worker_type = models.CharField(max_length=50, choices=WORKER_TYPES, default="plumber")
    profile_photo = models.ImageField(upload_to="worker_profiles/", blank=True, null=True)  # ✅ new

    def __str__(self):
        return f"{self.user.username} ({self.worker_type})"


    
class PreviousWork(models.Model):
    worker = models.ForeignKey(WorkerProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='work_image/',blank=True, null=True)
    completed_on = models.DateField()
    
    def __str__(self):
        return f"{self.title} - {self.worker.user.username}"
