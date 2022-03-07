from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    # viet ham thay the create() data in data base
    def _create_user(self, email, password, **extra_field):
        if not email:
            raise ValueError("Email field is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()
        return user
    
    # ham thay the tao superuser
    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)
        extra_field.setdefault('name', "admin")
        if extra_field.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_field.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_field)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"  # khai bao overide username dang nhap bang email
    objects = CustomUserManager()

    def __str__(self):
        return self.email