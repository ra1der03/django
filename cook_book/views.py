from django.http import HttpResponse
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
}


def recipe(request, name):
    data = {}
    servings = request.GET.get('servings')
    for i in DATA:
        data['title'] = name
        if i == name:
            data['name'] = DATA.get(i)
        else:
            continue
    if servings:
        for m in data['name']:
            data['name'][m] = data['name'].get(m)*int(servings)
    return render(request, 'recipes.html', data)


