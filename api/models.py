from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=255)
    image=models.ImageField(upload_to='music/images/',null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='music/')  # Requires media setup

    def __str__(self):
        return self.title
