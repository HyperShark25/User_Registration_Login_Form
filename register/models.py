from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager



class Custom_User_Model(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
