from django.shortcuts import render, redirect


from . forms import LoginForm,CreateRecordForm, UpdateRecordForm, CreateAreaForm, UpdateAreaForm, CreateCategoriaForm, UpdateCategoriaForm, CreateCategoriaPadreForm, UpdateCategoriaPadreForm, CreateMarcaForm, UpdateMarcaForm, CreateUnidadMedidaForm, UpdateUnidadMedidaForm, CreateProductoForm, UpdateProductoForm, CreateProductoCategoriaForm, UpdateProductoCategoriaForm, CreateProductoPrecioForm, UpdateProductoPrecioForm, CreateTipoDocumentoForm, UpdateTipoDocumentoForm, CreatePersonaForm, UpdatePersonaForm, CreateOperadorForm, UpdateOperadorForm, CreateTipoTelefonoForm, UpdateTipoTelefonoForm, CreateTelefonoForm, UpdateTelefonoForm, CreatePersonaTelefonoForm, UpdatePersonaTelefonoForm, CreateUbigeoForm, UpdateUbigeoForm, CreateTipoViaForm, UpdateTipoViaForm, CreateTipoZonaForm, UpdateTipoZonaForm, CreateDireccionForm, UpdateDireccionForm, CreateTipoDireccionForm, UpdateTipoDireccionForm, CreatePersonaDireccionForm, UpdatePersonaDireccionForm, CreatePersonaJuridicaForm, UpdatePersonaJuridicaForm, CreateSexoForm, UpdateSexoForm, CreateNacionalidadForm, UpdateNacionalidadForm, CreatePersonaNaturalForm, UpdatePersonaNaturalForm, CreateSucursalForm, UpdateSucursalForm, CreateCargoForm, UpdateCargoForm, CreateRolForm, UpdateRolForm, CreateEmpleadoForm, UpdateEmpleadoForm, CreateTipoClienteForm, UpdateTipoClienteForm, CreateClienteForm, UpdateClienteForm, CreateProveedorForm, UpdateProveedorForm, CreateVentaForm, UpdateVentaForm, CreateDetalleVentaForm, UpdateDetalleVentaForm, CreateTipoComprobanteForm, UpdateTipoComprobanteForm, CreateSucursalSerieForm, UpdateSucursalSerieForm, CreateComprobanteVentaForm, UpdateComprobanteVentaForm, CreateCompraForm, UpdateCompraForm, CreateDetalleCompraForm, UpdateDetalleCompraForm, CreateOficioForm, UpdateOficioForm, CreatePersonaOficioForm, UpdatePersonaOficioForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .models import Record, Area, Categoria, CategoriaPadre, Marca, UnidadMedida, Producto, ProductoCategoria, ProductoPrecio, TipoDocumento, Persona, Operador, TipoTelefono, Telefono, PersonaTelefono, Ubigeo, TipoVia, TipoZona, Direccion, TipoDireccion, PersonaDireccion, PersonaJuridica, Sexo, Nacionalidad, PersonaNatural, Sucursal, Cargo, Rol, Empleado, TipoCliente, Cliente, Proveedor, Venta, DetalleVenta, TipoComprobante, SucursalSerie, ComprobanteVenta, Compra, DetalleCompra, Oficio, PersonaOficio
from django.contrib import messages



#Homepage

def home(request):

    return render(request, 'webapp/index.html')



# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form =  LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)

# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request,'webapp/dashboard.html', context=context)



# - Create a record

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")
        
    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)


# - Update a record
@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form': form}

    return render(request, 'webapp/update-record.html',context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context=context)


# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")

# - Dashboard area

@login_required(login_url='my-login')
def dashboard_area(request):

    my_areas = Area.objects.all()

    context = {'areas': my_areas}

    return render(request,'webapp/dashboard-area.html', context=context)

# - Create an area

@login_required(login_url='my-login')
def create_area(request):

    form = CreateAreaForm()

    if request.method == "POST":
        form = CreateAreaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your area was created!")

            return redirect("dashboard-area")
        
    context = {'form': form}

    return render(request, 'webapp/create-area.html', context=context)

# - Update an area
@login_required(login_url='my-login')
def update_area(request, pk):

    area = Area.objects.get(id=pk)

    form = UpdateAreaForm(instance=area)

    if request.method == 'POST':

        form = UpdateAreaForm(request.POST, instance=area)

        if form.is_valid():

            form.save()

            messages.success(request, "Your area was updated!")

            return redirect("dashboard-area")
        
    context = {'form': form}

    return render(request, 'webapp/update-area.html',context=context)



# - Read / View a singular area

@login_required(login_url='my-login')
def singular_area(request, pk):

    all_areas = Area.objects.get(id=pk)

    context = {'area':all_areas}

    return render(request, 'webapp/view-area.html', context=context)


# - Delete an area

@login_required(login_url='my-login')
def delete_area(request, pk):
    area = Area.objects.get(id=pk)

    area.delete()

    messages.success(request, "Your area was deleted!")

    return redirect("dashboard-area")


# - Dashboard categoria

@login_required(login_url='my-login')
def dashboard_categoria(request):

    my_categorias = Categoria.objects.all()

    context = {'categorias': my_categorias}

    return render(request,'webapp/dashboard-categoria.html', context=context)

# - Create a categoria

@login_required(login_url='my-login')
def create_categoria(request):

    form = CreateCategoriaForm()

    if request.method == "POST":
        form = CreateCategoriaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your categoria was created!")

            return redirect("dashboard-categoria")
        
    context = {'form': form}

    return render(request, 'webapp/create-categoria.html', context=context)

# - Update a categoria
@login_required(login_url='my-login')
def update_categoria(request, pk):

    area = Categoria.objects.get(id=pk)

    form = UpdateCategoriaForm(instance=area)

    if request.method == 'POST':

        form = UpdateCategoriaForm(request.POST, instance=area)

        if form.is_valid():

            form.save()

            messages.success(request, "Your categoria was updated!")

            return redirect("dashboard-categoria")
        
    context = {'form': form}

    return render(request, 'webapp/update-categoria.html',context=context)



# - Read / View a singular categoria

@login_required(login_url='my-login')
def singular_categoria(request, pk):

    all_categorias = Categoria.objects.get(id=pk)

    context = {'categoria':all_categorias}

    return render(request, 'webapp/view-categoria.html', context=context)


# - Delete a categoria

@login_required(login_url='my-login')
def delete_categoria(request, pk):
    categoria = Categoria.objects.get(id=pk)

    categoria.delete()

    messages.success(request, "Your categoria was deleted!")

    return redirect("dashboard-categoria")


# - Dashboard categoria padre

@login_required(login_url='my-login')
def dashboard_categoriapadre(request):

    my_categorias_padres = CategoriaPadre.objects.all()

    context = {'categoriaspadres': my_categorias_padres}

    return render(request,'webapp/dashboard-categoriapadre.html', context=context)

# - Create a categoria-padre

@login_required(login_url='my-login')
def create_categoriapadre(request):

    form = CreateCategoriaPadreForm()

    if request.method == "POST":
        form = CreateCategoriaPadreForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your categoria padre was created!")

            return redirect("dashboard-categoriapadre")
        
    context = {'form': form}

    return render(request, 'webapp/create-categoriapadre.html', context=context)

# - Update a categoria padre
@login_required(login_url='my-login')
def update_categoriapadre(request, pk):

    categoriapadre = CategoriaPadre.objects.get(id=pk)

    form = UpdateCategoriaPadreForm(instance=categoriapadre)

    if request.method == 'POST':

        form = UpdateCategoriaPadreForm(request.POST, instance=categoriapadre)

        if form.is_valid():

            form.save()

            messages.success(request, "Your categoria padre was updated!")

            return redirect("dashboard-categoriapadre")
        
    context = {'form': form}

    return render(request, 'webapp/update-categoriapadre.html',context=context)



# - Read / View a singular categoria padre

@login_required(login_url='my-login')
def singular_categoriapadre(request, pk):

    all_categorias_padres = CategoriaPadre.objects.get(id=pk)

    context = {'categoriapadre':all_categorias_padres}

    return render(request, 'webapp/view-categoriapadre.html', context=context)


# - Delete a categoria

@login_required(login_url='my-login')
def delete_categoriapadre(request, pk):
    categoriapadre = CategoriaPadre.objects.get(id=pk)

    categoriapadre.delete()

    messages.success(request, "Your categoria padre was deleted!")

    return redirect("dashboard-categoriapadre")

# - Dashboard marca

@login_required(login_url='my-login')
def dashboard_marca(request):

    my_marcas = Marca.objects.all()

    context = {'marcas': my_marcas}

    return render(request,'webapp/dashboard-marca.html', context=context)

# - Create a marca

@login_required(login_url='my-login')
def create_marca(request):

    form = CreateMarcaForm()

    if request.method == "POST":
        form = CreateMarcaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your marca was created!")

            return redirect("dashboard-marca")
        
    context = {'form': form}

    return render(request, 'webapp/create-marca.html', context=context)

