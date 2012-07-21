# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import slugify

def my_filename(instance,filename):
    fname, dot, extension = filename.rpartition('.')
    slug = slugify(instance.jrm_id)
    return 'uploads/%s.%s' % (slug, extension)


class Ad(models.Model):
    minute=models.IntegerField(verbose_name=u"号码",db_index=True)
    imgfile=models.ImageField(upload_to=my_filename,null=True,blank=True)
    def __unicode__(self):
        return unicode(self.minute)



class AdUser(models.Model):
    user=models.ForeignKey(User)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    user_ad=models.ManyToManyField(Ad)
    def __unicode__(self):
        return self.user.username+":"+u"由"+self.start_time.isoformat(" ")+u"开始的广告租用"









