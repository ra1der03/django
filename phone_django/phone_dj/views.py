from django.shortcuts import render
from phone_dj.models import Phone


def create_phone(request):
    context, phones = {}, []
    sort = request.GET.get('sort')
    queryset = Phone.objects.all()
    for i in queryset:
        print(i, i.price)
        phones.append(i)
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
    phone, allem, context = [], {}, {}
    queryset = Phone.objects.all()
    for i in queryset:
        phone.append(i)
    for elem in phone:
        if elem.slug == name:
            allem[0] = elem
            break
    return render(request, 'phonee.html', allem)
