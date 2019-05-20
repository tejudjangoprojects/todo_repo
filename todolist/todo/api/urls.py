from django.conf.urls import url,include
from todo.api.views import TodoCRUDCBV

urlpatterns=[
url(r'',TodoCRUDCBV.as_view())
]
