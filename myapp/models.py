from django.db import models

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)

class Song(models.Model):
    title = models.CharField(max_length=200)
    band_member = models.ForeignKey(BandMember, on_delete=models.CASCADE)
    duration = models.DurationField()

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140,default = "Zaid Bismillah, Software Engineer")
    date = models.DateTimeField()