from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES=(('in progress','In progress'),('completed','completed'),('pending','pending'))
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    date_of_the_task=models.DateField(u'Day of the task', help_text=u'Day of the task',default=timezone.now)
    start_time_of_task=models.TimeField(u'Time to start the Task', help_text=u'Starting time',default=datetime.now().time())
    end_time_of_task=models.TimeField(u'Time to finish the Task', help_text=u'Final time',default=datetime.now().time())
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='In progress')
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    #class Meta:
    #    verbose_name = u'Scheduling Task'
    #    verbose_name_plural = u'Scheduling Task'
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
