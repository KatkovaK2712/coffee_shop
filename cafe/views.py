from django.shortcuts import render, redirect
from .models import Category, MenuItem, Review, PreOrder, HomePageContent, AboutPageContent, ContactsPageContent, CatTeamMember
from .forms import PreOrderForm, ReviewForm

def home(request):
    special_items = MenuItem.objects.filter(is_special=True, is_available=True)[:3]
    reviews = Review.objects.all().order_by('-created_at')[:3]
    home_content = HomePageContent.objects.all()
    
    context = {
        'special_items': special_items,
        'reviews': reviews,
        'home_content': home_content,
        'title': 'Главная'
    }
    return render(request, 'cafe/home.html', context)

def menu(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': 'Меню'
    }
    return render(request, 'cafe/menu.html', context)

def about(request):
    about_content = AboutPageContent.objects.all()
    cat_team = CatTeamMember.objects.all().order_by('order')
    context = {
        'about_content': about_content,
        'cat_team': cat_team,
        'title': 'О нас'
    }
    return render(request, 'cafe/about.html', context)

def contacts(request):
    contacts_content = ContactsPageContent.objects.all()
    context = {
        'contacts_content': contacts_content,
        'title': 'Контакты'
    }
    return render(request, 'cafe/contacts.html', context)

def reviews_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    
    reviews_list = Review.objects.all().order_by('-created_at')
    context = {
        'reviews': reviews_list,
        'form': form,
        'title': 'Отзывы'
    }
    return render(request, 'cafe/reviews.html', context)

def preorder(request):
    if request.method == 'POST':
        form = PreOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.items = "Временный заказ"
            order.total_amount = 0
            order.save()
            return redirect('preorder_success')
    else:
        form = PreOrderForm()
    
    context = {
        'form': form,
        'title': 'Предзаказ'
    }
    return render(request, 'cafe/preorder.html', context)

def preorder_success(request):
    return render(request, 'cafe/preorder_success.html', {'title': 'Заказ принят'})