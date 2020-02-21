def estaEnLista(numero,lista):
    if numero in lista:
        return True
    else:
        return False
    
def cargarLista():
    print('Ingresar numeros,o 0 (cero ) para terminar: ')
    n=int(input())
    lista=[] 
    while n!=0:
        while n<0 and n!=0:
            print('Error, numero NO positivo.')
            n=int(input())
        while estaEnLista(n,lista) and n!=0:
            print('Error, número repetido.')
            n=int(input())
        lista.append(n)
        n=int(input())
    if n==0:
        return lista   


def main():
    lst=cargarLista()
    print('La lista contiene:\n',lst)
main()