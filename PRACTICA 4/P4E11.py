def marco(a,b):
    for f in range (a):
        for c in range (b):
            if f==0 or f==a-1 or c==0 or c==b-1: #TODOS SON 'OR'
                print('*',end='')
            else:
                print(' ',end='') #No te olvides del espacio en el print('espacio',end='')
        print('')
def main():
    a=int(input('Ingrese altura: '))
    while a<2: #VALIDACION ALTURA
        print('Error. Ingrese un numero mayor o igual a dos:')
        a=int(input())
    b=int(input('Ingrese base: '))
    while b<2: #VALIDACION BASE
        print('Error. Ingrese un numero mayor o igual a dos:')
        b=int(input('Ingrese base: '))
    marco(a,b)
main()