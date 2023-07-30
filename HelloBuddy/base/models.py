from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    
    
    # The dunder __str__ method converts an object into its string representation which makes it more descriptive and 
    # readable when an instance of the profile is printed out. So, whenever we print out the profile of a user, it will display his/her username.



class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True) #topics have mulitple room but room have single topic
    name=models.CharField(max_length=200) 
    description=models.TextField(null=True,blank=True) #Means db cant have model here without this value havingsomehing in it os it cant be blank 
                                                       #Second para is for when submit form it cant be blank
    participants=models.ManyToManyField(User,related_name='participants',blank=True) 
    updated=models.DateTimeField(auto_now=True)     
    created=models.DateTimeField(auto_now_add=True) #Initial time stamp
    
    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)#specify parent name for relationship CASCADE=when parents delete simply dlt all the message in the room
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)     
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.body[0:50] #for preview data instead of full
