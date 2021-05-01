from django.urls import path
from .views import *


urlpatterns = [
    path('login/', UserLogin.as_view(), name = "login_page"),
    path('logout/', LogoutView.as_view(next_page = 'login_page'), name = "logout_page"),
    path('register/', UserRegister.as_view(), name = 'register_page'),

    
    path('', TaskList.as_view(), name = "main_page"),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name = "task_detail_page"),
    path('task_edit/<int:pk>', TaskUpdate.as_view(), name = 'task_edit_page'),
    path('task_create/', TaskCreate.as_view(), name = 'task_create_page'),
    path('task_delete/<int:pk>', TaskDelete.as_view(), name = 'task_delete_page')
]