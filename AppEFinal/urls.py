from django.contrib import admin
from django.urls import path
from AppEFinal import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('categorias/', views.lista_categorias, name='categorias_listado'),
    path('categorias/nuevo/', views.crear_categoria, name='categoria_nuevo'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='categoria_editar'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='categoria_eliminar'),

path('productos/', views.lista_productos, name='productos_listado'),
path('productos/nuevo/', views.crear_producto, name='producto_nuevo'),
path('productos/editar/<int:id>/', views.editar_producto, name='producto_editar'),
path('productos/eliminar/<int:id>/', views.eliminar_producto, name='producto_eliminar'),

]
