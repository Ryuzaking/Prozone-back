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
]   