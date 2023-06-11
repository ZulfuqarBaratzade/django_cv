from django.db import models

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