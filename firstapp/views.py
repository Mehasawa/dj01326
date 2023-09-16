from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contacts(request):
    mas = ['cat','dog','pig','bear']
    data = {'phone':'1-234-5678','adr':'Pushkin street','num':1, 'spisok':mas}
    return render(request, 'contacty.html',data)