from django.db import models
from apps.account.models import Account
from django.utils.text import slugify
from apps.core.models import Setting    
class Category(models.Model):
    title               = models.CharField(max_length=255)
    description         = models.TextField()
    created_date        = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


class Portofolio(models.Model):
    title               = models.CharField(max_length=255)
    featured_image      = models.ImageField()
    client              = models.CharField(max_length=200, null=True)
    slug                = models.SlugField(unique=True, null=True, blank=True, editable=False)
    category            = models.ForeignKey(Category, on_delete=models.RESTRICT)
    project_date        = models.DateTimeField()
    project_url         = models.URLField(null=True, blank=True)
    description         = models.TextField()
    SettingWeb          = models.ForeignKey(Setting, on_delete=models.RESTRICT, null=True, blank=True)
    created_date        = models.DateTimeField(auto_now_add=True)
    created_by          = models.ForeignKey(Account, on_delete=models.RESTRICT, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Portofolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    