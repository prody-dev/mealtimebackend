from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Rol, User, Categoria, Descuento, Precio 
from .models import Lugar, Estado, Vendedor, Comprador, Producto, Orden, OrdenProducto
from .models import ImagenProducto, Calificacion, CalificacionProducto, CalificacionVendedor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'rol', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = "__all__"

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = "__all__"

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = "__all__"

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__"

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"

class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = "__all__"

class OrdenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenProducto
        fields = "__all__"

class ImagenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = "__all__"

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = "__all__"

class CalificacionProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionProducto
        fields = "__all__"

class CalificacionVendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionVendedor
        fields = "__all__"