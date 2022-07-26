from django.urls import  path
from . import views
urlpatterns=[
    #path(请求地址,访问views中的index方法，)
    path('',views.index,name='index')
]