from django.db import models
from django.core.validators import MinLengthValidator


class admin_login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    admin_id=models.CharField(max_length=50)



    def __str__(self):
        return self.email

    def register(self):
        self.save()

    @staticmethod
    def get_admin_by_email(email):
        try:
            return admin_login.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if admin_login.objects.filter(email=self.email):
            return True

        return False


class admindata(models.Model):
    profile_img = models.ImageField(upload_to='user/profile_img/')
    mobile = models.IntegerField()
    rollno=models.CharField(max_length=50)
    def __str__(self):
        return self.emailid

