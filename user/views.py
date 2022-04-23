from django.shortcuts import redirect, render
from .models import User
from .forms import Add_A_User

# Create your views here.
def home(request):
    users = User.objects.all()
    context = {'users' : users}
    return render(request, 'home.html', context)

def addUser(request):
    if request.method == 'POST':
        form = Add_A_User(request.POST)
        if form.is_valid():
            form.save()
            users = User.objects.all()
            context = {'users' : users}
            return redirect('/', context)
    else:
        form = Add_A_User()        
        context = {'form' : form}
    
    return render(request, 'addUser.html', context)

def editUser(request, id):
    user = User.objects.filter(id=id).first()
    form = Add_A_User(instance=user)

    if request.method == 'POST':
        form = Add_A_User(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form' : form}
    return render(request, 'editUser.html', context)

def deleteUser(request, id):
    delete_user = User.objects.filter(id=id)
    context = {'delete' : delete_user}
    if request.method == 'POST':
        delete_user.delete()
        return redirect('/')
    return render(request, 'deleteUser.html', context)