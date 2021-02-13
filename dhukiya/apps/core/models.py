from django.db import models


class Seo(models.Model):
    pass

class Setting(models.Model):
    site_title                  = models.CharField(max_length=200)
    site_shortdescription       = models.CharField(max_length=255, null=True, blank=True)
    site_descriptions           = models.TextField(verbose_name='Descriptions')
    site_address                = models.CharField(verbose_name='Address', max_length=255, null=True, blank=True)
    site_phone                  = models.CharField(verbose_name='Phone Number',null=True, max_length=14)
    site_email                  = models.EmailField(null=True)
    site_opentime               = models.TimeField(null=True)
    site_closetime              = models.TimeField(null=True)
    site_logo                   = models.ImageField(null=True, blank=True)
    site_icon                   = models.ImageField(verbose_name='icon',null=True, blank=True)
    site_social_fb              = models.URLField(verbose_name='Facebook Page',null=True, blank=True)
    site_social_twitter         = models.URLField(verbose_name='Twitter Page',null=True, blank=True)
    site_social_instagram       = models.URLField(verbose_name='Instagram Account',null=True, blank=True)
    last_update                 = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.site_title


