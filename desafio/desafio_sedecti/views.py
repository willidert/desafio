from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from desafio_sedecti.serializers import PessoaSerializer
from desafio_sedecti.models import Pessoa
from desafio_sedecti.api_regras_de_negocio import RegrasNegocioAvaliador


class PessoaViewSet(ViewSet):

    def list(self, request):
        queryset = Pessoa.objects.order_by('pk')
        serializer = PessoaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PessoaSerializer(data=request.data)
        validador = RegrasNegocioAvaliador()

        if serializer.is_valid() and validador.run(campos=request.data):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Pessoa.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PessoaSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response(status=404)
        serializer = PessoaSerializer(item, data=request.data)
        if serializer.is_valid() and RegrasNegocioAvaliador.run(request.data):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
