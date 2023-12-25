from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User


class Note(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    content = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self) -> str:
        return self.user.username

class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField(upload_to="images/_songimage",default="images/_songimage/default_artist.png")
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title
    
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to="images/_profiles",default="images/_profiles/default_usr_icon.png")
    def __str__(self) -> str:
        return self.user.username