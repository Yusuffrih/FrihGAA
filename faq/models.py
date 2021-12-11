from django.db import models

# Create your models here.


class Faq(models.Model):
    class Meta:
        verbose_name_plural = 'FAQs'

    question = models.TextField(max_length=300, null=False, blank=False)
    answer = models.TextField(max_length=900, null=False, blank=False)

    def __str__(self):
        return self.question
