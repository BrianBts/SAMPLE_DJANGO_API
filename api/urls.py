from django.urls import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet)

urlpatterns=[
    path('', include(router.urls))
]

#ESTE ARCHIVO SE CREA LAS RUTAS CORRESPONDIENTES PARA LA ENTIDAD PROGRAMMERS ->r'programmers'<- A APARTIR DE SU VIEWSET ->views.ProgrammerViewSet<-
