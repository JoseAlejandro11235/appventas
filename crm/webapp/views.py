from django.shortcuts import render, redirect
from .forms import LoginForm,CreateRecordForm, UpdateRecordForm, CreateAreaForm, UpdateAreaForm, CreateCategoriaForm, UpdateCategoriaForm, CreateCategoriaPadreForm, UpdateCategoriaPadreForm, CreateMarcaForm, UpdateMarcaForm, CreateUnidadMedidaForm, UpdateUnidadMedidaForm, CreateProductoForm, UpdateProductoForm, CreateProductoCategoriaForm, UpdateProductoCategoriaForm, CreateProductoPrecioForm, UpdateProductoPrecioForm, CreateTipoDocumentoForm, UpdateTipoDocumentoForm, CreatePersonaForm, UpdatePersonaForm, CreateOperadorForm, UpdateOperadorForm, CreateTipoTelefonoForm, UpdateTipoTelefonoForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record, Area, Categoria, CategoriaPadre, Marca, UnidadMedida, Producto, ProductoCategoria, ProductoPrecio, TipoDocumento, Persona, Operador, TipoTelefono

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





# - User logout

def user_logout(request):
    
    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")
