from django.db import models
from django.conf import settings

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=20, unique=5)
    # project = models.OneToOneField('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.


class Project(models.Model):
    LANGUAGES = (
        ('en', 'English'),
        ('es', 'Español'),
    )

    language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        default='es',
        help_text='Select language',
    )
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField()
    video = models.URLField(null=True, blank=True)
    description = RichTextField()

    CATEGORIES = (
        ('ins', 'INSTITUCIONAL'),
        ('fic', 'FICCIÓN / NO FICCIÓN'),
        ('mus', 'MÚSICA'),
        ('pol', 'POLÍTICA'),
        ('pub', 'PUBLICIDAD'),
    )
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    is_principal = models.BooleanField(default=False)
    is_shown = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Bio(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    english_bio = RichTextField()
    spanish_bio = RichTextField()

    def __str__(self):
        return self.name
