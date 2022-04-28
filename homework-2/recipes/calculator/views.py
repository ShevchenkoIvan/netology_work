from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipes_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    recipes_dict = dict()
    if DATA.get(dish):
        for ingredient, amount in DATA.get(dish).items():
            summ = amount * servings
            recipes_dict[ingredient] = summ

    context = {
        'recipe': recipes_dict
    }
    return render(request, 'calculator/index.html', context)
