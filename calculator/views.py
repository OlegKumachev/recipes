from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipes(request, recipes):
    DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },

    }
    ingredient = {}
    servings = float(request.GET.get('servings', 1))
    for ing, amount in DATA[recipes].items():
        result = float(amount) * servings
        ingredient.update({ing: result})
    context = {'recipes': ingredient}

    return render(request, 'calculator/index.html',  context)


