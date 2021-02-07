from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

#Manager
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Email is mandatory for users")
        if not username:
            raise ValueError("Usernames are mandatory for users")

        user = self.model(
            #Normalize email converts email to all lowercase
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            # Normalize email converts email to all lowercase
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
#Object
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    #Mandatory fields for custmon user model below
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #Method the user uses to login. mandatory
    USERNAME_FIELD = 'email'
    #Below can be used to force user to input info. Not mandatory
    REQUIRED_FIELDS = ['username',]

    #Includes the manager
    objects= MyAccountManager()

    #Mandatory methods for custom user.
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

