from django.db import models

# Create your models here.


class Contact(models.Model):
    """ Contact app's model """

    class Meta:
        verbose_name = 'Contact'

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
        )
    email = models.EmailField(
        max_length=50,
        null=False,
        blank=False
        )
    subject = models.CharField(
        max_length=254,
        null=False,
        blank=False
        )
    content = models.TextField(
        max_length=3000,
        null=False,
        blank=False
        )

    def __str__(self):
        return self.name
