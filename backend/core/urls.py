from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolViewSet, UserViewSet, CustomAuthToken, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'rol', RolViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]