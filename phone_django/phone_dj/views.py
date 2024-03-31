from django.shortcuts import render
from phone_dj.models import Phone
from import_phones import data


def create_phone(request):
    all, context, phones = [], {}, []
    sort = request.GET.get('sort')
    for el in range(3):
        one = []
        for elem in data:
            one.append(data[elem][el])
        all.append(one)
    for i, one in enumerate(all, 0):
        phones.append(Phone(id=one[0], name=one[1], img=one[2], price=one[3], release_date=one[4],
                      lte_exists=one[5], slug=one[1].replace(' ', '-')))
    if sort == 'min_price':
        phones = sorted(phones, key=lambda x: x.price)
    elif sort == 'max_price':
        phones = sorted(phones, key=lambda x: x.price, reverse=True)
    elif sort == 'name':
        phones = sorted(phones, key=lambda x: x.name, reverse=True)
    for i, one in enumerate(phones, 0):
        context[i] = one
    return render(request, 'phones.html', context)


def display_phone(request, name):
    allem, context = {}, {}
    for el in range(3):
        if data['name'][el].replace(' ', '-') == name:
            for elem in data:
                allem[elem] = data[elem][el]
    return render(request, 'phonee.html', allem)
