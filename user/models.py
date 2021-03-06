from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, username,email, password):
        if not username:
            raise ValueError('Users must have a username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            # email=self.normalize_email(email),        
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,password):
        user = self.create_user(
            username=username,
            email="naseemudheene@gmail.com",
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60,blank=True)
    username = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    phone = models.CharField(max_length=20,unique=False,blank=True)
    address = models.CharField(max_length=140,blank=True)

    USERNAME_FIELD = 'username'

    # REQUIRED_FIELDS = []
    objects = MyUserManager()


    def __str__(self):
        return str(self.username)

    def has_perm(self,perm,obj=None):
        return self.is_admin
        
    def has_module_perms(self,app_label):
        return True
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        email = self.username