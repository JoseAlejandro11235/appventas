from django.shortcuts import render, redirect
from .forms import LoginForm, CreateRecordForm, UpdateRecordForm, CreateAreaForm, UpdateAreaForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record, Area

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


# - User logout

def user_logout(request):
    
    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")
