from django.urls import path, include

# import routers
from rest_framework import routers

from . import views

# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
router.register(r'advocates', views.AdvocateViewSet)
router.register(r'companies', views.CompaniesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]