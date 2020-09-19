from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('export/csv/', views.export_users_csv, name='export_users_csv'),
    path('export/xlsx/', views.export_users_xlsx, name='export_users_xlsx'),
    path('delete/', views.delete_task, name='delete_task'),
]