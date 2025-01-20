from rest_framework import viewsets, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rol, User, Categoria, Descuento, Precio 
from .models import Lugar, Estado, Vendedor, Comprador, Producto, Orden, ProductoOrden
from .models import ImagenProducto, Calificacion, CalificacionProducto, CalificacionVendedor
from .serializers import RolSerializer, UserSerializer, CategoriaSerializer
from .serializers import DescuentoSerializer, PrecioSerializer, LugarSerializer, EstadoSerializer
from .serializers import VendedorSerializer, CompradorSerializer, ProductoSerializer, OrdenSerializer
from .serializers import ProductoOrdenSerializer, ImagenProductoSerializer, CalificacionSerializer
from .serializers import CalificacionProductoSerializer, CalificacionVendedorSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print("Solicitud de login recibida")
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        rol = user.rol  # Asegúrate de que el modelo User tenga un campo 'rol'
        print(f"Token generado: {token.key}")
        print(f"Usuario: {user.username}, Rol: {rol.name}")  # Asumiendo que el modelo Rol tiene un campo 'nombre'
        return response

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        print("Solicitud de logout recibida")
        try:
            auth_header = request.headers.get('Authorization')
            if (auth_header and auth_header.startswith('Token ')):
                token_key = auth_header.split(' ')[1]
                token = Token.objects.get(key=token_key)
                print(f"Token a eliminar: {token.key}")
                token.delete()
                print("Token eliminado")
                return Response(status=status.HTTP_200_OK)
            else:
                print("No se encontró el token en la solicitud")
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Token.DoesNotExist:
            print("Token no válido")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error al procesar la solicitud de logout: {e}")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer

class PrecioViewSet(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class CompradorViewSet(viewsets.ModelViewSet):
    queryset = Comprador.objects.all()
    serializer_class = CompradorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class ProductoOrdenViewSet(viewsets.ModelViewSet):
    queryset = ProductoOrden.objects.all()
    serializer_class = ProductoOrdenSerializer

class ImagenProductoViewSet(viewsets.ModelViewSet):
    queryset = ImagenProducto.objects.all()
    serializer_class = ImagenProductoSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class CalificacionProductoViewSet(viewsets.ModelViewSet):
    queryset = CalificacionProducto.objects.all()
    serializer_class = CalificacionProductoSerializer

class CalificacionVendedorViewSet(viewsets.ModelViewSet):
    queryset = CalificacionVendedor.objects.all()
    serializer_class = CalificacionVendedorSerializer
