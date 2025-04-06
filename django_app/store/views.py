from django.shortcuts import render, redirect
from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products, 'form': form})