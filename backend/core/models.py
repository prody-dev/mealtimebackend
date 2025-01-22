from django.db import models
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.rol})"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Descuento(models.Model):
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.porcentaje}% de descuento"

class Precio(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.precio)

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Comprador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE, blank=True, null=True)
    precio = models.ForeignKey(Precio, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.nombre

class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"

class Orden(models.Model):
    fecha_orden = models.DateField()
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Productos = models.ManyToManyField(Producto, through='OrdenProducto')
    
    def __str__(self):
        return f"Orden {self.id} - {self.comprador}"
    
class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.orden} - {self.producto}"


class Calificacion(models.Model):
    calificacion = models.IntegerField()

    def __str__(self):
        return str(self.calificacion)

class CalificacionProducto(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.producto} - {self.calificacion}"

class CalificacionVendedor(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.vendedor} - {self.calificacion}"