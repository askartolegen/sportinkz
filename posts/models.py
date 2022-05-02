from django.db import models
from django.urls import reverse


# Create your models here.
class User_people(models.Model):
    username = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Username')
    fname = models.CharField(max_length=255, verbose_name='First Name')
    lname = models.CharField(max_length=255, verbose_name='Last Name')
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email Address')
    pass1 = models.CharField(max_length=255, verbose_name='Password')
    pass2 = models.CharField(max_length=255, verbose_name='Confirm Your Password')
    country = models.CharField(max_length=255, verbose_name='Country')
    city = models.CharField(max_length=255, verbose_name='City')


    # def get_absolute_url(self):
    #     return reverse('user-detail', args=[str(self.id)])

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.username})


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Boxing(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Boxing"
        verbose_name_plural = "Boxers"
        # ordering = ['-title', 'content']

class Wrestling(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Wrestling"
        verbose_name_plural = "Wrestlers"


class Athletics(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Athletics"
        verbose_name_plural = "Athletes"

class Weightlifting(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Weightlifting"
        verbose_name_plural = "Weightlifters"

class Cycling(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Cycling"
        verbose_name_plural = "Cyclists"

class Team_sports(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Team_sports"
        verbose_name_plural = "Teams"



