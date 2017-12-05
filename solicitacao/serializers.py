from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from solicitacao.models import *
from django.conf.urls import url, include


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'email', 'cargo')

    def create(self, validated_data):
        validated_data = dados.pop('funcionario')
        u = User.objects.create(**validated_data)
        p = Funcionario.objects.create(funcionario=u, **validated_data)
        return p

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instace.nome)
        instace.email = validated_data.get('content', instace.content)
        instace.cargo = validated_data.get('cargo', instace.cargo)
        instace.created = validated_data.get('created', instace.created)
        instance.save()
        return instance

class SolicitacaoSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(many=False)
    class Meta:
        model = Solicitacao
        fields = ('origem', 'destino', 'funcionario', 'data')

    def create(self, validated_data):
        validated_data = dados.pop('solicitacao')
        u = Solicitacao.objects.create(**validated_data)
        p = Funcionario.objects.create(solicitacao=u, **validated_data)
        return p

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('origem', instace.origem)
        instace.email = validated_data.get('destino', instace.desino)
        instace.cargo = validated_data.get('funcionario', instace.funcionario)
        instace.data = validated_data.get('data', instace.data)
        instace.created = validated_data.get('created', instace.created)
        instance.save()
        return instance

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ('placa', 'marca', 'modelo', 'ano')

    def create(self, validated_data):
        validated_data = dados.pop('veiculo')
        u = Veiculo.objects.create(**validated_data)
        p = Veiculo.objects.create(Veiculo=u, **validated_data)
        return p

    def update(self, instance, validated_data):
        instance.placa = validated_data.get('placa', instace.placa)
        instace.marca = validated_data.get('marca', instace.marca)
        instace.modelo = validated_data.get('modelo', instace.modelo)
        instace.ano = validated_data.get('ano', instace.ano)
        instace.created = validated_data.get('created', instace.created)
        instance.save()
        return instance

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = ('cnh', 'nome', 'categoria')

    def create(self, validated_data):
        validated_data = dados.pop('motorista')
        u = Motorista.objects.create(**validated_data)
        p = Motorista.objects.create(Motorista=u, **validated_data)
        return p

    def update(self, instance, validated_data):
        instance.cnh = validated_data.get('cnh', instace.cnh)
        instace.nome = validated_data.get('nome', instace.nome)
        instace.categoria = validated_data.get('categoria', instace.categoria)
        instace.created = validated_data.get('created', instace.created)
        instance.save()
        return instance

class AtendimentoSerializer(serializers.ModelSerializer):
    veiculo = VeiculoSerializer(many=False)
    motorista = MotoristaSerializer(many=False)
    solicitacao = SolicitacaoSerializer(many=False)
    class Meta:
        model = Atendimento
        field = ('veiculo', 'motorista', 'solicitacao',)

    def create(self, validated_data):
        validated_data = dados.pop('atendimento')
        u = Atendimento.objects.create(**validated_data)
        p = Atendimento.objects.create(atendimento=u, **validated_data)
        return p

    def update(self, instance, validated_data):
        instance.veiculo = validated_data.get('veiculo', instace.veiculo)
        instace.motorista = validated_data.get('motorista', instace.motorista)
        instace.solicitacao = validated_data.get('solicitacao', instace.solicitacao)
        instace.created = validated_data.get('created', instace.created)
        instance.save()
        return instance