# - Update a marca
@login_required(login_url='my-login')
def update_marca(request, pk):

    marca = Marca.objects.get(id=pk)

    form = UpdateMarcaForm(instance=marca)

    if request.method == 'POST':

        form = UpdateMarcaForm(request.POST, instance=marca)

        if form.is_valid():

            form.save()

            messages.success(request, "Your marca was updated!")

            return redirect("dashboard-marca")
        
    context = {'form': form}

    return render(request, 'webapp/update-marca.html',context=context)



# - Read / View a singular marca

@login_required(login_url='my-login')
def singular_marca(request, pk):

    all_marcas = Marca.objects.get(id=pk)

    context = {'marca':all_marcas}

    return render(request, 'webapp/view-marca.html', context=context)


# - Delete a marca

@login_required(login_url='my-login')
def delete_marca(request, pk):
    marca = Marca.objects.get(id=pk)

    marca.delete()

    messages.success(request, "Your marca was deleted!")

    return redirect("dashboard-marca")



# - Dashboard unidad medida

@login_required(login_url='my-login')
def dashboard_unidadmedida(request):

    my_unidadesmedidas = UnidadMedida.objects.all()

    context = {'unidadesmedidas': my_unidadesmedidas}

    return render(request,'webapp/dashboard-unidadmedida.html', context=context)

# - Create a unidad medida

@login_required(login_url='my-login')
def create_unidadmedida(request):

    form = CreateUnidadMedidaForm()

    if request.method == "POST":
        form = CreateUnidadMedidaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your Unidad Medida was created!")

            return redirect("dashboard-unidadmedida")
        
    context = {'form': form}

    return render(request, 'webapp/create-unidadmedida.html', context=context)

# - Update a unidad medida
@login_required(login_url='my-login')
def update_unidadmedida(request, pk):

    unidadmedida = UnidadMedida.objects.get(id=pk)

    form = UpdateUnidadMedidaForm(instance=unidadmedida)

    if request.method == 'POST':

        form = UpdateUnidadMedidaForm(request.POST, instance=unidadmedida)

        if form.is_valid():

            form.save()

            messages.success(request, "Your unidad medida was updated!")

            return redirect("dashboard-unidadmedida")
        
    context = {'form': form}

    return render(request, 'webapp/update-unidadmedida.html',context=context)



# - Read / View a singular unidad medida

@login_required(login_url='my-login')
def singular_unidadmedida(request, pk):

    all_unidadesmedidas = UnidadMedida.objects.get(id=pk)

    context = {'unidadmedida':all_unidadesmedidas}

    return render(request, 'webapp/view-unidadmedida.html', context=context)


# - Delete a unidad medida

@login_required(login_url='my-login')
def delete_unidadmedida(request, pk):
    unidadmedida = UnidadMedida.objects.get(id=pk)

    unidadmedida.delete()

    messages.success(request, "Your unidad medida was deleted!")

    return redirect("dashboard-unidadmedida")



# - Dashboard producto

@login_required(login_url='my-login')
def dashboard_producto(request):

    my_productos = Producto.objects.all()

    context = {'productos': my_productos}

    return render(request,'webapp/dashboard-producto.html', context=context)

# - Create a producto

@login_required(login_url='my-login')
def create_producto(request):

    form = CreateProductoForm()

    if request.method == "POST":
        form = CreateProductoForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your Producto was created!")

            return redirect("dashboard-producto")
        
    context = {'form': form}

    return render(request, 'webapp/create-producto.html', context=context)

# - Update a producto
@login_required(login_url='my-login')
def update_producto(request, pk):

    producto = Producto.objects.get(id=pk)

    form = UpdateProductoForm(instance=producto)

    if request.method == 'POST':

        form = UpdateProductoForm(request.POST, instance=producto)

        if form.is_valid():

            form.save()

            messages.success(request, "Your producto was updated!")

            return redirect("dashboard-producto")
        
    context = {'form': form}

    return render(request, 'webapp/update-producto.html',context=context)



# - Read / View a singular producto

@login_required(login_url='my-login')
def singular_producto(request, pk):

    all_productos = Producto.objects.get(id=pk)

    context = {'producto':all_productos}

    return render(request, 'webapp/view-producto.html', context=context)


# - Delete a producto

@login_required(login_url='my-login')
def delete_producto(request, pk):
    producto = Producto.objects.get(id=pk)

    producto.delete()

    messages.success(request, "Your producto was deleted!")

    return redirect("dashboard-producto")


# - Dashboard producto categoria

@login_required(login_url='my-login')
def dashboard_productocategoria(request):

    my_productoscategorias = ProductoCategoria.objects.all()

    context = {'productoscategorias': my_productoscategorias}

    return render(request, 'webapp/dashboard-productocategoria.html', context=context)

# - Create a producto categoria

@login_required(login_url='my-login')
def create_productocategoria(request):

    form = CreateProductoCategoriaForm()

    if request.method == "POST":
        form = CreateProductoCategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Producto Categoria was created!")
            return redirect("dashboard-productocategoria")
        
    context = {'form': form}

    return render(request, 'webapp/create-productocategoria.html', context=context)

# - Update a producto categoria
@login_required(login_url='my-login')
def update_productocategoria(request, pk):

    productocategoria = ProductoCategoria.objects.get(id=pk)

    form = UpdateProductoCategoriaForm(instance=productocategoria)

    if request.method == 'POST':
        form = UpdateProductoCategoriaForm(request.POST, instance=productocategoria)

        if form.is_valid():
            form.save()
            messages.success(request, "Your producto categoria was updated!")
            return redirect("dashboard-productocategoria")
        
    context = {'form': form}

    return render(request, 'webapp/update-productocategoria.html', context=context)

# - Read / View a singular producto categoria

@login_required(login_url='my-login')
def singular_productocategoria(request, pk):

    productocategoria = ProductoCategoria.objects.get(id=pk)

    context = {'productocategoria': productocategoria}

    return render(request, 'webapp/view-productocategoria.html', context=context)

# - Delete a producto categoria

@login_required(login_url='my-login')
def delete_productocategoria(request, pk):
    productocategoria = ProductoCategoria.objects.get(id=pk)
    productocategoria.delete()
    messages.success(request, "Your producto categoria was deleted!")
    return redirect("dashboard-productocategoria")


# - Dashboard producto precio

@login_required(login_url='my-login')
def dashboard_productoprecio(request):

    my_productosprecios = ProductoPrecio.objects.all()

    context = {'productosprecios': my_productosprecios}

    return render(request, 'webapp/dashboard-productoprecio.html', context=context)

# - Create a producto precio
@login_required(login_url='my-login')
def create_productoprecio(request):

    form = CreateProductoPrecioForm()

    if request.method == "POST":
        form = CreateProductoPrecioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Producto Precio was created!")
            return redirect("dashboard-productoprecio")
        
    context = {'form': form}

    return render(request, 'webapp/create-productoprecio.html', context=context)

# - Update a productoprecio
@login_required(login_url='my-login')
def update_productoprecio(request, pk):

    productoprecio = ProductoPrecio.objects.get(id=pk)

    form = UpdateProductoPrecioForm(instance=productoprecio)

    if request.method == 'POST':
        form = UpdateProductoPrecioForm(request.POST, instance=productoprecio)

        if form.is_valid():
            form.save()
            messages.success(request, "Your producto precio was updated!")
            return redirect("dashboard-productoprecio")
        
    context = {'form': form}

    return render(request, 'webapp/update-productoprecio.html', context=context)

# - Read / View a singular productoprecio

@login_required(login_url='my-login')
def singular_productoprecio(request, pk):

    productoprecio = ProductoPrecio.objects.get(id=pk)

    context = {'productoprecio': productoprecio}

    return render(request, 'webapp/view-productoprecio.html', context=context)

# - Delete a productoprecio

@login_required(login_url='my-login')
def delete_productoprecio(request, pk):
    productoprecio = ProductoPrecio.objects.get(id=pk)
    productoprecio.delete()
    messages.success(request, "Your productoprecio was deleted!")
    return redirect("dashboard-productoprecio")



# - Dashboard tipo documento

@login_required(login_url='my-login')
def dashboard_tipodocumento(request):

    my_tiposdocumentos = TipoDocumento.objects.all()

    context = {'tiposdocumentos': my_tiposdocumentos}

    return render(request, 'webapp/dashboard-tipodocumento.html', context=context)


# - Create a tipo documento
@login_required(login_url='my-login')
def create_tipodocumento(request):

    form = CreateTipoDocumentoForm()

    if request.method == "POST":
        form = CreateTipoDocumentoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Tipo Documento was created!")
            return redirect("dashboard-tipodocumento")
        
    context = {'form': form}

    return render(request, 'webapp/create-tipodocumento.html', context=context)


