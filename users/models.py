from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from clients.models import Client
import uuid

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The Username field is required')

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_operator(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_operator = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    telegram_username = models.CharField(max_length=150, unique=True, null=True)
    phone_number = models.CharField(max_length=150, unique=True, null=True)
    username = models.CharField(max_length=150, unique=True, null=True)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    unique_user_id = models.CharField(max_length=255, unique=True, default=uuid.uuid4, null=True)   
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        if self.is_operator and perm.endswith('delete'):
            return False
        return True

    def has_module_perms(self, app_label):
        return True
        

    @property
    def is_staff(self):
        return self.is_admin or self.is_operator

    def save(self, *args, **kwargs):
        if not self.first_name or not self.last_name or not self.phone_number or not self.unique_user_id and not self.is_admin and not self.is_operator:
            raise ValueError('First name, last name, phone number, and unique user ID are required fields')
        
        if not self.unique_user_id:
            self.unique_user_id = f"{self.first_name}{self.last_name}{uuid.uuid4()}"
        
        if not self.username:
            self.username = self.unique_user_id
        
        super(User, self).save(*args, **kwargs)