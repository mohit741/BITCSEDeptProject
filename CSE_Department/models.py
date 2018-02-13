from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import ProfileManager


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Profile')
    name = models.CharField(max_length=50, default='dummy')
    dept = models.CharField(max_length=20, default='CSE')
    phone = models.CharField(max_length=15, default='1234567890')

    objects = ProfileManager()

    @property
    def username(self):
        return self.user.username

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
    corresAuthors = models.CharField(max_length=100)
    paperTitle = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    impactFac = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    pp = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UnpaidScopus(models.Model):
    authors = models.CharField(max_length=100)
    corresAuthors = models.CharField(max_length=100)
    paperTitle = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    impactFac = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    pp = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PaidScopus(models.Model):
    authors = models.CharField(max_length=100)
    corresAuthors = models.CharField(max_length=100)
    paperTitle = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    impactFac = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    pp = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OtherJournals(models.Model):
    authors = models.CharField(max_length=100)
    corresAuthors = models.CharField(max_length=100)
    paperTitle = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    impactFac = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    pp = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ConferencesAttended(models.Model):
    authors = models.CharField(max_length=100)
    paperTitle = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    place = models.CharField(max_length=100)
    orgInstitute = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SeminarsAttended(models.Model):
    authors = models.CharField(max_length=100)
    paperTitle = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    place = models.CharField(max_length=100)
    orgInstitute = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class WorkshopsAttended(models.Model):
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    place = models.CharField(max_length=100)
    orgInstitute = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TrainingProgAttended(models.Model):
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    place = models.CharField(max_length=100)
    orgInstitute = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ConferencesOrg(models.Model):
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    orgInstitute = models.CharField(max_length=50)
    fundingAgency = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class WorkshopsOrg(models.Model):
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    orgInstitute = models.CharField(max_length=50)
    fundingAgency = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SeminarsOrg(models.Model):
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    orgInstitute = models.CharField(max_length=50)
    fundingAgency = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
