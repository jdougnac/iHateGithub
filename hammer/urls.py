
from django.urls import path
from . import views # . significa que importa desde el mismo directorio


urlpatterns = [
    path('',views.home, name ='home'),
    path('/createItem', views.createItem),
    path('/createMutation', views.createMutation),
    path('/runes', views.runes),
]
