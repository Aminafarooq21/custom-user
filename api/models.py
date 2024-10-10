from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


class MyUserManager(BaseUserManager):
    def create_user(self,email,password, *extra_fields):
        if not email:
            raise ValueError("email is not given")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is staff should be true for superuser')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser should be True for super user')
        if extra_fields.get('is_active') is not True:
            raise ValueError('is active should be true')

        return self.create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50,blank=True)
    gender = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']

    objects = MyUserManager()