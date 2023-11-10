from django.shortcuts import render, redirect,HttpResponse
from app0.models import Message

def top(request):
    return render(request, 'top-col-center.html')

def profile(request):
    return render(request, 'profile.html')

def memes(request):
    return render(request, 'memes.html')

def free(request):
    if (request.method == 'GET'):
        queryset = Message.objects.all().order_by('-id')
        return render(request,'free.html',{'msgs':queryset})
    else:
        mbti=request.POST.get('type')
        message=request.POST.get('content')
        if(mbti!='' and message!=''):
            Message.objects.create(type=mbti,content=message)
            return redirect('/mbti/free/')
        else:
            return HttpResponse('不要提交空白啊！')

def show(request,type):
    title={ 'type': type }
    match type:
        case 'intj':
            return render(request,'eachcard/intj.html',title)
        case 'intp':
            return render(request, 'eachcard/intp.html',title)
        case 'entj':
            return render(request, 'eachcard/entj.html',title)
        case 'entp':
            return render(request, 'eachcard/entp.html',title)
        case 'infj':
            return render(request,'eachcard/infj.html',title)
        case 'infp':
            return render(request, 'eachcard/infp.html',title)
        case 'enfj':
            return render(request, 'eachcard/enfj.html',title)
        case 'enfp':
            return render(request, 'eachcard/enfp.html',title)
        case 'istj':
            return render(request,'eachcard/istj.html',title)
        case 'isfj':
            return render(request, 'eachcard/isfj.html',title)
        case 'estj':
            return render(request, 'eachcard/estj.html',title)
        case 'esfj':
            return render(request, 'eachcard/esfj.html',title)
        case 'istp':
            return render(request,'eachcard/istp.html',title)
        case 'isfp':
            return render(request, 'eachcard/isfp.html',title)
        case 'estp':
            return render(request, 'eachcard/estp.html',title)
        case 'esfp':
            return render(request, 'eachcard/esfp.html',title)
