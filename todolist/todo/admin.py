from django.contrib import admin
from todo.models import Todo
import csv,io
from django.shortcuts import render,redirect,HttpResponse
from django.conf.urls import url,include
from django.contrib import admin
from todo import views
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=['id','title','description','date_of_the_task','start_time_of_task','end_time_of_task','status','created','modified']
    list_filter = ('created', 'modified',)
    search_fields = ('title', 'description')
    ordering=('-created',)
    #readonly_fields = ('download_link',)
    #fieldsets=(None,{'fields':('title','description','date_of_the_task','start_time_of_task','end_time_of_task','status')}),
    #('Advanced Options',{
    #'classes':('collapse',),'fields':('download_link',)
    #})

    def get_urls(self):
        urls=super().get_urls()
        urls+=[
        url(r'^download_file/', self.download_file,name='todo_todo_download-file'),
        ]
        return urls

    def download_link(self):
        return format_html(
            '<a href="/download-file">Download file</a>',
            reverse('admin:todo_todo_download-file')
        )
    download_link.short_description = "Download file"

    def download_file(self, request):
        tasks=Todo.objects.all()
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment; filename="todotasks.csv"'
        writer=csv.writer(response, delimiter=',')
        writer.writerow(['title', 'description', 'date_of_the_task', 'start_time_of_task', 'end_time_of_task', 'status', 'created', 'modified'])
        for obj in tasks:
            writer.writerow([obj.title, obj.description, obj.date_of_the_task, obj.start_time_of_task, obj.end_time_of_task, obj.status, obj.created, obj.modified])
        return response

admin.site.register(Todo,TodoAdmin)
