from django.shortcuts import render
from .models import *

# Create your views here.
def main_page_view(request):
    cafe_info = Info.objects.all().filter(is_visible=True)
    cafe_data = CafeInfo.objects.all()
    opening_hours = OpeningHours.objects.all()
    team_info = Team.objects.all().filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for item in categories:
        dishes = Dish.objects.filter(category=item.pk).filter(is_visible=True).order_by('dish_order')
        item.dishes = dishes

    special = Dish.objects.filter(category__title='Особенное меню')

    return render(request, 'index.html', context={
        'categories': categories,
        'special': special,
        'team_info': team_info[0],
        'info': cafe_info[0],
        'opening_hours': opening_hours,
        'cafe_data': cafe_data
    })

def dish_page_view(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish_info.html', context={'dish': dish})
