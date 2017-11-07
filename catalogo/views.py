from .models import Producto, Venta, Categoria, UnidadMed, Cliente, ShoppingCart, Departamento, Pedido, Envio, Detalle_Pedido, Tipo_Producto
from rest_framework import serializers, viewsets
from rest_framework import permissions


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class VentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venta
        fields = '__all__'


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Categoria.objects.filter()


class UnidadMedSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnidadMed
        fields = '__all__'


class UnidadMedViewSet(viewsets.ModelViewSet):
    queryset = UnidadMed.objects.all()
    serializer_class = UnidadMedSerializer


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        fields = '__all__'


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class EnvioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envio
        fields = '__all__'


class EnvioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer


class Detalle_PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detalle_Pedido
        fields = '__all__'


class Detalle_PedidoViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Pedido.objects.all()
    serializer_class = Detalle_PedidoSerializer


class Tipo_ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo_Producto
        fields = '__all__'


class Tipo_ProductoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Producto.objects.all()
    serializer_class = Tipo_ProductoSerializer