# - Update a tipo documento
@login_required(login_url='my-login')
def update_tipodocumento(request, pk):

    tipodocumento = TipoDocumento.objects.get(id=pk)

    form = UpdateTipoDocumentoForm(instance=tipodocumento)

    if request.method == 'POST':
        form = UpdateTipoDocumentoForm(request.POST, instance=tipodocumento)

        if form.is_valid():
            form.save()
            messages.success(request, "Your tipo documento was updated!")
            return redirect("dashboard-tipodocumento")
        
    context = {'form': form}

    return render(request, 'webapp/update-tipodocumento.html', context=context)

# - Read / View a singular tipo documento

@login_required(login_url='my-login')
def singular_tipodocumento(request, pk):

    tipodocumento = TipoDocumento.objects.get(id=pk)

    context = {'tipodocumento': tipodocumento}

    return render(request, 'webapp/view-tipodocumento.html', context=context)

# - Delete a productoprecio

@login_required(login_url='my-login')
def delete_tipodocumento(request, pk):
    tipodocumento = TipoDocumento.objects.get(id=pk)
    tipodocumento.delete()
    messages.success(request, "Your Tipo Documento was deleted!")
    return redirect("dashboard-tipodocumento")    



# - Dashboard persona
@login_required(login_url='my-login')
def dashboard_persona(request):

    personas = Persona.objects.all()

    context = {'personas': personas}

    return render(request, 'webapp/dashboard-persona.html', context=context)


# - Create a persona
@login_required(login_url='my-login')
def create_persona(request):

    form = CreatePersonaForm()

    if request.method == "POST":
        form = CreatePersonaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Persona was created!")
            return redirect("dashboard-persona")
        
    context = {'form': form}

    return render(request, 'webapp/create-persona.html', context=context)


# - Update a persona
@login_required(login_url='my-login')
def update_persona(request, pk):

    persona = Persona.objects.get(id=pk)

    form = UpdatePersonaForm(instance=persona)

    if request.method == 'POST':
        form = UpdatePersonaForm(request.POST, instance=persona)

        if form.is_valid():
            form.save()
            messages.success(request, "Your persona was updated!")
            return redirect("dashboard-persona")
        
    context = {'form': form}

    return render(request, 'webapp/update-persona.html', context=context)

# - Read / View a singular persona

@login_required(login_url='my-login')
def singular_persona(request, pk):

    persona = Persona.objects.get(id=pk)

    context = {'persona': persona}

    return render(request, 'webapp/view-persona.html', context=context)

# - Delete a persona

@login_required(login_url='my-login')
def delete_persona(request, pk):
    persona = Persona.objects.get(id=pk)
    persona.delete()
    messages.success(request, "Your Persona was deleted!")
    return redirect("dashboard-persona")  



# - Dashboard operador
@login_required(login_url='my-login')
def dashboard_operador(request):

    operadores = Operador.objects.all()

    context = {'operadores': operadores}

    return render(request, 'webapp/dashboard-operador.html', context=context)


# - Create an operador
@login_required(login_url='my-login')
def create_operador(request):

    form = CreateOperadorForm()

    if request.method == "POST":
        form = CreateOperadorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Operador was created!")
            return redirect("dashboard-operador")
        
    context = {'form': form}

    return render(request, 'webapp/create-operador.html', context=context)


# - Update an operador
@login_required(login_url='my-login')
def update_operador(request, pk):

    operador = Operador.objects.get(id=pk)

    form = UpdateOperadorForm(instance=operador)

    if request.method == 'POST':
        form = UpdateOperadorForm(request.POST, instance=operador)

        if form.is_valid():
            form.save()
            messages.success(request, "Your operador was updated!")
            return redirect("dashboard-operador")
        
    context = {'form': form}

    return render(request, 'webapp/update-operador.html', context=context)

# - Read / View a singular operador

@login_required(login_url='my-login')
def singular_operador(request, pk):

    operador = Operador.objects.get(id=pk)

    context = {'operador': operador}

    return render(request, 'webapp/view-operador.html', context=context)

# - Delete an operador

@login_required(login_url='my-login')
def delete_operador(request, pk):
    operador = Operador.objects.get(id=pk)
    operador.delete()
    messages.success(request, "Your Operador was deleted!")
    return redirect("dashboard-operador")



# - Dashboard tipotelefono
@login_required(login_url='my-login')
def dashboard_tipotelefono(request):

    tipostelefonos = TipoTelefono.objects.all()

    context = {'tipostelefonos': tipostelefonos}

    return render(request, 'webapp/dashboard-tipotelefono.html', context=context)


# - Create a tipotelefono
@login_required(login_url='my-login')
def create_tipotelefono(request):

    form = CreateTipoTelefonoForm()

    if request.method == "POST":
        form = CreateTipoTelefonoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoTelefono was created!")
            return redirect("dashboard-tipotelefono")
        
    context = {'form': form}

    return render(request, 'webapp/create-tipotelefono.html', context=context)


# - Update a tipotelefono
@login_required(login_url='my-login')
def update_tipotelefono(request, pk):

    tipotelefono = TipoTelefono.objects.get(id=pk)

    form = UpdateTipoTelefonoForm(instance=tipotelefono)

    if request.method == 'POST':
        form = UpdateTipoTelefonoForm(request.POST, instance=tipotelefono)

        if form.is_valid():
            form.save()
            messages.success(request, "Your tipo telefono was updated!")
            return redirect("dashboard-tipotelefono")
        
    context = {'form': form}

    return render(request, 'webapp/update-tipotelefono.html', context=context)

# - Read / View a singular tipotelefono

@login_required(login_url='my-login')
def singular_tipotelefono(request, pk):

    tipotelefono = TipoTelefono.objects.get(id=pk)

    context = {'tipotelefono': tipotelefono}

    return render(request, 'webapp/view-tipotelefono.html', context=context)

# - Delete a tipotelefono

@login_required(login_url='my-login')
def delete_tipotelefono(request, pk):
    tipotelefono = TipoTelefono.objects.get(id=pk)
    tipotelefono.delete()
    messages.success(request, "Your Tipo Telefono was deleted!")
    return redirect("dashboard-tipotelefono")



# - Dashboard Telefono
@login_required(login_url='my-login')
def dashboard_telefono(request):

    telefonos = Telefono.objects.all()

    context = {'telefonos': telefonos}

    return render(request, 'webapp/dashboard-telefono.html', context=context)


# - Create a Telefono
@login_required(login_url='my-login')
def create_telefono(request):

    form = CreateTelefonoForm()

    if request.method == "POST":
        form = CreateTelefonoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Telefono was created!")
            return redirect("dashboard-telefono")
        
    context = {'form': form}

    return render(request, 'webapp/create-telefono.html', context=context)


# - Update a Telefono
@login_required(login_url='my-login')
def update_telefono(request, pk):

    telefono = Telefono.objects.get(id=pk)

    form = UpdateTelefonoForm(instance=telefono)

    if request.method == 'POST':
        form = UpdateTelefonoForm(request.POST, instance=telefono)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Telefono was updated!")
            return redirect("dashboard-telefono")
        
    context = {'form': form}

    return render(request, 'webapp/update-telefono.html', context=context)

# - Read / View a singular Telefono

@login_required(login_url='my-login')
def singular_telefono(request, pk):

    telefono = Telefono.objects.get(id=pk)

    context = {'telefono': telefono}

    return render(request, 'webapp/view-telefono.html', context=context)

# - Delete a Telefono

@login_required(login_url='my-login')
def delete_telefono(request, pk):
    telefono = Telefono.objects.get(id=pk)
    telefono.delete()
    messages.success(request, "Your Telefono was deleted!")
    return redirect("dashboard-telefono")



# - Dashboard PersonaTelefono
@login_required(login_url='my-login')
def dashboard_personatelefono(request):

    personastelefonos = PersonaTelefono.objects.all()

    context = {'personastelefonos': personastelefonos}

    return render(request, 'webapp/dashboard-personatelefono.html', context=context)


# - Create a PersonaTelefono
@login_required(login_url='my-login')
def create_personatelefono(request):

    form = CreatePersonaTelefonoForm()

    if request.method == "POST":
        form = CreatePersonaTelefonoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaTelefono was created!")
            return redirect("dashboard-personatelefono")
        
    context = {'form': form}

    return render(request, 'webapp/create-personatelefono.html', context=context)


# - Update a PersonaTelefono
@login_required(login_url='my-login')
def update_personatelefono(request, pk):

    personatelefono = PersonaTelefono.objects.get(id=pk)

    form = UpdatePersonaTelefonoForm(instance=personatelefono)

    if request.method == 'POST':
        form = UpdatePersonaTelefonoForm(request.POST, instance=personatelefono)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaTelefono was updated!")
            return redirect("dashboard-personatelefono")
        
    context = {'form': form}

    return render(request, 'webapp/update-personatelefono.html', context=context)

# - Read / View a singular PersonaTelefono

@login_required(login_url='my-login')
def singular_personatelefono(request, pk):

    personatelefono = PersonaTelefono.objects.get(id=pk)

    context = {'personatelefono': personatelefono}

    return render(request, 'webapp/view-personatelefono.html', context=context)

# - Delete a PersonaTelefono

@login_required(login_url='my-login')
def delete_personatelefono(request, pk):
    personatelefono = PersonaTelefono.objects.get(id=pk)
    personatelefono.delete()
    messages.success(request, "Your PersonaTelefono was deleted!")
    return redirect("dashboard-personatelefono")


# - Dashboard Ubigeo
@login_required(login_url='my-login')
def dashboard_ubigeo(request):

    ubigeos = Ubigeo.objects.all()

    context = {'ubigeos': ubigeos}

    return render(request, 'webapp/dashboard-ubigeo.html', context=context)


# - Create an Ubigeo
@login_required(login_url='my-login')
def create_ubigeo(request):

    form = CreateUbigeoForm()

    if request.method == "POST":
        form = CreateUbigeoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Ubigeo was created!")
            return redirect("dashboard-ubigeo")
        
    context = {'form': form}

    return render(request, 'webapp/create-ubigeo.html', context=context)


# - Update an Ubigeo
@login_required(login_url='my-login')
def update_ubigeo(request, pk):

    ubigeo = Ubigeo.objects.get(ubigeo=pk)

    form = UpdateUbigeoForm(instance=ubigeo)

    if request.method == 'POST':
        form = UpdateUbigeoForm(request.POST, instance=ubigeo)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Ubigeo was updated!")
            return redirect("dashboard-ubigeo")
        
    context = {'form': form}

    return render(request, 'webapp/update-ubigeo.html', context=context)

# - Read / View a singular Ubigeo

@login_required(login_url='my-login')
def singular_ubigeo(request, pk):

    ubigeo = Ubigeo.objects.get(ubigeo=pk)

    context = {'ubigeo': ubigeo}

    return render(request, 'webapp/view-ubigeo.html', context=context)

# - Delete an Ubigeo

@login_required(login_url='my-login')
def delete_ubigeo(request, pk):
    ubigeo = Ubigeo.objects.get(ubigeo=pk)
    ubigeo.delete()
    messages.success(request, "Your Ubigeo was deleted!")
    return redirect("dashboard-ubigeo")


# - Dashboard TipoVia
@login_required(login_url='my-login')
def dashboard_tipovia(request):

    tiposvias = TipoVia.objects.all()

    context = {'tiposvias': tiposvias}

    return render(request, 'webapp/dashboard-tipovia.html', context=context)


# - Create a TipoVia
@login_required(login_url='my-login')
def create_tipovia(request):

    form = CreateTipoViaForm()

    if request.method == "POST":
        form = CreateTipoViaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoVia was created!")
            return redirect("dashboard-tipovia")
        
    context = {'form': form}

    return render(request, 'webapp/create-tipovia.html', context=context)


# - Update a TipoVia
@login_required(login_url='my-login')
def update_tipovia(request, pk):

    tipovia = TipoVia.objects.get(id=pk)

    form = UpdateTipoViaForm(instance=tipovia)

    if request.method == 'POST':
        form = UpdateTipoViaForm(request.POST, instance=tipovia)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoVia was updated!")
            return redirect("dashboard-tipovia")
        
    context = {'form': form}

    return render(request, 'webapp/update-tipovia.html', context=context)

# - Read / View a singular TipoVia

@login_required(login_url='my-login')
def singular_tipovia(request, pk):

    tipovia = TipoVia.objects.get(id=pk)

    context = {'tipovia': tipovia}

    return render(request, 'webapp/view-tipovia.html', context=context)

# - Delete a TipoVia

@login_required(login_url='my-login')
def delete_tipovia(request, pk):
    tipovia = TipoVia.objects.get(id=pk)
    tipovia.delete()
    messages.success(request, "Your TipoVia was deleted!")
    return redirect("dashboard-tipovia")



# - Dashboard TipoZona
@login_required(login_url='my-login')
def dashboard_tipozona(request):

    tiposzonas = TipoZona.objects.all()

    context = {'tiposzonas': tiposzonas}

    return render(request, 'webapp/dashboard-tipozona.html', context=context)


# - Create a TipoZona
@login_required(login_url='my-login')
def create_tipozona(request):

    form = CreateTipoZonaForm()

    if request.method == "POST":
        form = CreateTipoZonaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoZona was created!")
            return redirect("dashboard-tipozona")
        
    context = {'form': form}

    return render(request, 'webapp/create-tipozona.html', context=context)


# - Update a TipoZona
@login_required(login_url='my-login')
def update_tipozona(request, pk):

    tipozona = TipoZona.objects.get(id=pk)

    form = UpdateTipoZonaForm(instance=tipozona)

    if request.method == 'POST':
        form = UpdateTipoZonaForm(request.POST, instance=tipozona)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoZona was updated!")
            return redirect("dashboard-tipozona")
        
    context = {'form': form}

    return render(request, 'webapp/update-tipozona.html', context=context)

# - Read / View a singular TipoZona

@login_required(login_url='my-login')
def singular_tipozona(request, pk):

    tipozona = TipoZona.objects.get(id=pk)

    context = {'tipozona': tipozona}

    return render(request, 'webapp/view-tipozona.html', context=context)

# - Delete a TipoZona

@login_required(login_url='my-login')
def delete_tipozona(request, pk):
    tipozona = TipoZona.objects.get(id=pk)
    tipozona.delete()
    messages.success(request, "Your TipoZona was deleted!")
    return redirect("dashboard-tipozona")


# - Dashboard Direccion
@login_required(login_url='my-login')
def dashboard_direccion(request):

    direcciones = Direccion.objects.all()

    context = {'direcciones': direcciones}

    return render(request, 'webapp/dashboard-direccion.html', context=context)


# - Create a Direccion
@login_required(login_url='my-login')
def create_direccion(request):

    form = CreateDireccionForm()

    if request.method == "POST":
        form = CreateDireccionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Direccion was created!")
            return redirect("dashboard-direccion")
        
    context = {'form': form}

    return render(request, 'webapp/create-direccion.html', context=context)


# - Update a Direccion
@login_required(login_url='my-login')
def update_direccion(request, pk):

    direccion = Direccion.objects.get(id=pk)

    form = UpdateDireccionForm(instance=direccion)

    if request.method == 'POST':
        form = UpdateDireccionForm(request.POST, instance=direccion)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Direccion was updated!")
            return redirect("dashboard-direccion")
        
    context = {'form': form}

    return render(request, 'webapp/update-direccion.html', context=context)

# - Read / View a singular Direccion

@login_required(login_url='my-login')
def singular_direccion(request, pk):

    direccion = Direccion.objects.get(id=pk)

    context = {'direccion': direccion}

    return render(request, 'webapp/view-direccion.html', context=context)

# - Delete a Direccion

@login_required(login_url='my-login')
def delete_direccion(request, pk):
    direccion = Direccion.objects.get(id=pk)
    direccion.delete()
    messages.success(request, "Your Direccion was deleted!")
    return redirect("dashboard-direccion")




# - Dashboard TipoDireccion
@login_required(login_url='my-login')
def dashboard_tipodireccion(request):

    tiposdirecciones = TipoDireccion.objects.all()

    context = {'tiposdirecciones': tiposdirecciones}

    return render(request, 'webapp/dashboard-tipodireccion.html', context=context)


# - Create a TipoDireccion
@login_required(login_url='my-login')
def create_tipodireccion(request):

    form = CreateTipoDireccionForm()

    if request.method == "POST":
        form = CreateTipoDireccionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoDireccion was created!")
            return redirect("dashboard-tipodireccion")
        
    context = {'form': form}

    return render(request, 'webapp/create-tipodireccion.html', context=context)


# - Update a TipoDireccion
@login_required(login_url='my-login')
def update_tipodireccion(request, pk):

    tipodireccion = TipoDireccion.objects.get(id=pk)

    form = UpdateTipoDireccionForm(instance=tipodireccion)

    if request.method == 'POST':
        form = UpdateTipoDireccionForm(request.POST, instance=tipodireccion)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoDireccion was updated!")
            return redirect("dashboard-tipodireccion")
        
    context = {'form': form}

    return render(request, 'webapp/update-tipodireccion.html', context=context)

# - Read / View a singular TipoDireccion

@login_required(login_url='my-login')
def singular_tipodireccion(request, pk):

    tipodireccion = TipoDireccion.objects.get(id=pk)

    context = {'tipodireccion': tipodireccion}

    return render(request, 'webapp/view-tipodireccion.html', context=context)

# - Delete a TipoDireccion

@login_required(login_url='my-login')
def delete_tipodireccion(request, pk):
    tipodireccion = TipoDireccion.objects.get(id=pk)
    tipodireccion.delete()
    messages.success(request, "Your TipoDireccion was deleted!")
    return redirect("dashboard-tipodireccion")



# - Dashboard PersonaDireccion
@login_required(login_url='my-login')
def dashboard_personadireccion(request):

    personasdirecciones = PersonaDireccion.objects.all()

    context = {'personasdirecciones': personasdirecciones}

    return render(request, 'webapp/dashboard-personadireccion.html', context=context)


# - Create a PersonaDireccion
@login_required(login_url='my-login')
def create_personadireccion(request):

    form = CreatePersonaDireccionForm()

    if request.method == "POST":
        form = CreatePersonaDireccionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaDireccion was created!")
            return redirect("dashboard-personadireccion")
        
    context = {'form': form}

    return render(request, 'webapp/create-personadireccion.html', context=context)


# - Update a PersonaDireccion
@login_required(login_url='my-login')
def update_personadireccion(request, pk):

    personadireccion = PersonaDireccion.objects.get(id=pk)

    form = UpdatePersonaDireccionForm(instance=personadireccion)

    if request.method == 'POST':
        form = UpdatePersonaDireccionForm(request.POST, instance=personadireccion)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaDireccion was updated!")
            return redirect("dashboard-personadireccion")
        
    context = {'form': form}

    return render(request, 'webapp/update-personadireccion.html', context=context)

# - Read / View a singular PersonaDireccion

@login_required(login_url='my-login')
def singular_personadireccion(request, pk):

    personadireccion = PersonaDireccion.objects.get(id=pk)

    context = {'personadireccion': personadireccion}

    return render(request, 'webapp/view-personadireccion.html', context=context)

# - Delete a PersonaDireccion

@login_required(login_url='my-login')
def delete_personadireccion(request, pk):
    personadireccion = PersonaDireccion.objects.get(id=pk)
    personadireccion.delete()
    messages.success(request, "Your PersonaDireccion was deleted!")
    return redirect("dashboard-personadireccion")




# - Dashboard PersonaJuridica
@login_required(login_url='my-login')
def dashboard_personajuridica(request):

    personasjuridicas = PersonaJuridica.objects.all()

    context = {'personasjuridicas': personasjuridicas}

    return render(request, 'webapp/dashboard-personajuridica.html', context=context)


# - Create a PersonaJuridica
@login_required(login_url='my-login')
def create_personajuridica(request):

    form = CreatePersonaJuridicaForm()

    if request.method == "POST":
        form = CreatePersonaJuridicaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaJuridica was created!")
            return redirect("dashboard-personajuridica")
        
    context = {'form': form}

    return render(request, 'webapp/create-personajuridica.html', context=context)


# - Update a PersonaJuridica
@login_required(login_url='my-login')
def update_personajuridica(request, pk):
    persona = Persona.objects.get(documento=pk)
    personajuridica = PersonaJuridica.objects.get(id_persona=persona)

    form = UpdatePersonaJuridicaForm(instance=personajuridica)

    if request.method == 'POST':
        form = UpdatePersonaJuridicaForm(request.POST, instance=personajuridica)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaJuridica was updated!")
            return redirect("dashboard-personajuridica")
        
    context = {'form': form}

    return render(request, 'webapp/update-personajuridica.html', context=context)

# - Read / View a singular PersonaJuridica

@login_required(login_url='my-login')
def singular_personajuridica(request, pk):
    persona = Persona.objects.get(documento=pk)
    personajuridica = PersonaJuridica.objects.get(id_persona=persona)

    context = {'personajuridica': personajuridica}

    return render(request, 'webapp/view-personajuridica.html', context=context)

# - Delete a PersonaJuridica

@login_required(login_url='my-login')
def delete_personajuridica(request, pk):
    persona = Persona.objects.get(documento=pk)
    personajuridica = PersonaJuridica.objects.get(id_persona=persona)
    personajuridica.delete()
    messages.success(request, "Your PersonaJuridica was deleted!")
    return redirect("dashboard-personajuridica")


# - Dashboard Sexo
@login_required(login_url='my-login')
def dashboard_sexo(request):

    sexos = Sexo.objects.all()

    context = {'sexos': sexos}

    return render(request, 'webapp/dashboard-sexo.html', context=context)


# - Create a Sexo
@login_required(login_url='my-login')
def create_sexo(request):

    form = CreateSexoForm()

    if request.method == "POST":
        form = CreateSexoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Sexo was created!")
            return redirect("dashboard-sexo")
        
    context = {'form': form}

    return render(request, 'webapp/create-sexo.html', context=context)


# - Update a Sexo
@login_required(login_url='my-login')
def update_sexo(request, pk):

    sexo = Sexo.objects.get(id=pk)

    form = UpdateSexoForm(instance=sexo)

    if request.method == 'POST':
        form = UpdateSexoForm(request.POST, instance=sexo)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Sexo was updated!")
            return redirect("dashboard-sexo")
        
    context = {'form': form}

    return render(request, 'webapp/update-sexo.html', context=context)

# - Read / View a singular Sexo

@login_required(login_url='my-login')
def singular_sexo(request, pk):

    sexo = Sexo.objects.get(id=pk)

    context = {'sexo': sexo}

    return render(request, 'webapp/view-sexo.html', context=context)

# - Delete a Sexo

@login_required(login_url='my-login')
def delete_sexo(request, pk):
    sexo = Sexo.objects.get(id=pk)
    sexo.delete()
    messages.success(request, "Your Sexo was deleted!")
    return redirect("dashboard-sexo")



# - Dashboard Nacionalidad
@login_required(login_url='my-login')
def dashboard_nacionalidad(request):

    nacionalidades = Nacionalidad.objects.all()

    context = {'nacionalidades': nacionalidades}

    return render(request, 'webapp/dashboard-nacionalidad.html', context=context)


# - Create a Nacionalidad
@login_required(login_url='my-login')
def create_nacionalidad(request):

    form = CreateNacionalidadForm()

    if request.method == "POST":
        form = CreateNacionalidadForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Nacionalidad was created!")
            return redirect("dashboard-nacionalidad")
        
    context = {'form': form}

    return render(request, 'webapp/create-nacionalidad.html', context=context)


# - Update a Nacionalidad
@login_required(login_url='my-login')
def update_nacionalidad(request, pk):

    nacionalidad = Nacionalidad.objects.get(id=pk)

    form = UpdateNacionalidadForm(instance=nacionalidad)

    if request.method == 'POST':
        form = UpdateNacionalidadForm(request.POST, instance=nacionalidad)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Nacionalidad was updated!")
            return redirect("dashboard-nacionalidad")
        
    context = {'form': form}

    return render(request, 'webapp/update-nacionalidad.html', context=context)

# - Read / View a singular Nacionalidad

@login_required(login_url='my-login')
def singular_nacionalidad(request, pk):

    nacionalidad = Nacionalidad.objects.get(id=pk)

    context = {'nacionalidad': nacionalidad}

    return render(request, 'webapp/view-nacionalidad.html', context=context)

# - Delete a Nacionalidad

@login_required(login_url='my-login')
def delete_nacionalidad(request, pk):
    nacionalidad = Nacionalidad.objects.get(id=pk)
    nacionalidad.delete()
    messages.success(request, "Your Nacionalidad was deleted!")
    return redirect("dashboard-nacionalidad")



# - Dashboard PersonaNatural
@login_required(login_url='my-login')
def dashboard_personanatural(request):

    personasnaturales = PersonaNatural.objects.all()

    context = {'personasnaturales': personasnaturales}

    return render(request, 'webapp/dashboard-personanatural.html', context=context)


# - Create a PersonaNatural
@login_required(login_url='my-login')
def create_personanatural(request):

    form = CreatePersonaNaturalForm()

    if request.method == "POST":
        form = CreatePersonaNaturalForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaNatural was created!")
            return redirect("dashboard-personanatural")
        
    context = {'form': form}

    return render(request, 'webapp/create-personanatural.html', context=context)


# - Update a PersonaNatural
@login_required(login_url='my-login')
def update_personanatural(request, pk):
    persona = Persona.objects.get(documento=pk)
    personanatural = PersonaNatural.objects.get(id_persona=persona)

    form = UpdatePersonaNaturalForm(instance=personanatural)

    if request.method == 'POST':
        form = UpdatePersonaNaturalForm(request.POST, instance=personanatural)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaNatural was updated!")
            return redirect("dashboard-personanatural")
        
    context = {'form': form}

    return render(request, 'webapp/update-personanatural.html', context=context)

# - Read / View a singular PersonaNatural

@login_required(login_url='my-login')
def singular_personanatural(request, pk):
    persona = Persona.objects.get(documento=pk)
    personanatural = PersonaNatural.objects.get(id_persona=persona)

    context = {'personanatural': personanatural}

    return render(request, 'webapp/view-personanatural.html', context=context)

# - Delete a PersonaNatural

@login_required(login_url='my-login')
def delete_personanatural(request, pk):
    persona = Persona.objects.get(documento=pk)
    personanatural = PersonaNatural.objects.get(id_persona=persona)
    personanatural.delete()
    messages.success(request, "Your PersonaNatural was deleted!")
    return redirect("dashboard-personanatural")




# - Dashboard Sucursal
@login_required(login_url='my-login')
def dashboard_sucursal(request):

    sucursales = Sucursal.objects.all()

    context = {'sucursales': sucursales}

    return render(request, 'webapp/dashboard-sucursal.html', context=context)


# - Create a Sucursal
@login_required(login_url='my-login')
def create_sucursal(request):

    form = CreateSucursalForm()

    if request.method == "POST":
        form = CreateSucursalForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Sucursal was created!")
            return redirect("dashboard-sucursal")
        
    context = {'form': form}

    return render(request, 'webapp/create-sucursal.html', context=context)


# - Update a Sucursal
@login_required(login_url='my-login')
def update_sucursal(request, pk):

    sucursal = Sucursal.objects.get(id=pk)

    form = UpdateSucursalForm(instance=sucursal)

    if request.method == 'POST':
        form = UpdateSucursalForm(request.POST, instance=sucursal)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Sucursal was updated!")
            return redirect("dashboard-sucursal")
        
    context = {'form': form}

    return render(request, 'webapp/update-sucursal.html', context=context)

# - Read / View a singular Sucursal

@login_required(login_url='my-login')
def singular_sucursal(request, pk):

    sucursal = Sucursal.objects.get(id=pk)

    context = {'sucursal': sucursal}

    return render(request, 'webapp/view-sucursal.html', context=context)

# - Delete a Sucursal

@login_required(login_url='my-login')
def delete_sucursal(request, pk):
    sucursal = Sucursal.objects.get(id=pk)
    sucursal.delete()
    messages.success(request, "Your Sucursal was deleted!")
    return redirect("dashboard-sucursal")



# - Dashboard Cargo
@login_required(login_url='my-login')
def dashboard_cargo(request):

    cargos = Cargo.objects.all()

    context = {'cargos': cargos}

    return render(request, 'webapp/dashboard-cargo.html', context=context)


# - Create a Cargo
@login_required(login_url='my-login')
def create_cargo(request):

    form = CreateCargoForm()

    if request.method == "POST":
        form = CreateCargoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Cargo was created!")
            return redirect("dashboard-cargo")
        
    context = {'form': form}

    return render(request, 'webapp/create-cargo.html', context=context)


# - Update a Cargo
@login_required(login_url='my-login')
def update_cargo(request, pk):

    cargo = Cargo.objects.get(id=pk)

    form = UpdateCargoForm(instance=cargo)

    if request.method == 'POST':
        form = UpdateCargoForm(request.POST, instance=cargo)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Cargo was updated!")
            return redirect("dashboard-cargo")
        
    context = {'form': form}

    return render(request, 'webapp/update-cargo.html', context=context)

# - Read / View a singular Cargo

@login_required(login_url='my-login')
def singular_cargo(request, pk):

    cargo = Cargo.objects.get(id=pk)

    context = {'cargo': cargo}

    return render(request, 'webapp/view-cargo.html', context=context)

# - Delete a Cargo

@login_required(login_url='my-login')
def delete_cargo(request, pk):
    cargo = Cargo.objects.get(id=pk)
    cargo.delete()
    messages.success(request, "Your Cargo was deleted!")
    return redirect("dashboard-cargo")


# - Dashboard Rol
@login_required(login_url='my-login')
def dashboard_rol(request):

    roles = Rol.objects.all()

    context = {'roles': roles}

    return render(request, 'webapp/dashboard-rol.html', context=context)


# - Create a Rol
@login_required(login_url='my-login')
def create_rol(request):

    form = CreateRolForm()

    if request.method == "POST":
        form = CreateRolForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Rol was created!")
            return redirect("dashboard-rol")
        
    context = {'form': form}

    return render(request, 'webapp/create-rol.html', context=context)


# - Update a Rol
@login_required(login_url='my-login')
def update_rol(request, pk):

    rol = Rol.objects.get(id=pk)

    form = UpdateRolForm(instance=rol)

    if request.method == 'POST':
        form = UpdateRolForm(request.POST, instance=rol)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Rol was updated!")
            return redirect("dashboard-rol")
        
    context = {'form': form}

    return render(request, 'webapp/update-rol.html', context=context)

# - Read / View a singular Rol

@login_required(login_url='my-login')
def singular_rol(request, pk):

    rol = Rol.objects.get(id=pk)

    context = {'rol': rol}

    return render(request, 'webapp/view-rol.html', context=context)

# - Delete a Rol

@login_required(login_url='my-login')
def delete_rol(request, pk):
    rol = Rol.objects.get(id=pk)
    rol.delete()
    messages.success(request, "Your Rol was deleted!")
    return redirect("dashboard-rol")




# - Dashboard Empleado
@login_required(login_url='my-login')
def dashboard_empleado(request):

    empleados = Empleado.objects.all()

    context = {'empleados': empleados}

    return render(request, 'webapp/dashboard-empleado.html', context=context)


# - Create an Empleado
@login_required(login_url='my-login')
def create_empleado(request):

    form = CreateEmpleadoForm()

    if request.method == "POST":
        form = CreateEmpleadoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Empleado was created!")
            return redirect("dashboard-empleado")
        
    context = {'form': form}

    return render(request, 'webapp/create-empleado.html', context=context)


# - Update an Empleado
@login_required(login_url='my-login')
def update_empleado(request, pk):

    empleado = Empleado.objects.get(id=pk)

    form = UpdateEmpleadoForm(instance=empleado)

    if request.method == 'POST':
        form = UpdateEmpleadoForm(request.POST, instance=empleado)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Empleado was updated!")
            return redirect("dashboard-empleado")
        
    context = {'form': form}

    return render(request, 'webapp/update-empleado.html', context=context)

# - Read / View a singular Empleado

@login_required(login_url='my-login')
def singular_empleado(request, pk):

    empleado = Empleado.objects.get(id=pk)

    context = {'empleado': empleado}

    return render(request, 'webapp/view-empleado.html', context=context)

# - Delete an Empleado

@login_required(login_url='my-login')
def delete_empleado(request, pk):
    empleado = Empleado.objects.get(id=pk)
    empleado.delete()
    messages.success(request, "Your Empleado was deleted!")
    return redirect("dashboard-empleado")




# - Dashboard TipoCliente
@login_required(login_url='my-login')
def dashboard_tipocliente(request):

    tiposclientes = TipoCliente.objects.all()

    context = {'tiposclientes': tiposclientes}

    return render(request, 'webapp/dashboard-tipocliente.html', context=context)


# - Create a TipoCliente
@login_required(login_url='my-login')
def create_tipocliente(request):

    form = CreateTipoClienteForm()

    if request.method == "POST":
        form = CreateTipoClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoCliente was created!")
            return redirect("dashboard-tipocliente")
        
    context = {'form': form}

    return render(request, 'webapp/create-tipocliente.html', context=context)


# - Update a TipoCliente
@login_required(login_url='my-login')
def update_tipocliente(request, pk):

    tipocliente = TipoCliente.objects.get(id=pk)

    form = UpdateTipoClienteForm(instance=tipocliente)

    if request.method == 'POST':
        form = UpdateTipoClienteForm(request.POST, instance=tipocliente)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoCliente was updated!")
            return redirect("dashboard-tipocliente")
        
    context = {'form': form}

    return render(request, 'webapp/update-tipocliente.html', context=context)

# - Read / View a singular TipoCliente

@login_required(login_url='my-login')
def singular_tipocliente(request, pk):

    tipocliente = TipoCliente.objects.get(id=pk)

    context = {'tipocliente': tipocliente}

    return render(request, 'webapp/view-tipocliente.html', context=context)

# - Delete a TipoCliente

@login_required(login_url='my-login')
def delete_tipocliente(request, pk):
    tipocliente = TipoCliente.objects.get(id=pk)
    tipocliente.delete()
    messages.success(request, "Your TipoCliente was deleted!")
    return redirect("dashboard-tipocliente")


# - Dashboard Cliente
@login_required(login_url='my-login')
def dashboard_cliente(request):

    clientes = Cliente.objects.all()

    context = {'clientes': clientes}

    return render(request, 'webapp/dashboard-cliente.html', context=context)


# - Create a Cliente
@login_required(login_url='my-login')
def create_cliente(request):

    form = CreateClienteForm()

    if request.method == "POST":
        form = CreateClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Cliente was created!")
            return redirect("dashboard-cliente")
        
    context = {'form': form}

    return render(request, 'webapp/create-cliente.html', context=context)


# - Update a Cliente
@login_required(login_url='my-login')
def update_cliente(request, pk):

    persona = Persona.objects.get(documento=pk)
    cliente = Cliente.objects.get(id_persona=persona)

    form = UpdateClienteForm(instance=cliente)

    if request.method == 'POST':
        form = UpdateClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Cliente was updated!")
            return redirect("dashboard-cliente")
        
    context = {'form': form}

    return render(request, 'webapp/update-cliente.html', context=context)

# - Read / View a singular Cliente

@login_required(login_url='my-login')
def singular_cliente(request, pk):

    persona = Persona.objects.get(documento=pk)
    cliente = Cliente.objects.get(id_persona=persona)

    context = {'cliente': cliente}

    return render(request, 'webapp/view-cliente.html', context=context)

# - Delete a Cliente

@login_required(login_url='my-login')
def delete_cliente(request, pk):
    persona = Persona.objects.get(documento=pk)
    cliente = Cliente.objects.get(id_persona=persona)
    cliente.delete()
    messages.success(request, "Your Cliente was deleted!")
    return redirect("dashboard-cliente")




# - Dashboard Proveedor
@login_required(login_url='my-login')
def dashboard_proveedor(request):

    proveedores = Proveedor.objects.all()

    context = {'proveedores': proveedores}

    return render(request, 'webapp/dashboard-proveedor.html', context=context)


# - Create a Proveedor
@login_required(login_url='my-login')
def create_proveedor(request):

    form = CreateProveedorForm()

    if request.method == "POST":
        form = CreateProveedorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Proveedor was created!")
            return redirect("dashboard-proveedor")
        
    context = {'form': form}

    return render(request, 'webapp/create-proveedor.html', context=context)


# - Update a Proveedor
@login_required(login_url='my-login')
def update_proveedor(request, pk):

    proveedor = Proveedor.objects.get(id=pk)

    form = UpdateProveedorForm(instance=proveedor)

    if request.method == 'POST':
        form = UpdateProveedorForm(request.POST, instance=proveedor)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Proveedor was updated!")
            return redirect("dashboard-proveedor")
        
    context = {'form': form}

    return render(request, 'webapp/update-proveedor.html', context=context)

# - Read / View a singular Proveedor

@login_required(login_url='my-login')
def singular_proveedor(request, pk):

    proveedor = Proveedor.objects.get(id=pk)

    context = {'proveedor': proveedor}

    return render(request, 'webapp/view-proveedor.html', context=context)

# - Delete a Proveedor

@login_required(login_url='my-login')
def delete_proveedor(request, pk):
    proveedor = Proveedor.objects.get(id=pk)
    proveedor.delete()
    messages.success(request, "Your Proveedor was deleted!")
    return redirect("dashboard-proveedor")



# - Dashboard Venta
@login_required(login_url='my-login')
def dashboard_venta(request):

    ventas = Venta.objects.all()

    context = {'ventas': ventas}

    return render(request, 'webapp/dashboard-venta.html', context=context)


# - Create a Venta
@login_required(login_url='my-login')
def create_venta(request):

    form = CreateVentaForm()

    if request.method == "POST":
        form = CreateVentaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Venta was created!")
            return redirect("dashboard-venta")
        
    context = {'form': form}

    return render(request, 'webapp/create-venta.html', context=context)


# - Update a Venta
@login_required(login_url='my-login')
def update_venta(request, pk):

    venta = Venta.objects.get(id=pk)

    form = UpdateVentaForm(instance=venta)

    if request.method == 'POST':
        form = UpdateVentaForm(request.POST, instance=venta)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Venta was updated!")
            return redirect("dashboard-venta")
        
    context = {'form': form}

    return render(request, 'webapp/update-venta.html', context=context)

# - Read / View a singular Venta

@login_required(login_url='my-login')
def singular_venta(request, pk):

    venta = Venta.objects.get(id=pk)

    context = {'venta': venta}

    return render(request, 'webapp/view-venta.html', context=context)

# - Delete a Venta

@login_required(login_url='my-login')
def delete_venta(request, pk):
    venta = Venta.objects.get(id=pk)
    venta.delete()
    messages.success(request, "Your Venta was deleted!")
    return redirect("dashboard-venta")



# - Dashboard DetalleVenta
@login_required(login_url='my-login')
def dashboard_detalleventa(request):

    detalles_venta = DetalleVenta.objects.all()

    context = {'detalles_venta': detalles_venta}

    return render(request, 'webapp/dashboard-detalleventa.html', context=context)


# - Create a DetalleVenta
@login_required(login_url='my-login')
def create_detalleventa(request):

    form = CreateDetalleVentaForm()

    if request.method == "POST":
        form = CreateDetalleVentaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your DetalleVenta was created!")
            return redirect("dashboard-detalleventa")
        
    context = {'form': form}

    return render(request, 'webapp/create-detalleventa.html', context=context)


# - Update a DetalleVenta
@login_required(login_url='my-login')
def update_detalleventa(request, pk):

    detalleventa = DetalleVenta.objects.get(id=pk)

    form = UpdateDetalleVentaForm(instance=detalleventa)

    if request.method == 'POST':
        form = UpdateDetalleVentaForm(request.POST, instance=detalleventa)

        if form.is_valid():
            form.save()
            messages.success(request, "Your DetalleVenta was updated!")
            return redirect("dashboard-detalleventa")
        
    context = {'form': form}

    return render(request, 'webapp/update-detalleventa.html', context=context)

# - Read / View a singular DetalleVenta

@login_required(login_url='my-login')
def singular_detalleventa(request, pk):

    detalleventa = DetalleVenta.objects.get(id=pk)

    context = {'detalleventa': detalleventa}

    return render(request, 'webapp/view-detalleventa.html', context=context)

# - Delete a DetalleVenta

@login_required(login_url='my-login')
def delete_detalleventa(request, pk):
    detalleventa = DetalleVenta.objects.get(id=pk)
    detalleventa.delete()
    messages.success(request, "Your DetalleVenta was deleted!")
    return redirect("dashboard-detalleventa")



# - Dashboard TipoComprobante
@login_required(login_url='my-login')
def dashboard_tipocomprobante(request):

    tiposcomprobantes = TipoComprobante.objects.all()

    context = {'tiposcomprobantes': tiposcomprobantes}

    return render(request, 'webapp/dashboard-tipocomprobante.html', context=context)


# - Create a TipoComprobante
@login_required(login_url='my-login')
def create_tipocomprobante(request):

    form = CreateTipoComprobanteForm()

    if request.method == "POST":
        form = CreateTipoComprobanteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoComprobante was created!")
            return redirect("dashboard-tipocomprobante")
        
    context = {'form': form}

    return render(request, 'webapp/create-tipocomprobante.html', context=context)


# - Update a TipoComprobante
@login_required(login_url='my-login')
def update_tipocomprobante(request, pk):

    tipocomprobante = TipoComprobante.objects.get(id=pk)

    form = UpdateTipoComprobanteForm(instance=tipocomprobante)

    if request.method == 'POST':
        form = UpdateTipoComprobanteForm(request.POST, instance=tipocomprobante)

        if form.is_valid():
            form.save()
            messages.success(request, "Your TipoComprobante was updated!")
            return redirect("dashboard-tipocomprobante")
        
    context = {'form': form}

    return render(request, 'webapp/update-tipocomprobante.html', context=context)

# - Read / View a singular TipoComprobante

@login_required(login_url='my-login')
def singular_tipocomprobante(request, pk):

    tipocomprobante = TipoComprobante.objects.get(id=pk)

    context = {'tipocomprobante': tipocomprobante}

    return render(request, 'webapp/view-tipocomprobante.html', context=context)

# - Delete a TipoComprobante

@login_required(login_url='my-login')
def delete_tipocomprobante(request, pk):
    tipocomprobante = TipoComprobante.objects.get(id=pk)
    tipocomprobante.delete()
    messages.success(request, "Your TipoComprobante was deleted!")
    return redirect("dashboard-tipocomprobante")



# - Dashboard SucursalSerie
@login_required(login_url='my-login')
def dashboard_sucursalserie(request):

    sucursalesseries = SucursalSerie.objects.all()

    context = {'sucursalesseries': sucursalesseries}

    return render(request, 'webapp/dashboard-sucursalserie.html', context=context)


# - Create a SucursalSerie
@login_required(login_url='my-login')
def create_sucursalserie(request):

    form = CreateSucursalSerieForm()

    if request.method == "POST":
        form = CreateSucursalSerieForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your SucursalSerie was created!")
            return redirect("dashboard-sucursalserie")
        
    context = {'form': form}

    return render(request, 'webapp/create-sucursalserie.html', context=context)


# - Update a SucursalSerie
@login_required(login_url='my-login')
def update_sucursalserie(request, pk):

    sucursalserie = SucursalSerie.objects.get(id=pk)

    form = UpdateSucursalSerieForm(instance=sucursalserie)

    if request.method == 'POST':
        form = UpdateSucursalSerieForm(request.POST, instance=sucursalserie)

        if form.is_valid():
            form.save()
            messages.success(request, "Your SucursalSerie was updated!")
            return redirect("dashboard-sucursalserie")
        
    context = {'form': form}

    return render(request, 'webapp/update-sucursalserie.html', context=context)

# - Read / View a singular SucursalSerie

@login_required(login_url='my-login')
def singular_sucursalserie(request, pk):

    sucursalserie = SucursalSerie.objects.get(id=pk)

    context = {'sucursalserie': sucursalserie}

    return render(request, 'webapp/view-sucursalserie.html', context=context)

# - Delete a SucursalSerie

@login_required(login_url='my-login')
def delete_sucursalserie(request, pk):
    sucursalserie = SucursalSerie.objects.get(id=pk)
    sucursalserie.delete()
    messages.success(request, "Your SucursalSerie was deleted!")
    return redirect("dashboard-sucursalserie")



# - Dashboard ComprobanteVenta
@login_required(login_url='my-login')
def dashboard_comprobanteventa(request):

    comprobantesventas = ComprobanteVenta.objects.all()

    context = {'comprobantes_venta': comprobantesventas}

    return render(request, 'webapp/dashboard-comprobanteventa.html', context=context)


# - Create a ComprobanteVenta
@login_required(login_url='my-login')
def create_comprobanteventa(request):

    form = CreateComprobanteVentaForm()

    if request.method == "POST":
        form = CreateComprobanteVentaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your ComprobanteVenta was created!")
            return redirect("dashboard-comprobanteventa")
        
    context = {'form': form}

    return render(request, 'webapp/create-comprobanteventa.html', context=context)


# - Update a ComprobanteVenta
@login_required(login_url='my-login')
def update_comprobanteventa(request, pk):

    comprobanteventa = ComprobanteVenta.objects.get(id=pk)

    form = UpdateComprobanteVentaForm(instance=comprobanteventa)

    if request.method == 'POST':
        form = UpdateComprobanteVentaForm(request.POST, instance=comprobanteventa)

        if form.is_valid():
            form.save()
            messages.success(request, "Your ComprobanteVenta was updated!")
            return redirect("dashboard-comprobanteventa")
        
    context = {'form': form}

    return render(request, 'webapp/update-comprobanteventa.html', context=context)

# - Read / View a singular ComprobanteVenta

@login_required(login_url='my-login')
def singular_comprobanteventa(request, pk):

    comprobanteventa = ComprobanteVenta.objects.get(id=pk)

    context = {'comprobanteventa': comprobanteventa}

    return render(request, 'webapp/view-comprobanteventa.html', context=context)

# - Delete a ComprobanteVenta

@login_required(login_url='my-login')
def delete_comprobanteventa(request, pk):
    comprobanteventa = ComprobanteVenta.objects.get(id=pk)
    comprobanteventa.delete()
    messages.success(request, "Your ComprobanteVenta was deleted!")
    return redirect("dashboard-comprobanteventa")



# - Dashboard Compra
@login_required(login_url='my-login')
def dashboard_compra(request):

    compras = Compra.objects.all()

    context = {'compras': compras}

    return render(request, 'webapp/dashboard-compra.html', context=context)


# - Create a Compra
@login_required(login_url='my-login')
def create_compra(request):

    form = CreateCompraForm()

    if request.method == "POST":
        form = CreateCompraForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Compra was created!")
            return redirect("dashboard-compra")
        
    context = {'form': form}

    return render(request, 'webapp/create-compra.html', context=context)


# - Update a Compra
@login_required(login_url='my-login')
def update_compra(request, pk):

    compra = Compra.objects.get(id=pk)

    form = UpdateCompraForm(instance=compra)

    if request.method == 'POST':
        form = UpdateCompraForm(request.POST, instance=compra)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Compra was updated!")
            return redirect("dashboard-compra")
        
    context = {'form': form}

    return render(request, 'webapp/update-compra.html', context=context)

# - Read / View a singular Compra

@login_required(login_url='my-login')
def singular_compra(request, pk):

    compra = Compra.objects.get(id=pk)

    context = {'compra': compra}

    return render(request, 'webapp/view-compra.html', context=context)

# - Delete a Compra

@login_required(login_url='my-login')
def delete_compra(request, pk):
    compra = Compra.objects.get(id=pk)
    compra.delete()
    messages.success(request, "Your Compra was deleted!")
    return redirect("dashboard-compra")



# - Dashboard DetalleCompra
@login_required(login_url='my-login')
def dashboard_detallecompra(request):

    detallescompras = DetalleCompra.objects.all()

    context = {'detalles_compra': detallescompras}

    return render(request, 'webapp/dashboard-detallecompra.html', context=context)


# - Create a DetalleCompra
@login_required(login_url='my-login')
def create_detallecompra(request):

    form = CreateDetalleCompraForm()

    if request.method == "POST":
        form = CreateDetalleCompraForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your DetalleCompra was created!")
            return redirect("dashboard-detallecompra")
        
    context = {'form': form}

    return render(request, 'webapp/create-detallecompra.html', context=context)


# - Update a DetalleCompra
@login_required(login_url='my-login')
def update_detallecompra(request, pk):

    detallecompra = DetalleCompra.objects.get(id=pk)

    form = UpdateDetalleCompraForm(instance=detallecompra)

    if request.method == 'POST':
        form = UpdateDetalleCompraForm(request.POST, instance=detallecompra)

        if form.is_valid():
            form.save()
            messages.success(request, "Your DetalleCompra was updated!")
            return redirect("dashboard-detallecompra")
        
    context = {'form': form}

    return render(request, 'webapp/update-detallecompra.html', context=context)

# - Read / View a singular DetalleCompra

@login_required(login_url='my-login')
def singular_detallecompra(request, pk):

    detallecompra = DetalleCompra.objects.get(id=pk)

    context = {'detallecompra': detallecompra}

    return render(request, 'webapp/view-detallecompra.html', context=context)

# - Delete a DetalleCompra

@login_required(login_url='my-login')
def delete_detallecompra(request, pk):
    detallecompra = DetalleCompra.objects.get(id=pk)
    detallecompra.delete()
    messages.success(request, "Your DetalleCompra was deleted!")
    return redirect("dashboard-detallecompra")



# - Dashboard Oficio
@login_required(login_url='my-login')
def dashboard_oficio(request):

    oficios = Oficio.objects.all()

    context = {'oficios': oficios}

    return render(request, 'webapp/dashboard-oficio.html', context=context)


# - Create an Oficio
@login_required(login_url='my-login')
def create_oficio(request):

    form = CreateOficioForm()

    if request.method == "POST":
        form = CreateOficioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Oficio was created!")
            return redirect("dashboard-oficio")
        
    context = {'form': form}

    return render(request, 'webapp/create-oficio.html', context=context)


# - Update an Oficio
@login_required(login_url='my-login')
def update_oficio(request, pk):

    oficio = Oficio.objects.get(id=pk)

    form = UpdateOficioForm(instance=oficio)

    if request.method == 'POST':
        form = UpdateOficioForm(request.POST, instance=oficio)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Oficio was updated!")
            return redirect("dashboard-oficio")
        
    context = {'form': form}

    return render(request, 'webapp/update-oficio.html', context=context)

# - Read / View a singular Oficio

@login_required(login_url='my-login')
def singular_oficio(request, pk):

    oficio = Oficio.objects.get(id=pk)

    context = {'oficio': oficio}

    return render(request, 'webapp/view-oficio.html', context=context)

# - Delete an Oficio

@login_required(login_url='my-login')
def delete_oficio(request, pk):
    oficio = Oficio.objects.get(id=pk)
    oficio.delete()
    messages.success(request, "Your Oficio was deleted!")
    return redirect("dashboard-oficio")


# - Dashboard PersonaOficio
@login_required(login_url='my-login')
def dashboard_personaoficio(request):

    personasoficios = PersonaOficio.objects.all()

    context = {'personasoficios': personasoficios}

    return render(request, 'webapp/dashboard-personaoficio.html', context=context)


# - Create a PersonaOficio
@login_required(login_url='my-login')
def create_personaoficio(request):

    form = CreatePersonaOficioForm()

    if request.method == "POST":
        form = CreatePersonaOficioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaOficio was created!")
            return redirect("dashboard-personaoficio")
        
    context = {'form': form}

    return render(request, 'webapp/create-personaoficio.html', context=context)



# - Update a PersonaOficio
@login_required(login_url='my-login')
def update_personaoficio(request, pk):

    persona_oficio = PersonaOficio.objects.get(id=pk)

    form = UpdatePersonaOficioForm(instance=persona_oficio)

    if request.method == 'POST':
        form = UpdatePersonaOficioForm(request.POST, instance=persona_oficio)

        if form.is_valid():
            form.save()
            messages.success(request, "Your PersonaOficio was updated!")
            return redirect("dashboard-personaoficio")
        
    context = {'form': form}

    return render(request, 'webapp/update-personaoficio.html', context=context)

# - Read / View a singular PersonaOficio

@login_required(login_url='my-login')
def singular_personaoficio(request, pk):

    persona_oficio = PersonaOficio.objects.get(id=pk)

    context = {'persona_oficio': persona_oficio}

    return render(request, 'webapp/view-personaoficio.html', context=context)

# - Delete a PersonaOficio

@login_required(login_url='my-login')
def delete_personaoficio(request, pk):
    persona_oficio = PersonaOficio.objects.get(id=pk)
    persona_oficio.delete()
    messages.success(request, "Your PersonaOficio was deleted!")
    return redirect("dashboard-personaoficio")














# - User logout

def user_logout(request):
    
    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")
