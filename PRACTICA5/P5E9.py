def sep(caracter):
    if ord(caracter) not in range(ord('A'),ord('z')+1):
        return True
        
def Cant(txt):
    pos=0
    cant=0
    while pos<len(txt):
        while pos<len(txt) and sep(txt[pos]):
            pos+=1
        ini=pos
        while pos<len(txt) and not sep(txt[pos]):
            pos+=1
        fin=pos
        pal=txt[ini:fin]
        cant+=1
    return cant
        
def larga(txt):
    pos=0
    palabra=''
    while pos<len(txt):
        while pos<len(txt) and sep(txt[pos]):
            pos+=1
        ini=pos
        while pos<len(txt) and not sep(txt[pos]):
            pos+=1
        fin=pos
        if fin-ini>len(palabra):
            palabra=txt[ini:fin]
    return palabra

def corta(txt):
    pos=0
    palabra='INICIOOO0000OOO000OOO000OOO000OOO000OOO000OOO'
    while pos<len(txt):
        while pos<len(txt) and sep(txt[pos]):
            pos+=1
        ini=pos
        while pos<len(txt) and not sep(txt[pos]):
            pos+=1
        fin=pos
        if fin-ini<len(palabra):
            palabra=txt[ini:fin]
    return palabra


def main():
    txt=input('Ingrese un texto: ')
    print('El texto tiene {} palabras, la de mayor longitud es “{}” y la de menorlongitud es “{}”'.format(Cant(txt),larga(txt),corta(txt)))
main()
        