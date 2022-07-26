from django.shortcuts import render, redirect
from dj_app.forms import UserForm
from dj_app.models import Sale
from dj_app.utils import get_plot

def index_page(request):   
    qs = Sale.objects.all()
    item = [x.item for x in qs]
    price = [y.price for y in qs]

    chart = get_plot(item, price)

    context = {'chart': chart}
    return render(request, 'index.html', context)
