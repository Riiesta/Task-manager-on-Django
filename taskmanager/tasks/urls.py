from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    # Добавьте маршруты для редактирования и удаления по аналогии
]
