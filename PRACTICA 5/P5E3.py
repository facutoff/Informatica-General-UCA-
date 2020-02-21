def primeraMitad(palabra):
    mitad=int(len(palabra)/2)
    return palabra[:mitad]

def main():
    palabra=input('Ingrese una palabra de longitud par: ')
    for x in range(0,len(palabra)): #VALIDACION
        if palabra[x]>='A'and palabra[x]<='Z' or palabra[x]>='a'and palabra[x]<='z':
            h=1
        else:
            h=2
        while len(palabra)%2!=0 or h!=1: 
           palabra=input('Error. Ingrese una palabra de longitud par: ')
    print('\nLa función ha retornado: ',primeraMitad(palabra))
main()