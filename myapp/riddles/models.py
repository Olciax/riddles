from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Riddles(models.Model):
    text = models.TextField()
    img = models.TextField(null=True, blank=True)
    answer = models.TextField()
    hint = models.TextField(null=True, blank=True)
    points = models.SmallIntegerField()

    class Meta:
        ordering = ('id', )
    def __str__(self):

        return f"Zagadka {self.id}"

class Level(models.Model):
    name = models.CharField(max_length=48)
    riddles = models.ManyToManyField(Riddles)

    def __str__(self):
        return f"{self.name}"


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.SmallIntegerField()
    img = models.ImageField(blank=True, null=True, upload_to="Pulpit/costam")
    editname = models.BooleanField(default=False)
    editmail = models.BooleanField(default=False)
    editimg = models.BooleanField(default=False)
    donecur = models.BooleanField(default=False)

    class Meta:
        ordering = ['points']

    def get_absolute_url(self):
        return reverse('details', kwargs={'user_id': self.pk})




class DoneRiddles(models.Model):
    riddles = models.ForeignKey(Riddles, on_delete=models.CASCADE)
    my_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)



class CuriosityQA(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=128)


class Curiosity(models.Model):
    text = models.TextField()
    img = models.ImageField(blank=True, null=True, upload_to="Pulpit/costam")
    curiosityQA = models.ManyToManyField(CuriosityQA)

class DoneCuriosity(models.Model):
    curiosity = models.ForeignKey(Curiosity, on_delete=models.CASCADE)
    my_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)











# Create your models here.
