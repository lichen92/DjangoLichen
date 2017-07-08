from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'num_index':'2', 'num':'0'}
    return render(request, 'ttsx_goods/index.html', context)


