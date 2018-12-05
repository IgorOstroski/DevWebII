from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    context_dic = {'boldmessage': "Que precisa estar funcionando e no ar ateh segunda feira"}
    return render(request,'rango/index.html',context_dic)

# Create your views here.
