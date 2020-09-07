from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Fuel, Distributor
from django.http import Http404, HttpResponseRedirect
from .forms import BuyForm
from Cabinet.models import Order
from django.contrib.auth.decorators import login_required

def main_view(request):
    return render(request, 'Home/home.html')

def about_view(request):
    return render(request, 'Home/about.html')

class Category_view(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'Home/categories.html', {'categories': categories})

class Fuel_view(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        fuels = Fuel.objects.filter(type_id=category.id)
        return render(request, 'Home/fuels.html', {'fuels': fuels})

@login_required
def buyform(request, slug, pk):
    try:
        user = request.user
        category = Category.objects.get(slug=slug)
        fuel = Fuel.objects.get(id=pk, type_id=category.id)
        if request.method == 'POST':
            buy_form = BuyForm(request.POST)
            if buy_form.is_valid():
                new_order = Order(volume=buy_form.cleaned_data['volume'], address=buy_form.cleaned_data['address'], client_id=user.id, fuel_id=pk)
                new_order.save()
                return HttpResponseRedirect('/cabinet/current_orders/')
        else:
            buy_form = BuyForm()
        return render(request, 'Home/fuel_detail.html', {'fuel': fuel, 'buy_form':buy_form})
    except:
        raise Http404