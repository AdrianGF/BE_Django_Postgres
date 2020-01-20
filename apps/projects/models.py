import datetime
from django.db import models
# from django.utils import timezone

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    financed = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    # def __str__(self):
    #     return self.question_text
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)