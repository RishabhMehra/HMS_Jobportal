from django.contrib import admin
from .models import *

# Register your models here.


# this is USER MODEL
admin.site.register(StudentUser)

# this is recruiter model
admin.site.register(Recruiter)

# this is admin model
