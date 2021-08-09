import random

def rend(a,b):
    return random.randint(a,b)

def main():
    r=rend(0,1)
    a=(input('Ingrese opcion 1 vestimenta: '))*r
    b=(input('Ingrese opcion 2 vestimenta: '))*(1-r)
    c=(input('Ingrese opcion 1 plato: '))*(1-r)
    d=(input('Ingrese opcion 2 plato: '))*r
    e=(input('Ingrese opcion 1 bebida: '))*(1-r)
    f=(input('Ingrese opcion 2 bebida: '))*r
    r=rend(0,1)
    print('Cena al azar:'+a+b,c+d,e+f)

main()
    

    
    
    