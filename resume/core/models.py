from django.db import models

# Create your models here.
class General_Settings(models.Model):
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
    def __str__(self):
        return f"General Settings: {self.name}"
    class Meta:
        verbose_name = "General Settings"
        verbose_name_plural = "General Settings"
        ordering = ('name',)