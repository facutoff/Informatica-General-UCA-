import random

def first(a,b):
    return random.randint(a,b)

def main():
    a=int(input('Ingrese limite inferior: '))
    b=int(input('Ingrese limite superior: '))
    h=first(a,b)
    print('Limite inferior {:d}, limite superior {:d}. Numero generado: ​{:d}'.format(a,b,h))
    j=first(h,b)
    print('Limite inferior {:d}, limite superior {:d}. Numero generado: ​{:d}'.format(h,b,j))
    k=first(a,j)
    print('Limite inferior {:d}, limite superior {:d}. Numero generado: ​{:d}'.format(a,j,k))
    
main()
    