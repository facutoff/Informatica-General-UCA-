def inserOrd(lst,num):
    pos=0
    while pos<len(lst) and num!='':
        if num>=lst[pos] and num<=lst[pos+1]:
            lst.insert(pos+1,num)
            num=''
        else:
            pos+=1
    return lst

def main():
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
        while len(lista)>1 and n<lista[-1] and n!=0:
            print('ERROR. La lista va de menor a mayor')
            n=int(input())
        lista.append(n)
        n=int(input())
        if n==0:
            print('Lista generada:\n',lista)
            
    num=int(input('\nIngrese valor a insertar: '))
    print('\nLa lista con la inserción ordenada es:\n',inserOrd(lista,num))
main()