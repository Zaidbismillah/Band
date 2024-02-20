from django.db import models

class BandMember(models.Model):
    """Model representing a band member.

    Attributes:
        name (str): The name of the band member.
        instrument (str): The instrument played by the band member.
    """
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)

class Song(models.Model):
    """Model representing a song.

    Attributes:
        title (str): The title of the song.
        band_member (BandMember): The band member associated with the song.
        duration (timedelta): The duration of the song.
    """
    title = models.CharField(max_length=200)
    band_member = models.ForeignKey(BandMember, on_delete=models.CASCADE)
    duration = models.DurationField()

class Post(models.Model):
    """Model representing a post.

    Attributes:
        title (str): The title of the post.
        body (str): The content of the post.
        signature (str): The signature of the post's author.
        date (datetime): The date and time when the post was created.
    """
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Zaid Bismillah, Software Engineer")
    date = models.DateTimeField()
