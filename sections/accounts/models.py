from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MemberManager(BaseUserManager):
    def create_user(self, email, username, role, password=None): # Only required fields as param
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        user = self.model(
            email = self.normalize_email(email), # Normalize used to change capitals into lower case
            username = username,
            role = role,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, role, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            role = role,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class Member(AbstractBaseUser):
    class Role(models.TextChoices):
        STUDENT = 'S', "Student"
        TECAHER = 'T', "Teacher"
        SYSTEM_MANAGER = 'M', "System Manager" 
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(verbose_name="Username", max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateField(verbose_name="Last Login", auto_now=True)
    role = models.CharField(verbose_name="Role", choices=Role.choices, default=Role.STUDENT, max_length=10)
    # Required defaults
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # Login parameter
    REQUIRED_FIELDS = ['username', 'role']

    objects = MemberManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    
