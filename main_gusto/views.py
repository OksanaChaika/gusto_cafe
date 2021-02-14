from django.shortcuts import render

# Create your views here.
def main_page_view(request):
    categories = [
        'Закуски',
        'Основные блюда',
        'Гарниры',
        'Десерты'
    ]

    return render(request, 'index.html', context={
        'categories': categories
    })
