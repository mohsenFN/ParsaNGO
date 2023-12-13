from django.db import models


class Number(models.Model):
    number = models.CharField(max_length=20,primary_key=True)
    pub_date = models.DateTimeField("date number saved")

class Colab(models.Model):
    fullname = models.CharField(max_length=130)
    number = models.CharField(max_length=11 ,help_text="Phone Numbers will be saved without 0 at start like 914838781")
    code_melli = models.TextField(max_length=10)
    pub_date = models.DateTimeField("date number saved")