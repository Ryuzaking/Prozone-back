# vistas.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from backProzone.models import Employee, Profile
from django.contrib.auth.models import User
from .serializer import EmployeeSerializer, ProfileSerializer, UserSerializer, CustomTokenObtainPairSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
import logging

from backProzone.models import (
    col_departamento, col_roles, prd_Almacen, prd_contacto_proveedor,
    prd_categorias, prd_producto, prd_lotes, prd_producto_catalogo, pd_clientes, 
    pd_pedidos, ped_detalles_pedido, env_vehiculos, env_rutas, env_tipo_vehiculo,
    env_conductores, env_conductores_vehiculos, env_envio, env_estado_envio, env_historial_envios
)
from .serializer import (
    ColDepartamentoSerializer, ColRolesSerializer, PrdAlmacenSerializer, PrdContactoProveedorSerializer,
    PrdCategoriasSerializer, PrdProductoSerializer, PrdLotesSerializer, PrdProductoCatalogoSerializer,
    PdClientesSerializer, PdPedidosSerializer, PedDetallesPedidoSerializer, EnvVehiculosSerializer,
    EnvRutasSerializer, EnvTipoVehiculoSerializer, EnvConductoresSerializer, EnvConductoresVehiculosSerializer,
    EnvEnvioSerializer, EnvEstadoEnvioSerializer, EnvHistorialEnviosSerializer
)

logger = logging.getLogger(__name__)

# Create your views here.

class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProfileList(APIView):
    serializer_class = ProfileSerializer

class UserList(APIView):
    def get(self, request):
        queryset = User.objects.all()
        data = UserSerializer(queryset, many=True).data
        return Response(data)

        
