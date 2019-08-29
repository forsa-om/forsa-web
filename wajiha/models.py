from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from sorl import thumbnail


class OpportunityCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    slug = models.SlugField(allow_unicode=True)

    title = models.CharField(max_length=250)
    description = models.TextField()

    category = models.ForeignKey(
        OpportunityCategory, models.SET_DEFAULT, default=1)

    image = thumbnail.ImageField(default='default.jpg')

    start_at = models.DateField(null=True, blank=True)
    end_at = models.DateField(null=True, blank=True)

    website = models.URLField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    age_min = models.IntegerField(null=True, blank=True)
    age_max = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    hidden = models.BooleanField(default=True)

    source_url = models.URLField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('wajiha:opportunity_detail', args=[self.pk, self.slug])

    def __str__(self):
        return self.title
