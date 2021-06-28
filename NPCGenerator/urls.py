
from django.urls import path
from . import views # . significa que importa desde el mismo directorio


urlpatterns = [
    path('',views.home, name ='home'),
    path('/NPCGenerator',views.creeateNPC, name ='NPCGenerator'),
]
