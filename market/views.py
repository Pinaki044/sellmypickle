from django.shortcuts import render
from .models import Type, Item, SHG
from django.shortcuts import get_object_or_404

def home(request):
    print('home mai gaya')
    categories = Type.objects.all()
    new_items = Item.objects.order_by('-id')[:5]
    shg_stories = SHGStory.objects.all()  # can limit or filter as needed

    context = {
        'categories': categories,
        'new_items': new_items,
        'shg_stories': shg_stories,
    }
    return render(request, 'market/home.html', context)

def browse(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'market/browse.html', context)

def wishlist(request):
    # Placeholder logic for now
    return render(request, 'market/wishlist.html')

def cart(request):
    # Placeholder logic for now
    return render(request, 'market/cart.html')

def shg_list(request):
    shgs = SHG.objects.all()
    context = {
        'shgs': shgs
    }
    return render(request, 'market/shg_list.html', context)

def shg_detail(request, pk):
    story = get_object_or_404(SHGStory, pk=pk)
    return render(request, 'market/shg_detail.html', {'story': story})

def pickle_list(request):
    pickles = Product.objects.filter(category='Pickle')
    return render(request, 'market/pickle_list.html', {'pickles': pickles})

