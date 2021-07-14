from django.conf.urls import url
from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.index, name='todo-index'),
    path('update/<int:pk>/',views.update, name='todo-update'),
    path('delete/<int:pk>/',views.delete, name='todo-delete'),

]


