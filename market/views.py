from django.shortcuts import render
from .models import Type, Item, SHG

def home(request):
    categories = Type.objects.all()
    new_items = Item.objects.order_by('-id')[:5]
    shg_stories = SHG.objects.all()[:3]  # can limit or filter as needed

    context = {
        'categories': categories,
        'new_items': new_items,
        'shg_stories': shg_stories,
    }
    return render(request, 'market/home.html', context)

