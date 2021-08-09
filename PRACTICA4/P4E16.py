def figura(ancho):
    for y in range ((ancho+1)//2):
        for x in range (ancho):
            if y==0 or x==0 or y==(ancho+1)//2-1 or x==ancho-1 or  y<=x-1:
                print('*',end='')
            else:
                print(' ',end='')
        print()
def main():
    ancho=int(input('Ingrese ancho: '))
    while ancho<7 or ancho%2==0: #VALIDACION
        ancho=int(input('ERROR. Ingrese numero IMPAR MAYOR O IGUAL a 7: '))
    figura(ancho)
main()
