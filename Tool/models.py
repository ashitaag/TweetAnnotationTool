from django.db import models

# Create your models here.

class Tweet(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.CharField(max_length = 300)
    key_term_injured = models.CharField(max_length = 1000, default="[]")
    key_term_killed = models.CharField(max_length= 1000, default="[]")
    accident_related = models.BooleanField(default=False)
    informative = models.BooleanField(default=False)
    num_killed = models.IntegerField(default=0)
    num_vehicles = models.IntegerField(default=0)
    key_term_num_vehicles = models.CharField(max_length=1000, default="[]")
    num_injured = models.IntegerField(default=0)
    severity = models.BooleanField(default=False)
    is_annotated = models.BooleanField(default=False)



