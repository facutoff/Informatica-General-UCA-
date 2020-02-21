import random

def cargarListaAleat():
    n0=int(input('INGRESE VALOR 1: '))
    n1=int(input('INGRESE VALOR 2: '))
    n2=int(input('INGRESE VALOR 3: '))
    lista=[]
    if n0>n1:
        for i in range (0,n2):
            lista.append(random.randint(n1,n0))
    if n1>n0:
        for i in range (0,n2):
            lista.append(random.randint(n0,n1))
    return lista

def minVal(lista):
    #n=lista[len(lista)]
    #for n in range (0,len(lista)):
     #   if lista[n]<m:
      #      m=lista[n]
       # else:
        #    None
    return min(lista)   
def maxVal(lista):
    #l=min(lista)
    #for i in range (0,len(lista)):
    #    while lista[i]<l:
    #        l=lista[n]
    return max(lista)   
            
def main():
    l=cargarListaAleat()
    print(l)
    print(maxVal(l))
    print(minVal(l))
main()
   