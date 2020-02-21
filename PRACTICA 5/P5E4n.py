def sep(caracter):
    return ord(caracter) not in range(ord('A'),ord('z')+1)
#'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoópqrstuvwxyz'

def palabra(pal):
    pos=0
    while pos<len(pal):
        while pos<len(pal) and sep(pal[pos]):
            pos+=1
        ini=pos
        while pos<len(pal) and not sep(pal[pos]):
            pos+=1
        fin=pos
        return pal[ini:fin]

def mayus(palabra):
    for x in range(len(palabra)):
        if palabra[x]>='A' and palabra[x]<='Z':
            palabra=palabra[:x]+chr(ord(palabra[x])+32)+palabra[x+1:]
    return palabra

def principioFin(txt):
    pal=mayus(palabra(txt))
    pal2=mayus(palabra(txt[::-1]))
    if pal==pal2[::-1]:
        return True

def main():
    texto=input('Ingrese texto: ')
    if principioFin(texto):
        print('El texto cumple la condición.')
    else:
        print('El texto NO cumple la condición.')
main()