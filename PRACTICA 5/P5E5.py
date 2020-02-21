def mitad(texto,c):
    m=c//2
    return texto[m:]+texto[:m]
def main():
    texto=input('Ingrese un texto: ')
    c=len(texto)
    while c%2!=0 or c<2:
        texto=input('Error. Ingrese un texto: ')
        c=len(texto)
    print('\nLa función ha retornado: '+mitad(texto,c))
main()