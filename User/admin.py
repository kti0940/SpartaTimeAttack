from django.contrib import admin
from User.models import User as UserModel
from User.models import UserType as UserTypeModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserTypeModel)