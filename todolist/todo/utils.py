import json
from todo.models import Todo
def is_json(data):
    try:
        real_data=json.loads(data)
        valid=True
    except ValueError:
        valid=False
    return valid
def get_object_by_id(id):
    try:
        s=Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        s=None
    return s
