from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),


    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),


    #CRUD AREAS

    path('dashboard-area', views.dashboard_area, name="dashboard-area"),
    path('create-area', views.create_area, name="create-area"),
    path('update-area/<int:pk>', views.update_area, name='update-area'),
    path('area/<int:pk>', views.singular_area, name="area"),
    path('delete-area/<int:pk>', views.delete_area, name="delete-area"),


    #CRUD CATEGORIAS

    path('dashboard-categoria', views.dashboard_categoria, name="dashboard-categoria"),
    path('create-categoria', views.create_categoria, name="create-categoria"),
    path('update-categoria/<int:pk>', views.update_categoria, name='update-categoria'),
    path('categoria/<int:pk>', views.singular_categoria, name="categoria"),
    path('delete-categoria/<int:pk>', views.delete_categoria, name="delete-categoria"),

    #CRUD CATEGORIAS PADRES

    path('dashboard-categoriapadre', views.dashboard_categoriapadre, name="dashboard-categoriapadre"),
    path('create-categoriapadre', views.create_categoriapadre, name="create-categoriapadre"),
    path('update-categoriapadre/<int:pk>', views.update_categoriapadre, name='update-categoriapadre'),
    path('categoriapadre/<int:pk>', views.singular_categoriapadre, name="categoriapadre"),
    path('delete-categoriapadre/<int:pk>', views.delete_categoriapadre, name="delete-categoriapadre"),

    #CRUD MARCA

    path('dashboard-marca', views.dashboard_marca, name="dashboard-marca"),
    path('create-marca', views.create_marca, name="create-marca"),
    path('update-marca/<int:pk>', views.update_marca, name='update-marca'),
    path('marca/<int:pk>', views.singular_marca, name="marca"),
    path('delete-marca/<int:pk>', views.delete_marca, name="delete-marca"),


    #CRUD UNIDAD MEDIDA

    path('dashboard-unidadmedida', views.dashboard_unidadmedida, name="dashboard-unidadmedida"),
    path('create-unidadmedida', views.create_unidadmedida, name="create-unidadmedida"),
    path('update-unidadmedida/<int:pk>', views.update_unidadmedida, name='update-unidadmedida'),
    path('unidadmedida/<int:pk>', views.singular_unidadmedida, name="unidadmedida"),
    path('delete-unidadmedida/<int:pk>', views.delete_unidadmedida, name="delete-unidadmedida"),

    #CRUD PRODUCTO

    path('dashboard-producto', views.dashboard_producto, name="dashboard-producto"),
    path('create-producto', views.create_producto, name="create-producto"),
    path('update-producto/<int:pk>', views.update_producto, name='update-producto'),
    path('producto/<int:pk>', views.singular_producto, name="producto"),
    path('delete-producto/<int:pk>', views.delete_producto, name="delete-producto"),


    #CRUD PRODUCTO CATEGORIA

    path('dashboard-productocategoria', views.dashboard_productocategoria, name="dashboard-productocategoria"),
    path('create-productocategoria', views.create_productocategoria, name="create-productocategoria"),
    path('update-productocategoria/<int:pk>', views.update_productocategoria, name='update-productocategoria'),
    path('productocategoria/<int:pk>', views.singular_productocategoria, name="productocategoria"),
    path('delete-productocategoria/<int:pk>', views.delete_productocategoria, name="delete-productocategoria"),


    # CRUD PRODUCTO PRECIO

    path('dashboard-productoprecio', views.dashboard_productoprecio, name="dashboard-productoprecio"),
    path('create-productoprecio', views.create_productoprecio, name="create-productoprecio"),
    path('update-productoprecio/<int:pk>', views.update_productoprecio, name='update-productoprecio'),
    path('productoprecio/<int:pk>', views.singular_productoprecio, name="productoprecio"),
    path('delete-productoprecio/<int:pk>', views.delete_productoprecio, name="delete-productoprecio"),


    #CRUD TIPO DOCUMENTO

    path('dashboard-tipodocumento', views.dashboard_tipodocumento, name="dashboard-tipodocumento"),
    path('create-tipodocumento', views.create_tipodocumento, name="create-tipodocumento"),
    path('update-tipodocumento/<int:pk>', views.update_tipodocumento, name='update-tipodocumento'),
    path('tipodocumento/<int:pk>', views.singular_tipodocumento, name="tipodocumento"),
    path('delete-tipodocumento/<int:pk>', views.delete_tipodocumento, name="delete-tipodocumento"),


   # CRUD PERSONA

    path('dashboard-persona', views.dashboard_persona, name="dashboard-persona"),
    path('create-persona', views.create_persona, name="create-persona"),
    path('update-persona/<int:pk>', views.update_persona, name='update-persona'),
    path('persona/<int:pk>', views.singular_persona, name="persona"),
    path('delete-persona/<int:pk>', views.delete_persona, name="delete-persona"),




   # CRUD OPERADOR

    path('dashboard-operador', views.dashboard_operador, name="dashboard-operador"),
    path('create-operador', views.create_operador, name="create-operador"),
    path('update-operador/<int:pk>', views.update_operador, name='update-operador'),
    path('operador/<int:pk>', views.singular_operador, name="operador"),
    path('delete-operador/<int:pk>', views.delete_operador, name="delete-operador"),




    

    #CRUD RECORDS

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),
    
    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

]







