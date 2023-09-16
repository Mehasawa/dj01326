from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contacts(request):
    mas = ['cat','dog','pig','bear']
    data = {'phone':'1-234-5678','adr':'Pushkin street','num':1, 'spisok':mas}
    return render(request, 'contacty.html',data)

def month(req,id):
    k1 = ['январь','февраль','март']
    k2 = ['Василий','Михаил','Петр']
    k3 = ['img/rt1.jpg','img/rt2.jpg','img/222.gif']
    data = {'month':k1[id],'name':k2[id],'pic':k3[id]}
    return render(req, 'rm.html',data)