class EmployeeRegister(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        user_data = {
            'username': request.data.get('email', ''),
            'email': request.data.get('email', ''),
            'first_name': request.data.get('nombre', ''),
            'last_name': request.data.get('apellido', ''),
            'password': request.data.get('password', '')
        }

        user_serializer = UserSerializer(data=user_data)
        logger.debug(f"user_serializer data: {user_data}")
        if user_serializer.is_valid():
            user = user_serializer.save()
            employee_data = request.data.copy()
            employee_data['user'] = user.id
            employee_serializer = self.get_serializer(data=employee_data)
            logger.debug(f"employee_serializer data: {employee_data}")
            if employee_serializer.is_valid():
                self.perform_create(employee_serializer)
                headers = self.get_success_headers(employee_serializer.data)
                return Response(employee_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                logger.error(f"employee_serializer errors: {employee_serializer.errors}")
                return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.error(f"user_serializer errors: {user_serializer.errors}")
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ColDepartamentoList(generics.ListCreateAPIView):
    queryset = col_departamento.objects.all()
    serializer_class = ColDepartamentoSerializer

class ColDepartamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = col_departamento.objects.all()
    serializer_class = ColDepartamentoSerializer

class ColRolesList(generics.ListCreateAPIView):
    queryset = col_roles.objects.all()
    serializer_class = ColRolesSerializer

class ColRolesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = col_roles.objects.all()
    serializer_class = ColRolesSerializer

class PrdAlmacenList(generics.ListCreateAPIView):
    queryset = prd_Almacen.objects.all()
    serializer_class = PrdAlmacenSerializer

class PrdAlmacenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = prd_Almacen.objects.all()
    serializer_class = PrdAlmacenSerializer

class PrdContactoProveedorList(generics.ListCreateAPIView):
    queryset = prd_contacto_proveedor.objects.all()
    serializer_class = PrdContactoProveedorSerializer

class PrdContactoProveedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = prd_contacto_proveedor.objects.all()
    serializer_class = PrdContactoProveedorSerializer

class PrdCategoriasList(generics.ListCreateAPIView):
    queryset = prd_categorias.objects.all()
    serializer_class = PrdCategoriasSerializer

class PrdCategoriasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = prd_categorias.objects.all()
    serializer_class = PrdCategoriasSerializer

class PrdProductoList(generics.ListCreateAPIView):
    queryset = prd_producto.objects.all()
    serializer_class = PrdProductoSerializer

class PrdProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = prd_producto.objects.all()
    serializer_class = PrdProductoSerializer

class PrdLotesList(generics.ListCreateAPIView):
    queryset = prd_lotes.objects.all()
    serializer_class = PrdLotesSerializer

class PrdLotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = prd_lotes.objects.all()
    serializer_class = PrdLotesSerializer

class PrdProductoCatalogoList(generics.ListCreateAPIView):
    queryset = prd_producto_catalogo.objects.all()
    serializer_class = PrdProductoCatalogoSerializer

class PrdProductoCatalogoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = prd_producto_catalogo.objects.all()
    serializer_class = PrdProductoCatalogoSerializer

class PdClientesList(generics.ListCreateAPIView):
    queryset = pd_clientes.objects.all()
    serializer_class = PdClientesSerializer

class PdClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = pd_clientes.objects.all()
    serializer_class = PdClientesSerializer

class PdPedidosList(generics.ListCreateAPIView):
    queryset = pd_pedidos.objects.all()
    serializer_class = PdPedidosSerializer

class PdPedidosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = pd_pedidos.objects.all()
    serializer_class = PdPedidosSerializer

class PedDetallesPedidoList(generics.ListCreateAPIView):
    queryset = ped_detalles_pedido.objects.all()
    serializer_class = PedDetallesPedidoSerializer

class PedDetallesPedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ped_detalles_pedido.objects.all()
    serializer_class = PedDetallesPedidoSerializer

class EnvVehiculosList(generics.ListCreateAPIView):
    queryset = env_vehiculos.objects.all()
    serializer_class = EnvVehiculosSerializer

class EnvVehiculosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = env_vehiculos.objects.all()
    serializer_class = EnvVehiculosSerializer

class EnvRutasList(generics.ListCreateAPIView):
    queryset = env_rutas.objects.all()
    serializer_class = EnvRutasSerializer

class EnvRutasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = env_rutas.objects.all()
    serializer_class = EnvRutasSerializer

class EnvTipoVehiculoList(generics.ListCreateAPIView):
    queryset = env_tipo_vehiculo.objects.all()
    serializer_class = EnvTipoVehiculoSerializer

class EnvTipoVehiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = env_tipo_vehiculo.objects.all()
    serializer_class = EnvTipoVehiculoSerializer

class EnvConductoresList(generics.ListCreateAPIView):
    queryset = env_conductores.objects.all()
    serializer_class = EnvConductoresSerializer

class EnvConductoresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = env_conductores.objects.all()
    serializer_class = EnvConductoresSerializer

class EnvConductoresVehiculosList(generics.ListCreateAPIView):
    queryset = env_conductores_vehiculos.objects.all()
    serializer_class = EnvConductoresVehiculosSerializer

class EnvConductoresVehiculosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = env_conductores_vehiculos.objects.all()
    serializer_class = EnvConductoresVehiculosSerializer

class EnvEnvioList(generics.ListCreateAPIView):
    queryset = env_envio.objects.all()
    serializer_class = EnvEnvioSerializer

class EnvEnvioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = env_envio.objects.all()
    serializer_class = EnvEnvioSerializer

class EnvEstadoEnvioList(generics.ListCreateAPIView):
    queryset = env_estado_envio.objects.all()
    serializer_class = EnvEstadoEnvioSerializer

class EnvEstadoEnvioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = env_estado_envio.objects.all()
    serializer_class = EnvEstadoEnvioSerializer

class EnvHistorialEnviosList(generics.ListCreateAPIView):
    queryset = env_historial_envios.objects.all()
    serializer_class = EnvHistorialEnviosSerializer

class EnvHistorialEnviosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = env_historial_envios.objects.all()
    serializer_class = EnvHistorialEnviosSerializer   