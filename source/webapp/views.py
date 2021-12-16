from django.shortcuts import render


# Create your views here.


def calc_view(request):
    return render(request, 'index.html')


def result_view(request):
    context = {
        'first': int(request.POST.get('first')),
        'second': int(request.POST.get('second')),
        'method': request.POST.get('method'),
    }

    if context['method'] == '+':
        context['total'] = context['first'] + context['second']
        return render(request, 'total.html', context)
    elif context['method'] == '-':
        context['total'] = context['first'] - context['second']
        return render(request, 'total.html', context)
    elif context['method'] == '*':
        context['total'] = context['first'] * context['second']
        return render(request, 'total.html', context)
    else:
        try:
            context['total'] = context['first'] / context['second']
            return render(request, 'total.html', context)
        except ZeroDivisionError:
            context['total'] = "Нельзя делить на ноль"
            return render(request, 'total.html', context)
