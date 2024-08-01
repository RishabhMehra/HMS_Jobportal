from django.db import models
from django.contrib.auth.models import User


# this is USER MODEL
class StudentUser(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # cascade means child se bhi delete ho jaye  #here user is child tht we hv created User is given by django
    mobile = models.CharField(
        max_length=15, null=True
    )  # null true means it is not neccesary to fill data
    image = models.FileField(null=True)
    gender = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=15, null=True)

    def _str_(self):

        return (
            self.user.username
        )  # this is user from already created user in django admin


# this is recruiter model
class Recruiter(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # cascade means child se bhi delete ho jaye
    mobile = models.CharField(
        max_length=15, null=True
    )  # null true means it is not neccesary to fill data
    image = models.FileField(null=True)
    gender = models.CharField(max_length=15, null=True)
    company = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(
        max_length=15, null=True
    )  # jab tak admin accept na kre tab tak pending aaye status

    def _str_(self):
        return self.user.username
