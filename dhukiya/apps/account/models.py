from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, username, email,first_name,last_name, password=None):
        if not username:
            raise ValueError("user must have an username")
        if not email:
            raise ValueError("User must have an Email")
        if not first_name:
            raise ValueError("User must have an Firs Name")
        if not last_name:
            raise ValueError("User must have an Last Name")

        
        user = self.model(
            email = self.normalize_email(email), 
            username = username,
            first_name = first_name,
            last_name = last_name
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,first_name,last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,

        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class Divisi(models.Model):
    div_title           = models.CharField(max_length=5, null=True)
    div_descriptions    = models.CharField(max_length=100, null=True)
    div_created_date    = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.div_title


class Account(AbstractBaseUser):
    username    = models.CharField(max_length=20, unique=True)
    email       = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name  = models.CharField(max_length=255, null=False)
    last_name   = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    role        = models.ForeignKey(Divisi, on_delete=models.RESTRICT, null=True)
    about_me    = models.TextField(null=True)
    facebook    = models.URLField(null=True, blank=True)
    twitter     = models.URLField(null=True, blank=True)
    instagram   = models.URLField(null=True, blank=True)
    website     = models.URLField(null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name' ]

    objects = AccountManager()

    def __str__(self):
        return str(self.first_name)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

