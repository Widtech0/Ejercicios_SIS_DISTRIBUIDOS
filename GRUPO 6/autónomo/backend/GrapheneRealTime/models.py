from django.db import models

class Equipaje(models.Model):
    marca = models.TextField("Marca")
    numero_objeto = models.IntegerField("Numero de objetos")

    def __str__(self) -> str:
        return self.marca

class Boleto(models.Model):
    codigo = models.TextField("Nombre", max_length=50, blank=True,null=True)
    precio = models.IntegerField("Precio")

    def __str__(self) -> str:
        return self.codigo

class Persona(models.Model):
    nombre = models.TextField("Nombre", max_length=50, blank=True,null=True)
    apellido = models.TextField("Apellido", max_length=50 , blank=True,null=True)
    id_equipaje = models.ForeignKey(Equipaje, on_delete=models.CASCADE )
    id_boleto = models.ForeignKey(Boleto, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.nombre + self.apellido )
