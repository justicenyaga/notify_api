from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    id_number = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    sub_county = models.CharField(max_length=255, blank=True, null=True)
    ward = models.CharField(max_length=255, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


class PolicePost(models.Model):
    name = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    sub_county = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Case(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    police_post = models.ForeignKey(
        PolicePost, on_delete=models.SET_NULL, null=True)
    case_type = models.CharField(max_length=255)
    case_description = models.TextField()
    filed_on = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    resolved_on = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.first_name + ' ' + self.user.last_name + ' - ' + self.case_type)
