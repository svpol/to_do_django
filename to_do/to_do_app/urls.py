from django.urls import path
from to_do_app import views


app_name = 'to_do_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('edit/<int:task_id>/', views.edit, name='edit'),
    path('done_tasks/', views.done_tasks, name='done_tasks'),
    path('done_true/<int:task_id>', views.done_true, name='done_true'),
    path('reopen/<int:task_id>', views.reopen, name='reopen'),
]