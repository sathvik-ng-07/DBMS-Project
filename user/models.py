from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def def_img():
    return "https://static.wikia.nocookie.net/solo-leveling/images/8/8b/Jinwoo4.jpg/revision/latest?cb=20210803222649"


class profile(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE ,related_name = "fk")
    profile_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.uid}"
    def __list__(self) -> list:
        usr = User.objects.get(username = self.uname)
        return [usr]





class Courses(models.Model):
    Course_ID = models.CharField(primary_key = True, max_length=10)
    Course_name = models.CharField(max_length=50, unique=True,default="(*_*)")
    Date_added = models.DateTimeField(auto_now=True)
    No_of_enrolment = models.IntegerField(default=0)
    Course_description = models.CharField(max_length = 1200,null=True)
    Image_link = models.CharField(max_length=150,default=def_img)

    def __str__(self) -> str:
        return f"{self.Course_ID} :  {self.Course_name}"
    def __list__(self) -> list:
        return [self.Course_ID,self.Course_name,self.Date_added,self.No_of_enrolment,self.Course_description,self.Image_link]



class Topics(models.Model):
    Topic_ID = models.CharField(primary_key = True, max_length=10)
    Topic_name = models.CharField(max_length=50,default="(*-*)")
    Topic_description = models.CharField(max_length=1200,null=True)
    Last_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return f"{self.Topic_ID} :  {self.Topic_name}"
    def __list__(self) -> list:
        return [self.Topic_ID,self.Topic_name,self.Topic_description,self.Last_updated]










class CTtable(models.Model):
    Course_ID = models.ForeignKey('Courses', related_name = "ct_cid", on_delete = models.CASCADE)
    Topics_IDs = models.CharField(max_length=10000,null=True)
    # Related_topic_IDs = models.CharField(max_length=10000,null=True)
    # Course_rating = models.IntegerField(default=0)
    # Recommended_Time = models.IntegerField(default=0)
    Topic_Sources = models.CharField(max_length=1000,null=True)


    def __str__(self) -> str:
        return f"{self.Course_ID}"
    def __list__(self) -> list:
        return [self.Course_ID,self.Topics_IDs,self.Related_topic_IDs,self.Course_rating,self.Recommended_Time]






class Progress(models.Model):
    User_ID = models.ForeignKey("Profile", related_name = "prog_uid", on_delete = models.CASCADE)
    Course_ID = models.ForeignKey('Courses', related_name = "prog_cid", on_delete = models.CASCADE)
    Completed_topic_IDs = models.CharField(max_length=1000,null=True)
    Incompleted_topic_IDs = models.CharField(max_length=1000,null=True)
    Start_date = models.DateTimeField(auto_now=True)
    Last_update_date = models.DateTimeField(auto_now=True) # if Finish date is same as Start_date // display as unfinished


    def __str__(self) -> str:
        return f"{self.User_ID} :  {self.Course_ID}"
    def __list__(self) -> list:
        return [self.User_ID,self.Course_ID,self.Completed_topic_IDs,self.Incompleted_topic_IDs,self.Start_date,self.Finish_date]