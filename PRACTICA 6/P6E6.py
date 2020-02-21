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
    
def ordenarLst(lista):
    for i in range (len(lista)-1):
        for j in range (i+1,len(lista)):
            if lista[i]>lista[j]:
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista
def main():
    lista=cargarLista()
    print('Lista generada:\n',lista)
    print('\nLa lista ordenada es: \n',ordenarLst(lista))
main()