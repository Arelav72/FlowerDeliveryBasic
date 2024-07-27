from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Flower, Order
from .forms import UserRegisterForm, OrderForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'orders/register.html', {'form': form})

@login_required
def catalog(request):
    flowers = Flower.objects.all()
    return render(request, 'orders/catalog.html', {'flowers': flowers})

@login_required
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            form.save_m2m()
            return redirect('catalog')
    else:
        form = OrderForm()
    return render(request, 'orders/order.html', {'form': form})

# Create your views here.
