from re import L
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel



# Create your models here.
class Activity(TimeStampedModel): 

    SEMI_A = "1학기"
    SEMI_B = "2학기"


    SEMI_CHOICES = (
      (SEMI_A, "22년도 1학기"),
      (SEMI_B, "22년도 2학기"),
    )
    
    title = models.CharField(max_length=100, default = '', null=True, blank=False, verbose_name='제목')
    semester = models.CharField(choices=SEMI_CHOICES, default = '', max_length=10, blank=False, null=True, verbose_name='학기')
    thumnail_img = models.ImageField(default = '', verbose_name='썸네일이미지')
    
    img_a = models.ImageField(verbose_name='이미지1', null=True, blank=True)
    img_b = models.ImageField(verbose_name='이미지2', null=True, blank=True)
    img_c = models.ImageField(verbose_name='이미지3', null=True, blank=True)
    desc = models.TextField(max_length=300, verbose_name='내용')
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="activity",  null=True, blank=False
    ) 
    

    class Meta:
        ordering = ["-created"]

    @property
    def get_photo_url(self):
      if self.thumnail_img:
          return self.thumnail_img.url
      else:
          return "/static/images/user.jpg"

    @property
    def get_photo_url_a(self):
      if self.img_a:
          return self.img_a.url
      else:
          return None

    @property
    def get_photo_url_b(self):
      if self.img_b:
          return self.img_b.url
      else:
          return None

    @property
    def get_photo_url_c(self):
      if self.img_c:
          return self.img_c.url
      else:
          return None 

class Semester(TimeStampedModel):
    name = models.CharField(max_length=32, verbose_name="학기")

    def __str__(self):
        return self.name 

class Act_Comment(TimeStampedModel):
    # activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='act_comments', null=True)
    desc = models.TextField(max_length=300, null=True, blank=True)
    activity = models.ForeignKey(
        "Activity", on_delete=models.CASCADE, related_name="comm", null=True, blank=True
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="comment_users", null=True, blank=True
    )
    def __str__(self):
        return self.desc
    class Meta:
        db_table = 'comments'


class Challenge(TimeStampedModel): 
    desc = models.TextField(max_length=300)
    users = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="challenge_user",  null=True, blank=True
    ) 

class Challenge_Comment(TimeStampedModel):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='challenge_comments', null=True)
    desc = models.TextField(max_length=300)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="challenge_users",   null=False, blank=False
    )

    def __str__(self):
        return self.desc

    class Meta:
        db_table = 'challenge_comments'


