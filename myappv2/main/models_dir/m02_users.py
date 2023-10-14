from collections.abc import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from main.models_dir import m01_properties

# Base Manager for Creating and Edit User
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# Custom User for Custom Fields
class CustomUser(AbstractUser, PermissionsMixin):
    username                = None
    profile_picture         = models.ImageField(upload_to = 'profile_pics', blank = True, null = True)
    bio                     = models.TextField(max_length = 512, blank = True, null = True)
    phone                   = PhoneNumberField(unique = True, blank = True, null = True)
    phone_confirmed         = models.BooleanField(blank = True, default = False)
    email                   = models.EmailField(unique = True, blank = True, null = True)
    email_confirmed         = models.BooleanField(blank = True, default = False)
    country                 = models.CharField(max_length = 256, blank = True, null = True)
    city                    = models.CharField(max_length = 256, blank = True, null = True)

    objects                 = CustomUserManager()

    USERNAME_FIELD          = "email"
    REQUIRED_FIELDS         = ["phone"]
    
    
    def clean(self) -> None:
        if not (self.phone or self.email):
            raise ValidationError("Either phone number or email must be provided")
        
        return super().clean()

    def __str__(self) -> str:
        return f"{self.email}"
    

# Authentication Tokens
class AuthTokens(models.Model):
    user            = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True)
    token_type      = models.CharField(max_length = 5, blank = True, null = True)
    device          = models.CharField(max_length = 120, blank = True, null = True)
    tokens          = models.CharField(max_length = 512, blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.user.email}: {self.tokens} on {self.device}/{self.token_type}"
    
    def save(self, *arg, **kwarg):
        return super().save(arg, kwarg)

# Email/Phone Confirmation Model
class EmailPhoneConfirmation(models.Model):
    tokens          = models.CharField(max_length = 64, blank = True, null = True)
    exp_date        = models.DateField(blank = True, null = True)
    user            = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True)
    method          = models.CharField(max_length = 25, blank = True, null = True)
    sms_count       = models.IntegerField(blank = True, null = True)
    email_count     = models.IntegerField(blank = True, null = True)


# Notification
class UserNotification(models.Model):
    message         = models.CharField(max_length = 255, blank = True, null = True)
    user            = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True)
    created_date    = models.DateField(blank = True, null = True)
    is_read         = models.BooleanField(blank = True, default = False)
    is_seen         = models.BooleanField(blank = True, default = False)
    n_code          = models.CharField(max_length = 120, blank = True, null = True)
    link            = models.CharField(max_length = 255, blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.user}: {self.created_date}"


# Wishlist
class Wishlist(models.Model):
    user            = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True)
    name            = models.CharField(max_length = 120, blank = True, null = True)
    items           = models.ManyToManyField("WistlistItem", blank = True)
    date            = models.DateField(blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.id}. {self.user.email}: {self.name}"


# Wishlist Item
class WistlistItem(models.Model):
    property_model  = models.ForeignKey("Property", on_delete = models.CASCADE, blank = True, null = True)
    date_added      = models.DateField(blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.pk}: {self.property_model.name}"
