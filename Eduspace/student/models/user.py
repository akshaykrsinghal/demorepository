from django.db import models
from django.core.validators import MinLengthValidator


class user_login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Rollno=models.CharField(max_length=50)



    def __str__(self):
        return self.email

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return user_login.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if user_login.objects.filter(email=self.email):
            return True

        return False


class user(models.Model):
    profile_img = models.ImageField(upload_to='profile_img')
    mobile = models.IntegerField()
    emailid = models.CharField(max_length=50)
    rollno=models.CharField(max_length=50)
    def __str__(self):
        return self.emailid

class education_detail(models.Model):
    emailid = models.ForeignKey(user, on_delete=models.CASCADE)
    sec_roll=models.CharField(max_length=50)
    sec_school = models.CharField(max_length=50)
    sec_board = models.CharField(max_length=10)
    sec_percent = models.IntegerField()
    Int_roll=models.CharField(max_length=40)
    Int_school = models.CharField(max_length=50)
    Int_board = models.CharField(max_length=10)
    Int_percent = models.IntegerField()
    def __str__(self):
        return self.emailid


class graduation(models.Model):
    emailid = models.ForeignKey(education_detail, on_delete=models.CASCADE)
    grad_roll=models.CharField(max_length=10)
    clg_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=10)
    sem1 = models.IntegerField()
    sem2 = models.IntegerField()
    sem3 = models.IntegerField()
    sem4 = models.IntegerField()
    sem5 = models.IntegerField()
    sem6 = models.IntegerField()
    sem7 = models.IntegerField()
    sem8 = models.IntegerField()
    def __str__(self):
        return self.emailid
