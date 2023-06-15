from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class AbstractModel(models.Model):
    updated_date=models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='update_date',

    )
    created_date=models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='created_date'
    )
    class Meta:
        abstract = True

class General_Settings(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    description=models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='description',
    )
    parameter=models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='parameter'

    )

    def __str__(self):
        return f"General Settings: {self.name}"
    class Meta:
        verbose_name = "General Settings"
        verbose_name_plural = "General Settings"
        ordering = ('name',)
class ImageSettings(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    description=models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='description',
    )
    file = models.ImageField(
        default='',
        help_text='',
        verbose_name='Image',
        blank=True,
        upload_to='images/',
    )
    def __str__(self):
        return f"Image Setttings : {self.name}"
    class Meta:
        verbose_name = "Image Settings"
        verbose_name_plural = "Image Settings"
        ordering = ('name',)
class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='name',

    )
    percentage= models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    def __str__(self):
        return f"Skill Setttings : {self.name}"
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skill"
        ordering = ('order',)
class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',

    )
    job_title=models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',

    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location'

    )
    start_date = models.DateField(
        verbose_name='Start Date',

    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',

    )
    def __str__(self):
        return f"Experience : {self.company_name}"
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"
        ordering = ('start_date',)


class Education(AbstractModel):
    edu_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Education Name',

    )
    edu_title=models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Education Title',

    )
    edu_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Education Location'

    )
    start_date = models.DateField(
        verbose_name='Start Date',

    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',

    )
    def __str__(self):
        return f"Education : {self.edu_name}"
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ('start_date',)


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
    )
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon'
    )

    def __str__(self):
        return f"Social Media : {self.link}"
    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"
        ordering = ('order',)
