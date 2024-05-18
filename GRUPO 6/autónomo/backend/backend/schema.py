import graphene
from graphene_django import DjangoObjectType
from GrapheneRealTime.models import Persona, Equipaje, Boleto

class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona
        fields = ("id", "nombre", "apellido", "id_equipaje", "id_boleto")

class EquipajeType(DjangoObjectType):
    class Meta:
        model = Equipaje
        fields = ("id", "marca", "numero_objeto")

class BoletoType(DjangoObjectType):
    class Meta:
        model = Boleto
        fields = ("id", "codigo", "precio")

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello")

    personas = graphene.List(PersonaType)
    boletos = graphene.List(BoletoType)
    equipajes = graphene.List(EquipajeType)

    def resolve_personas(self, info):
        return Persona.objects.all()

    def resolve_equipajes(self, info):
        return Equipaje.objects.all()

    def resolve_boletos(self, info):
        return Boleto.objects.all()

class CrearPersona(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()
        id_equipaje = graphene.ID()
        id_boleto = graphene.ID()

    persona = graphene.Field(PersonaType)

    def mutate(self, info, nombre, apellido, id_equipaje, id_boleto):
        equipaje = Equipaje.objects.get(pk=id_equipaje)
        boleto = Boleto.objects.get(pk=id_boleto)
        persona = Persona(nombre=nombre, apellido=apellido, id_equipaje=equipaje, id_boleto=boleto)
        persona.save()
        return CrearPersona(persona=persona)

class Mutation(graphene.ObjectType):
    crear_persona = CrearPersona.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
