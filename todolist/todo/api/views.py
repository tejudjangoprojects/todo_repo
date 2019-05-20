from django.shortcuts import render
from todo.models import Todo
from todo.forms import TodoForm
from django.views.generic import View
from todo.mixins import HttpResponseMixin,SerializeMixin
from todo.utils import is_json,get_object_by_id
import json

class TodoCRUDCBV(SerializeMixin,HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json only'}),status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            todo=get_object_by_id(id)
            if todo is None:
                return self.render_to_http_response(json.dumps({"msg":'No Record found with the given id'}),status=400)
            json_data=self.serialize([todo,])
            return self.render_to_http_response(json_data)
        qs=Todo.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)
