def triangulo(catetos):
    for f in range (catetos):
        for c in range (catetos):
            if c<=f:
                print('*',end='')
        print('') #Debe ir fuera del 'for c' (columna)
def main():
    catetos=int(input('Ingrese base: '))
    while catetos<3: #VALIDACION
        print('ERROR. Ingrese numero MAYOR o IGUAL a tres')
        catetos=int(input())
    triangulo(catetos)
main()
