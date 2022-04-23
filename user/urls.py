from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='user_view'),
    path('addUser', views.addUser, name='user_add'),
    path('editUser/<int:id>', views.editUser,name='user_edit'),
    path('deleteUser/<int:id>', views.deleteUser,name='user_delete'),
]