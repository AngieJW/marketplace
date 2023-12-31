from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('core:index')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form,
    })
