from django.shortcuts import render
from .models import Category, Dish

# Create your views here.
def main_page_view(request):
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for item in categories:
        dishes = Dish.objects.filter(category=item.pk).filter(is_visible=True).order_by('dish_order')
        item.dishes = dishes

    special = Dish.objects.filter(category__title='Особенное меню')


    return render(request, 'index.html', context={
        'categories': categories,
        'special': special
    })
