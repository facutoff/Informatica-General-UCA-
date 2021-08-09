def triangulo(b):
    for f in range ((b+1)//2):
        for c in range (b):
            if c-f<=((b-1)//2)<=c+f:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
def main():
    base=int(input('Ingrese base: '))
    while base<3 or base%2==0: #VALIDACION
        print('ERROR. Ingrese numero IMPAR MAYOR O IGUAL a 3')
        base=int(input())
    triangulo(base)
main()
