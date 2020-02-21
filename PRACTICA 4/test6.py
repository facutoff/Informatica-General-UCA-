def aBinario(n):
    binario=0
    potencia=0
    while n!=0:
        r=n%2
        n=n//2
        binario=binario+(r*10**potencia)
        potencia=potencia+1
    return binario   

def main():
    num=int(input('Ingrese un numero decimal: '))
    cifras=len(str(num))
    ##validacion
    while not ((num>0 and num<1000) or cifras<4):
        print('ERROR. Ingrese un numero decimal positivo y de 3 cifras.')
        num=int(input())
    ##
    print()
    print('Numero en binario: {}.'.format(aBinario(num)))

main()