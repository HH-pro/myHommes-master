from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save


# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The given must be email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    # User Model


class User(AbstractUser):
    # description = models.CharField(max_length=200, default='')
    # city = models.CharField( max_length=200,default='')

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class User_Document(models.Model):
    Your_Email_Address = models.CharField(max_length=100)
    Proof_of_Address = models.FileField(upload_to='documents/')
    Proof_of_ID = models.FileField(upload_to='documents/')
    Bank_Statement = models.FileField(upload_to='documents/')
    Work_payslip  = models.FileField(upload_to='documents/')
    Contract = models.FileField(upload_to='documents/')
    Guarantor_contract = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.Your_Email_Address
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    city = models.CharField(blank=True, max_length=200)
    phone_number = models.IntegerField(blank=True, default='0')


    def __str__(self):
        return self.user.email


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
