from django.db import models

class GK_Knowledge(models.Model):
    Sr_No=models.IntegerField()
    Question=models.CharField(max_length=250)
    Option_a=models.CharField(max_length=250)
    Option_b=models.CharField(max_length=250)
    Option_c=models.CharField(max_length=250)
    answer=models.CharField(max_length=250)
    Group=models.CharField(max_length=250)
    def __str__(self):
        return self.Question

class client1(models.Model):
    First=models.CharField(max_length=250)
    Last=models.CharField(max_length=250)
    Phone=models.CharField(max_length=250)
    Query=models.CharField(max_length=250)
    def __str__(self):
        return self.First

    




