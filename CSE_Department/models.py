from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Profile',
                                verbose_name='Employee ID')
    name = models.CharField(max_length=50, default='dummy', verbose_name='Name')
    dept = models.CharField(max_length=20, default='CSE', verbose_name='Department')
    phone = models.CharField(max_length=15, default='1234567890', verbose_name='Phone')
    desgn = models.CharField(max_length=20, default='staff', verbose_name='Designation')

    @property
    def username(self):
        return self.user.username

    def status(self):
        return self.desgn

    class Meta:
        ordering = ("user",)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()


class SCIJournals(models.Model):
    authors = models.CharField(max_length=100)
    corresAuthors = models.CharField(max_length=100, verbose_name='Corresponding Authors')
    paperTitle = models.CharField(max_length=50, verbose_name='Paper Title')
    name = models.CharField(max_length=50, verbose_name='Name')
    impactFac = models.CharField(max_length=50, verbose_name='Impact Factor')
    volume = models.CharField(max_length=50)
    pp = models.CharField(max_length=50, verbose_name='PP')
    year = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UnpaidScopus(models.Model):
    authors = models.CharField(max_length=100)
    corresAuthors = models.CharField(max_length=100, verbose_name='Corresponding Authors')
    paperTitle = models.CharField(max_length=50, verbose_name='Paper Title')
    name = models.CharField(max_length=50, verbose_name='Name')
    impactFac = models.CharField(max_length=50, verbose_name='Impact Factor')
    volume = models.CharField(max_length=50)
    pp = models.CharField(max_length=50, verbose_name='PP')
    year = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PaidScopus(models.Model):
    authors = models.CharField(max_length=100)
    corresAuthors = models.CharField(max_length=100, verbose_name='Corresponding Authors')
    paperTitle = models.CharField(max_length=50, verbose_name='Paper Title')
    name = models.CharField(max_length=50, verbose_name='Name')
    impactFac = models.CharField(max_length=50, verbose_name='Impact Factor')
    volume = models.CharField(max_length=50)
    pp = models.CharField(max_length=50, verbose_name='PP')
    year = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OtherJournals(models.Model):
    authors = models.CharField(max_length=100)
    corresAuthors = models.CharField(max_length=100, verbose_name='Corresponding Authors')
    paperTitle = models.CharField(max_length=50, verbose_name='Paper Title')
    name = models.CharField(max_length=50, verbose_name='Name')
    impactFac = models.CharField(max_length=50, verbose_name='Impact Factor')
    volume = models.CharField(max_length=50)
    pp = models.CharField(max_length=50, verbose_name='PP')
    year = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ConferencesAttended(models.Model):
    authors = models.CharField(max_length=100)
    paperTitle = models.CharField(max_length=50, verbose_name='Paper Title')
    name = models.CharField(max_length=50)
    total_duration = models.IntegerField()
    place = models.CharField(max_length=100)
    orgInstitute = models.CharField(max_length=50, verbose_name='Organising Institute')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SeminarsAttended(models.Model):
    authors = models.CharField(max_length=100)
    paperTitle = models.CharField(max_length=50, verbose_name='Paper Title')
    name = models.CharField(max_length=50)
    total_duration = models.IntegerField()
    place = models.CharField(max_length=100)
    orgInstitute = models.CharField(max_length=50, verbose_name='Organising Institute')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class WorkshopsAttended(models.Model):
    name = models.CharField(max_length=50)
    total_duration = models.IntegerField()
    place = models.CharField(max_length=100)
    orgInstitute = models.CharField(max_length=50, verbose_name='Organising Institute')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TrainingProgAttended(models.Model):
    name = models.CharField(max_length=50)
    total_duration = models.IntegerField()
    place = models.CharField(max_length=100)
    orgInstitute = models.CharField(max_length=50, verbose_name='Organising Institute')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ConferencesOrg(models.Model):
    name = models.CharField(max_length=50)
    total_duration = models.IntegerField()
    orgInstitute = models.CharField(max_length=50, verbose_name='Organising Institute')
    fundingAgency = models.CharField(max_length=100, verbose_name='Funding Agency')
    role = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class WorkshopsOrg(models.Model):
    name = models.CharField(max_length=50)
    total_duration = models.IntegerField()
    orgInstitute = models.CharField(max_length=50, verbose_name='Organising Institute')
    fundingAgency = models.CharField(max_length=100, verbose_name='Funding Agency')
    role = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SeminarsOrg(models.Model):
    name = models.CharField(max_length=50)
    total_duration = models.IntegerField()
    orgInstitute = models.CharField(max_length=50, verbose_name='Organising Institute')
    fundingAgency = models.CharField(max_length=100, verbose_name='Funding Agency')
    role = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
