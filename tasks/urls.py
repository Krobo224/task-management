from django.urls import path
from .views import add_user, add_task, get_tasks, get_users, delete_task, delete_user, update_task, update_user

urlpatterns = [
    path('api/adduser/', add_user, name='add_user'),
    path('api/add_task/<int:userid>/', add_task, name='add_task'),
    path('api/get_task/<int:userid>/', get_tasks, name='get_tasks'),
    path('api/get_users/', get_users, name="get_users"),
    path('api/delete_task/<int:taskid>/', delete_task, name="delete_task"),
    path('api/delete_user/<int:userid>/', delete_user, name="delete_user"),
    path('api/update_task/<int:taskid>/', update_task, name="update_task"),
    path('api/update_user/<int:userid>/', update_user, name="update_user")
]
