import math

def calcrad(a,b):
    return math.pow(a,1/b)

def main():
    rad=int(input('Ingrese radicando (numero real): '))
    ind=int(input('Ingrese indice (numero natural): '))
    print('La raiz ',ind,' de ',rad,' es: ',calcrad(rad,ind))

main()