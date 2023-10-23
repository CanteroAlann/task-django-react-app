from django.urls import path
from .views import TaskList, UserList,TaskDetail


app_name = "task"

urlpatterns = [
    path("", TaskList.as_view()),
    path('task/<int:pk>/', TaskDetail.as_view()),

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserList.as_view()),
]
