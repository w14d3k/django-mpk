from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, pesel, active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last_name")
        if not pesel:
            raise ValueError("User must have a pesel")
        
        user_obj = self.model(
            first_name=first_name,
            last_name=last_name,
            email = self.normalize_email(email),
            pesel=pesel
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = active
        user_obj.save(using = self._db)
        return user_obj
    
    def create_staffuser(self, email, password, first_name, last_name, pesel):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            pesel=pesel,
            is_staff=True
        )
        return user
    
    def create_superuser(self, email, password, first_name, last_name, pesel):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            pesel=pesel,
            is_staff=True,
            is_admin=True
        )
        return user
    
class User(AbstractBaseUser):
   
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    pesel = models.CharField(unique=True, max_length=11, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'pesel']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_pesel(self):
        return self.pesel
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
    