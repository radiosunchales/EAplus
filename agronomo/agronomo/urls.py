from django.contrib import admin
from django.urls import path, include
from cognito import views

from cognito.api.views import Alta_usuarios_View
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", Alta_usuarios_View, basename='alta_usuario_view')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='signin'),
    path('sign-out/', views.signout, name='signout'),
    path('api/', include(route.urls)),
]
