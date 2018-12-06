from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    context_dic = {'boldmessage': "Que precisa estar funcionando e no ar ateh segunda feira"}
    return render(request,'rango/index.html',context_dic)

def about(request):
    context_dic = {'text': "Testando..."}
    return render(request,'rango/about.html',context_dic)

def outra_view(request):
    dic = {'text':"Show"}
    return render(request,'rango/about.html',dic)
