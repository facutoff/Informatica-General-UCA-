import math
def aBinario(num):
    binario=0
    p=0
    while num!=0:
        c=num%2
        num=num//2
        binario+=(c*math.pow(10,p))
        p+=1
    return int(binario)
def main():
    num=int(input('Ingrese numero a convertir: '))
    while num<0 or num>1000:
        print('Error, ingrese numero positivo de 3 cifras: ')
        num=int(input())
    print('El numero en binario es: {:d}.'.format(aBinario(num)))
main()

