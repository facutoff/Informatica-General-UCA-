def main():
    c=0
    while c<5:
        a=int(input('Ingrese numero entero: '))
        if a%2==0 and a%4!=0:
            c+=1
            print('Numero Par. Total de numeros pares ingresados: {:d}'.format(c))
        elif a%4==0:
            c+=1
            print('Numero Par. Tambien es multiplo de 4. Total de numeros pares ingresados: {:d}'.format(c))
    print('\nFIN')
main()
    
    