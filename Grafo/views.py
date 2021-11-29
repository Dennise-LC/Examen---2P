from django.shortcuts import render
import random
import math

# Create your views here.
OP = {'Umbral': lambda x,u: 'Si' if x > u  else 'No'}

def home(request):
    return render(request,'h.html',{'D':[x for x in range(1,20)]})

def p2(request):
    Cv = 0
    Dv = 0
    if request.method == 'GET':
        Cv = int(request.GET.get('CV'))
        Dv = int(request.GET.get('DV'))
        print(Dv,Cv)
    GeneraDatos(Cv,Dv)
    return render(request,'probando.html')


def p3(request):
    U = 0
    if request.method == 'GET':
        U = float(request.GET.get('umbral'))
    Enviar = Grafo(U)
    return render(request,'probando.html',{'esta': Enviar[0],'Nodos':Enviar[1],'Conexion':Enviar[2]})

def GeneraDatos(dv,cv):
    file = open('Database.txt','w')
    f = [dv,cv]
    for c in range(int(f[0])):
        for x in range(int(f[1])):
            if x != int(f[1])-1:
                file.write(str(random.randrange(0, 100))+ ',')
            else:
                file.write(str(random.randrange(0, 100)))
        if c != int(f[0])-1:
            file.write('\n')
    file.close()

def Grafo(U):
    Matriz  = [[int(c) for c in x.split(',')]for x in open('Database.txt','r').read().split('\n')]
    Nodos = []
    Unicos = []
    N = []
    for x in range(len(Matriz)):
        for c in range(len(Matriz)):
            if c >= x:
                f = math.dist(Matriz[x],Matriz[c])
                N.append(['R'+str(x+1),'R'+str(c+1),f,OP['Umbral'](f,float(U))])
                if f > U :
                    Nodos.append(str(x+1))
                    Nodos.append(str(c+1))         
    for x in Nodos:
        if x not in Unicos:
            Unicos.append(x)
    R = [N,','.join(Unicos),','.join(Nodos)]                 
    return R


