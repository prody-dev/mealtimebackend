from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolViewSet, UserViewSet, CustomAuthToken, LogoutView, CategoriaViewSet
from .views import DescuentoViewSet, PrecioViewSet, LugarViewSet, EstadoViewSet, VendedorViewSet, CompradorViewSet
from .views import ProductoViewSet, OrdenViewSet, OrdenProductoViewSet, ImagenProductoViewSet, CalificacionViewSet
from .views import CalificacionProductoViewSet, CalificacionVendedorViewSet

router = DefaultRouter()
router.register(r'rol', RolViewSet)
router.register(r'user', UserViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'descuento', DescuentoViewSet)
router.register(r'precio', PrecioViewSet)
router.register(r'lugar', LugarViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'vendedor', VendedorViewSet)
router.register(r'comprador', CompradorViewSet)
router.register(r'producto', ProductoViewSet)
router.register(r'orden', OrdenViewSet)
router.register(r'orden-producto', OrdenProductoViewSet)
router.register(r'imagen-producto', ImagenProductoViewSet)
router.register(r'calificacion', CalificacionViewSet)
router.register(r'calificacion-producto', CalificacionProductoViewSet)
router.register(r'calificacion-vendedor', CalificacionVendedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]