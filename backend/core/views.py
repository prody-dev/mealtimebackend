from rest_framework import viewsets, permissions, status
from .models import Rol, User
from .serializers import RolSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

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
            if auth_header and auth_header.startswith('Token '):
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