from rest_framework import serializers
from .models import Vehiculo, Matricula, Llanta

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ('id', 'matricula', 'foto')

class LlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llanta
        fields = ('id', 'codigo_de_fabricacion', 'posicion_respecto_al_vehiculo')

class VehiculoSerializer(serializers.ModelSerializer):
    matricula = MatriculaSerializer()
    llantas = LlantaSerializer(many=True)

    class Meta:
        model = Vehiculo
        fields = (
            'id', 'marca', 'modelo', 'placa', 'anio_de_fabricacion', 'color', 'cilindraje', 'tonelaje',
            'unidad_carburaje', 'combustible', 'condicion', 'fotografia', 'matricula', 'llantas'
        )

    def create(self, validated_data):
        matricula_data = validated_data.pop('matricula')
        llantas_data = validated_data.pop('llantas')
        vehiculo = Vehiculo.objects.create(**validated_data)
        Matricula.objects.create(vehiculo=vehiculo, **matricula_data)
        for llanta_data in llantas_data:
            Llanta.objects.create(vehiculo=vehiculo, **llanta_data)
        return vehiculo

    def update(self, instance, validated_data):
        matricula_data = validated_data.pop('matricula')
        llantas_data = validated_data.pop('llantas')
        matricula = instance.matricula
        matricula.matricula = matricula_data.get('matricula', matricula.matricula)
        matricula.foto = matricula_data.get('foto', matricula.foto)
        matricula.save()
        llantas = {llanta.id: llanta for llanta in instance.llantas.all()}
        for llanta_data in llantas_data:
            llanta_id = llanta_data.get('id', None)
            if llanta_id:
                if llanta_id in llantas:
                    llanta = llantas.pop(llanta_id)
                    llanta.codigo_de_fabricacion = llanta_data.get('codigo_de_fabricacion', llanta.codigo_de_fabricacion)
                    llanta.posicion_respecto_al_vehiculo = llanta_data.get('posicion_respecto_al_vehiculo', llanta.posicion_respecto_al_vehiculo)
                    llanta.save()
                else:
                    Llanta.objects.create(vehiculo=instance, **llanta_data)
        for llanta in llantas.values():
            llanta.delete()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
