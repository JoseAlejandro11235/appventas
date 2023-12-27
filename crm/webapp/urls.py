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



    # CRUD TIPO TELEFONO
    
    path('dashboard-tipotelefono', views.dashboard_tipotelefono, name="dashboard-tipotelefono"),
    path('create-tipotelefono', views.create_tipotelefono, name="create-tipotelefono"),
    path('update-tipotelefono/<int:pk>', views.update_tipotelefono, name='update-tipotelefono'),
    path('tipotelefono/<int:pk>', views.singular_tipotelefono, name="tipotelefono"),
    path('delete-tipotelefono/<int:pk>', views.delete_tipotelefono, name="delete-tipotelefono"),


    # CRUD TELEFONO

    path('dashboard-telefono', views.dashboard_telefono, name="dashboard-telefono"),
    path('create-telefono', views.create_telefono, name="create-telefono"),
    path('update-telefono/<int:pk>', views.update_telefono, name='update-telefono'),
    path('telefono/<int:pk>', views.singular_telefono, name="telefono"),
    path('delete-telefono/<int:pk>', views.delete_telefono, name="delete-telefono"),




    # CRUD PERSONA TELEFONO

    path('dashboard-personatelefono', views.dashboard_personatelefono, name="dashboard-personatelefono"),
    path('create-personatelefono', views.create_personatelefono, name="create-personatelefono"),
    path('update-personatelefono/<int:pk>', views.update_personatelefono, name='update-personatelefono'),
    path('personatelefono/<int:pk>', views.singular_personatelefono, name="personatelefono"),
    path('delete-personatelefono/<int:pk>', views.delete_personatelefono, name="delete-personatelefono"),


    # CRUD UBIGEO

    path('dashboard-ubigeo', views.dashboard_ubigeo, name="dashboard-ubigeo"),
    path('create-ubigeo', views.create_ubigeo, name="create-ubigeo"),
    path('update-ubigeo/<int:pk>', views.update_ubigeo, name='update-ubigeo'),
    path('ubigeo/<int:pk>', views.singular_ubigeo, name="ubigeo"),
    path('delete-ubigeo/<int:pk>', views.delete_ubigeo, name="delete-ubigeo"),


    # CRUD TIPO VIA

    path('dashboard-tipovia', views.dashboard_tipovia, name="dashboard-tipovia"),
    path('create-tipovia', views.create_tipovia, name="create-tipovia"),
    path('update-tipovia/<int:pk>', views.update_tipovia, name='update-tipovia'),
    path('tipovia/<int:pk>', views.singular_tipovia, name="tipovia"),
    path('delete-tipovia/<int:pk>', views.delete_tipovia, name="delete-tipovia"),



    # CRUD TIPO ZONA

    path('dashboard-tipozona', views.dashboard_tipozona, name="dashboard-tipozona"),
    path('create-tipozona', views.create_tipozona, name="create-tipozona"),
    path('update-tipozona/<int:pk>', views.update_tipozona, name='update-tipozona'),
    path('tipozona/<int:pk>', views.singular_tipozona, name="tipozona"),
    path('delete-tipozona/<int:pk>', views.delete_tipozona, name="delete-tipozona"),


    # CRUD DIRECCION

    path('dashboard-direccion', views.dashboard_direccion, name="dashboard-direccion"),
    path('create-direccion', views.create_direccion, name="create-direccion"),
    path('update-direccion/<int:pk>', views.update_direccion, name='update-direccion'),
    path('direccion/<int:pk>', views.singular_direccion, name="direccion"),
    path('delete-direccion/<int:pk>', views.delete_direccion, name="delete-direccion"),



    #CRUD TIPO DIRECCION

    path('dashboard-tipodireccion', views.dashboard_tipodireccion, name="dashboard-tipodireccion"),
    path('create-tipodireccion', views.create_tipodireccion, name="create-tipodireccion"),
    path('update-tipodireccion/<int:pk>', views.update_tipodireccion, name='update-tipodireccion'),
    path('tipodireccion/<int:pk>', views.singular_tipodireccion, name="tipodireccion"),
    path('delete-tipodireccion/<int:pk>', views.delete_tipodireccion, name="delete-tipodireccion"),


    # CRUD PERSONA DIRECCION

    path('dashboard-personadireccion', views.dashboard_personadireccion, name="dashboard-personadireccion"),
    path('create-personadireccion', views.create_personadireccion, name="create-personadireccion"),
    path('update-personadireccion/<int:pk>', views.update_personadireccion, name='update-personadireccion'),
    path('personadireccion/<int:pk>', views.singular_personadireccion, name="personadireccion"),
    path('delete-personadireccion/<int:pk>', views.delete_personadireccion, name="delete-personadireccion"),



    #CRUD PERSONA JURIDICA

    path('dashboard-personajuridica', views.dashboard_personajuridica, name="dashboard-personajuridica"),
    path('create-personajuridica', views.create_personajuridica, name="create-personajuridica"),
    path('update-personajuridica/<int:pk>', views.update_personajuridica, name='update-personajuridica'),
    path('personajuridica/<int:pk>', views.singular_personajuridica, name="personajuridica"),
    path('delete-personajuridica/<int:pk>', views.delete_personajuridica, name="delete-personajuridica"),


    #CRUD SEXO

    path('dashboard-sexo', views.dashboard_sexo, name="dashboard-sexo"),
    path('create-sexo', views.create_sexo, name="create-sexo"),
    path('update-sexo/<int:pk>', views.update_sexo, name='update-sexo'),
    path('sexo/<int:pk>', views.singular_sexo, name="sexo"),
    path('delete-sexo/<int:pk>', views.delete_sexo, name="delete-sexo"),




    #CRUD NACIONALIDAD

    path('dashboard-nacionalidad', views.dashboard_nacionalidad, name="dashboard-nacionalidad"),
    path('create-nacionalidad', views.create_nacionalidad, name="create-nacionalidad"),
    path('update-nacionalidad/<int:pk>', views.update_nacionalidad, name='update-nacionalidad'),
    path('nacionalidad/<int:pk>', views.singular_nacionalidad, name="nacionalidad"),
    path('delete-nacionalidad/<int:pk>', views.delete_nacionalidad, name="delete-nacionalidad"),


    # CRUD PERSONA NATURAL

    path('dashboard-personanatural', views.dashboard_personanatural, name="dashboard-personanatural"),
    path('create-personanatural', views.create_personanatural, name="create-personanatural"),
    path('update-personanatural/<int:pk>', views.update_personanatural, name='update-personanatural'),
    path('personanatural/<int:pk>', views.singular_personanatural, name="personanatural"),
    path('delete-personanatural/<int:pk>', views.delete_personanatural, name="delete-personanatural"),



    #CRUD SURCURSAL

    path('dashboard-sucursal', views.dashboard_sucursal, name="dashboard-sucursal"),
    path('create-sucursal', views.create_sucursal, name="create-sucursal"),
    path('update-sucursal/<int:pk>', views.update_sucursal, name='update-sucursal'),
    path('sucursal/<int:pk>', views.singular_sucursal, name="sucursal"),
    path('delete-sucursal/<int:pk>', views.delete_sucursal, name="delete-sucursal"),



    #CRUD CARGO

    path('dashboard-cargo', views.dashboard_cargo, name="dashboard-cargo"),
    path('create-cargo', views.create_cargo, name="create-cargo"),
    path('update-cargo/<int:pk>', views.update_cargo, name='update-cargo'),
    path('cargo/<int:pk>', views.singular_cargo, name="cargo"),
    path('delete-cargo/<int:pk>', views.delete_cargo, name="delete-cargo"),

    
    #CRUD ROL

    path('dashboard-rol', views.dashboard_rol, name="dashboard-rol"),
    path('create-rol', views.create_rol, name="create-rol"),
    path('update-rol/<int:pk>', views.update_rol, name='update-rol'),
    path('rol/<int:pk>', views.singular_rol, name="rol"),
    path('delete-rol/<int:pk>', views.delete_rol, name="delete-rol"),


    #CRUD EMPLEADO

    path('dashboard-empleado', views.dashboard_empleado, name="dashboard-empleado"),
    path('create-empleado', views.create_empleado, name="create-empleado"),
    path('update-empleado/<int:pk>', views.update_empleado, name='update-empleado'),
    path('empleado/<int:pk>', views.singular_empleado, name="empleado"),
    path('delete-empleado/<int:pk>', views.delete_empleado, name="delete-empleado"),



    #CRUD TIPO CLIENTE

    path('dashboard-tipocliente', views.dashboard_tipocliente, name="dashboard-tipocliente"),
    path('create-tipocliente', views.create_tipocliente, name="create-tipocliente"),
    path('update-tipocliente/<int:pk>', views.update_tipocliente, name='update-tipocliente'),
    path('tipocliente/<int:pk>', views.singular_tipocliente, name="tipocliente"),
    path('delete-tipocliente/<int:pk>', views.delete_tipocliente, name="delete-tipocliente"),


    #CRUD CLIENTE

    path('dashboard-cliente', views.dashboard_cliente, name="dashboard-cliente"),
    path('create-cliente', views.create_cliente, name="create-cliente"),
    path('update-cliente/<int:pk>', views.update_cliente, name='update-cliente'),
    path('cliente/<int:pk>', views.singular_cliente, name="cliente"),
    path('delete-cliente/<int:pk>', views.delete_cliente, name="delete-cliente"),


    # CRUD PROVEEDOR

    path('dashboard-proveedor', views.dashboard_proveedor, name="dashboard-proveedor"),
    path('create-proveedor', views.create_proveedor, name="create-proveedor"),
    path('update-proveedor/<int:pk>', views.update_proveedor, name='update-proveedor'),
    path('proveedor/<int:pk>', views.singular_proveedor, name="proveedor"),
    path('delete-proveedor/<int:pk>', views.delete_proveedor, name="delete-proveedor"),



    # CRUD VENTA

    path('dashboard-venta', views.dashboard_venta, name="dashboard-venta"),
    path('create-venta', views.create_venta, name="create-venta"),
    path('update-venta/<int:pk>', views.update_venta, name='update-venta'),
    path('venta/<int:pk>', views.singular_venta, name="venta"),
    path('delete-venta/<int:pk>', views.delete_venta, name="delete-venta"),


    # CRUD DETALLE VENTA

    path('dashboard-detalleventa', views.dashboard_detalleventa, name="dashboard-detalleventa"),
    path('create-detalleventa', views.create_detalleventa, name="create-detalleventa"),
    path('update-detalleventa/<int:pk>', views.update_detalleventa, name='update-detalleventa'),
    path('detalleventa/<int:pk>', views.singular_detalleventa, name="detalleventa"),
    path('delete-detalleventa/<int:pk>', views.delete_detalleventa, name="delete-detalleventa"),


    # CRUD TIPO COMPROBANTE

    path('dashboard-tipocomprobante', views.dashboard_tipocomprobante, name="dashboard-tipocomprobante"),
    path('create-tipocomprobante', views.create_tipocomprobante, name="create-tipocomprobante"),
    path('update-tipocomprobante/<int:pk>', views.update_tipocomprobante, name='update-tipocomprobante'),
    path('tipocomprobante/<int:pk>', views.singular_tipocomprobante, name="tipocomprobante"),
    path('delete-tipocomprobante/<int:pk>', views.delete_tipocomprobante, name="delete-tipocomprobante"),


    # CRUD SUCURSAL SERIE

    path('dashboard-sucursalserie', views.dashboard_sucursalserie, name="dashboard-sucursalserie"),
    path('create-sucursalserie', views.create_sucursalserie, name="create-sucursalserie"),
    path('update-sucursalserie/<str:pk>', views.update_sucursalserie, name='update-sucursalserie'),
    path('sucursalserie/<str:pk>', views.singular_sucursalserie, name="sucursalserie"),
    path('delete-sucursalserie/<str:pk>', views.delete_sucursalserie, name="delete-sucursalserie"),


    # CRUD COMPROBANTE VENTA

    path('dashboard-comprobanteventa', views.dashboard_comprobanteventa, name="dashboard-comprobanteventa"),
    path('create-comprobanteventa', views.create_comprobanteventa, name="create-comprobanteventa"),
    path('update-comprobanteventa/<int:pk>', views.update_comprobanteventa, name='update-comprobanteventa'),
    path('comprobanteventa/<int:pk>', views.singular_comprobanteventa, name="comprobanteventa"),
    path('delete-comprobanteventa/<int:pk>', views.delete_comprobanteventa, name="delete-comprobanteventa"),


    # CRUD COMPRA

    path('dashboard-compra', views.dashboard_compra, name="dashboard-compra"),
    path('create-compra', views.create_compra, name="create-compra"),
    path('update-compra/<int:pk>', views.update_compra, name='update-compra'),
    path('compra/<int:pk>', views.singular_compra, name="compra"),
    path('delete-compra/<int:pk>', views.delete_compra, name="delete-compra"),


    # CRUD DETALLE COMPRA

    path('dashboard-detallecompra', views.dashboard_detallecompra, name="dashboard-detallecompra"),
    path('create-detallecompra', views.create_detallecompra, name="create-detallecompra"),
    path('update-detallecompra/<int:pk>', views.update_detallecompra, name='update-detallecompra'),
    path('detallecompra/<int:pk>', views.singular_detallecompra, name="detallecompra"),
    path('delete-detallecompra/<int:pk>', views.delete_detallecompra, name="delete-detallecompra"),


    # CRUD OFICIO

    path('dashboard-oficio', views.dashboard_oficio, name="dashboard-oficio"),
    path('create-oficio', views.create_oficio, name="create-oficio"),
    path('update-oficio/<int:pk>', views.update_oficio, name='update-oficio'),
    path('oficio/<int:pk>', views.singular_oficio, name="oficio"),
    path('delete-oficio/<int:pk>', views.delete_oficio, name="delete-oficio"),
    

    # CRUD PERSONA OFICIO

    path('dashboard-personaoficio', views.dashboard_personaoficio, name="dashboard-personaoficio"),
    path('create-personaoficio', views.create_personaoficio, name="create-personaoficio"),
    path('update-personaoficio/<int:pk>', views.update_personaoficio, name='update-personaoficio'),
    path('personaoficio/<int:pk>', views.singular_personaoficio, name="personaoficio"),
    path('delete-personaoficio/<int:pk>', views.delete_personaoficio, name="delete-personaoficio"),







        

    #CRUD RECORDS

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),
    
    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

]







