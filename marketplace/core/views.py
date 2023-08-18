from django.shortcuts import render

from item.models import Category, Item

# Create your views here.
def index(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')
