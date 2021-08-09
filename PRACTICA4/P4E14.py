def triangulo(h):
    for f in range (h):
        for c in range (h,0,-1):
            if f+(c-4)>=(h-1)//2>=f-(c-4):
                print('**',end='')
            else:
                print(' ',end='')
        print()
def main():
    altura=int(input('Ingrese altura: '))
    while altura<5 or altura%2==0: #VALIDACION
        print('ERROR. Ingrese numero IMPAR MAYOR O IGUAL a 5')
        altura=int(input())
    triangulo(altura)
main()