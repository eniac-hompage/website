from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel



# Create your models here.
class Activity(TimeStampedModel): 

    SEMI_A = "1학기"
    SEMI_B = "2학기"

    
    SEMI_CHOICES = (
      (SEMI_A, "1학기"),
      (SEMI_B, "1학기"),
    )

    title = models.CharField(max_length=100, default = '', null=True, blank=False)
    semester = models.CharField(choices=SEMI_CHOICES, default = '', max_length=10, blank=False, null=True)
    thumnail_img = models.ImageField(default = '')
    desc = models.TextField(max_length=300)

class Act_Comment(TimeStampedModel):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='act_comments', null=True)
    desc = models.TextField(max_length=300)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="comment_users",   null=False, blank=False
    )

    def __str__(self):
        return self.desc

    class Meta:
        db_table = 'comments'