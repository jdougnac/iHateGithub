
from django.urls import path
from . import views # . significa que importa desde el mismo directorio


urlpatterns = [
    path('/chapters/',views.createChapter, name ='createChapter'),    
]
