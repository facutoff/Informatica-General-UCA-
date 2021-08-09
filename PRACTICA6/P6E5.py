import random

def cargarLista():
    print('Ingresar numeros,o 0 (cero ) para terminar: ')
    n=int(input())
    lista=[] 
    while n!=0:
        while n<0 and n!=0:
            print('Error, numero NO positivo.')
            n=int(input())
        while n in lista and n!=0:
            print('Error, número repetido.')
            n=int(input())
        lista.append(n)
        n=int(input())
    if n==0:
        return lista
    
def cambiaLista(lst,a,b):
    for i in range(len(lst)):
        if lst[i] not in range(a,b+1):
            lst[i]=random.randint(a,b+1)
    return lst

def main():
    lista=cargarLista()
    print('Lista generada:\n',lista)
    a=int(input('\nIngrese limite a del rango: '))
    b=int(input('Ingrese limite b del rango: '))
    print('\nLa lista modificada es:\n',cambiaLista(lista,a,b))
main()