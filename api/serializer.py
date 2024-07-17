# serializer.py
from rest_framework import serializers
from backProzone.models import (
    col_departamento, col_roles, Employee, Profile, prd_Almacen, prd_contacto_proveedor,
    prd_categorias, prd_producto, prd_lotes, prd_producto_catalogo, pd_clientes, 
    pd_pedidos, ped_detalles_pedido, env_vehiculos, env_rutas, env_tipo_vehiculo,
    env_conductores, env_conductores_vehiculos, env_envio, env_estado_envio, env_historial_envios
)
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'nombre', 'apellido', 'telefono', 'email', 'password', 'status', 'fecha_ingreso', 'user', 'rol', 'departamento']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'user_id': self.user.id,})

        # Obtener información del empleado
        empleado_data = Employee.objects.filter(user=self.user).values().first()
        if empleado_data:
            data.update({'empleado': empleado_data})

            # Obtener información del perfil del empleado
            perfil_data = Profile.objects.filter(employee__user=self.user).values().first()
            if perfil_data:
                data.update({'perfil': perfil_data})

        return data

class ColDepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_departamento
        fields = '__all__'

class ColRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = col_roles
        fields = '__all__'

class PrdAlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = prd_Almacen
        fields = '__all__'

class PrdContactoProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = prd_contacto_proveedor
        fields = '__all__'

class PrdCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = prd_categorias
        fields = '__all__'

class PrdProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = prd_producto
        fields = '__all__'

class PrdLotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = prd_lotes
        fields = '__all__'

class PrdProductoCatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = prd_producto_catalogo
        fields = '__all__'

class PdClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = pd_clientes
        fields = '__all__'

class PdPedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = pd_pedidos
        fields = '__all__'

class PedDetallesPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ped_detalles_pedido
        fields = '__all__'

class EnvVehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_vehiculos
        fields = '__all__'

class EnvRutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_rutas
        fields = '__all__'

class EnvTipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_tipo_vehiculo
        fields = '__all__'

class EnvConductoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_conductores
        fields = '__all__'

class EnvConductoresVehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_conductores_vehiculos
        fields = '__all__'

class EnvEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_envio
        fields = '__all__'

class EnvEstadoEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_estado_envio
        fields = '__all__'

class EnvHistorialEnviosSerializer(serializers.ModelSerializer):
    class Meta:
        model = env_historial_envios
        fields = '__all__'