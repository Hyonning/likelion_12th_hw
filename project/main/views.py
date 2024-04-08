from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'generation': 12,
        'MTV': ['model', 'templates', 'view'],
        'info':{'model': '데이터', 'templates': '보여지는 부분', 'view': '요청에 따른 적절한 로직 수행'},
        'members':{'request','url conf', 'view','model','template','response'}
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request) :
    return render(request, 'main/secondpage.html')

