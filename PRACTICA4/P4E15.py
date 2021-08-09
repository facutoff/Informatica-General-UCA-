def rombo(d):
    for y in range (d):
        for x in range (d):
            if x-y<=d//2<=x+y and y<=d//2 or x-y+1<=d//2<=1-x+y and y>d//2:
                print('* ',end='')
            else:
                print('  ',end='')
        print()
def main():
    diagon=int(input('Ingrese diagonal: '))
    while diagon<5 or diagon%2==0: #VALIDACION
        diagon=int(input('ERROR. Ingrese numero IMPAR MAYOR O IGUAL a 5: '))
    rombo(diagon)
main()