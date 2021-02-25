from django.shortcuts import render


def toys(request):
    with open('d:/python practice/testtask/toys.yaml') as file:
        context = {'data': [i for i in file.readlines()]}
    return render(request, 'toys.html', context=context)

# def games(request):
