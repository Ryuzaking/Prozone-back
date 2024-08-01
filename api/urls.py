from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'api'

urlpatterns = [
    path('v1/api/employees/', views.EmployeeList.as_view(), name='employees'),
    path('v1/api/user/', views.UserList.as_view(), name='user'),
    path('v1/api/employees/register/', views.EmployeeRegister.as_view(), name='employee-register'),
    path('v1/api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/api/col_departamento/', views.ColDepartamentoList.as_view(), name='col_departamento-list'),
    path('v1/api/col_departamento/<int:pk>/', views.ColDepartamentoDetail.as_view(), name='col_departamento-detail'),
    path('v1/api/col_roles/', views.ColRolesList.as_view(), name='col_roles-list'),
    path('v1/api/col_roles/<int:pk>/', views.ColRolesDetail.as_view(), name='col_roles-detail'),
    path('v1/api/prd_producto/', views.PrdProductoList.as_view(), name='prd_Producto-list'),
    path('v1/api/prd_producto/<int:pk>/', views.PrdProductoDetail.as_view(), name='prd_Producto-detail'),
    path('v1/api/prd_lotes/', views.PrdLotesList.as_view(), name='prd_Lotes'),
    path('v1/api/prd_lotes/<int:pk>/', views.PrdLotesDetail.as_view(), name='prd_Lotes-detail'),
    path('v1/api/prd_almacen/', views.PrdAlmacenList.as_view(), name='prd_almacen_list'),
    path('v1/api/prd_almacen/<int:pk>/', views.PrdAlmacenDetail.as_view(), name='prd_almacen_detail'),
    path('v1/api/prd_contacto_proveedor/', views.PrdContactoProveedorList.as_view(), name='prd_contacto_proveedor_list'),
    path('v1/api/prd_contacto_proveedor/<int:pk>/', views.PrdContactoProveedorDetail.as_view(), name='prd_contacto_proveedor_detail'),
    path('v1/api/prd_categorias/', views.PrdCategoriasList.as_view(), name='prd_categorias_list'),
    path('v1/api/prd_categorias/<int:pk>/', views.PrdCategoriasDetail.as_view(), name='prd_categorias_detail'),
    path('v1/api/clientes/', views.PdClientesList.as_view(), name='pd_clientes-list'),
    path('v1/api/clientes/<int:pk>/', views.PdClientesDetail.as_view(), name='pd_clientes-detail'),
    path('v1/api/pedidos/', views.PdPedidosList.as_view(), name='pd_pedidos-list'),
    path('v1/api/pedidos/<int:pk>/', views.PdPedidosDetail.as_view(), name='pd_pedidos-detail'),
    path('v1/api/detalles_pedido/', views.PedDetallesPedidoList.as_view(), name='ped_detalles_pedido-list'),
    path('v1/api/detalles_pedido/<int:pk>/', views.PedDetallesPedidoDetail.as_view(), name='ped_detalles_pedido-detail'),
    path('v1/api/vehiculos/', views.EnvVehiculosList.as_view(), name='env_vehiculos-list'),
    path('v1/api/vehiculos/<int:pk>/', views.EnvVehiculosDetail.as_view(), name='env_vehiculos-detail'),
    path('v1/api/rutas/', views.EnvRutasList.as_view(), name='env_rutas-list'),
    path('v1/api/rutas/<int:pk>/', views.EnvRutasDetail.as_view(), name='env_rutas-detail'),
    path('v1/api/tipo_vehiculo/', views.EnvTipoVehiculoList.as_view(), name='env_tipo_vehiculo-list'),
    path('v1/api/tipo_vehiculo/<int:pk>/', views.EnvTipoVehiculoDetail.as_view(), name='env_tipo_vehiculo-detail'),
    path('v1/api/conductores/', views.EnvConductoresList.as_view(), name='env_conductores-list'),
    path('v1/api/conductores/<int:pk>/', views.EnvConductoresDetail.as_view(), name='env_conductores-detail'),
    path('v1/api/conductores_vehiculos/', views.EnvConductoresVehiculosList.as_view(), name='env_conductores_vehiculos-list'),
    path('v1/api/conductores_vehiculos/<int:pk>/', views.EnvConductoresVehiculosDetail.as_view(), name='env_conductores_vehiculos-detail'),
    path('v1/api/envio/', views.EnvEnvioList.as_view(), name='env_envio-list'),
    path('v1/api/envio/<int:pk>/', views.EnvEnvioDetail.as_view(), name='env_envio-detail'),
    path('v1/api/estado_envio/', views.EnvEstadoEnvioList.as_view(), name='env_estado_envio-list'),
    path('v1/api/estado_envio/<int:pk>/', views.EnvEstadoEnvioDetail.as_view(), name='env_estado_envio-detail'),
    path('v1/api/historial_envios/', views.EnvHistorialEnviosList.as_view(), name='env_historial_envios-list'),
    path('v1/api/historial_envios/<int:pk>/', views.EnvHistorialEnviosDetail.as_view(), name='env_historial_envios-detail'),
    path('pedidos/weekly_count/', views.PdPedidosWeeklyCountView.as_view(), name='pd_pedidos_weekly_count'),


]   