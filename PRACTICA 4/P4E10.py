def rectangulo(b,a):
    for f in range (a): 
        for c in range (b): 
            print('* ',end='')
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
    rectangulo(b,a)
main()