def principioFin(texto):
    primera=''
    ultima=''
    
    for x in range(len(texto)): #PRIMERA PALABRA
        if texto[x]==' ':
            break
        elif texto[x]>='a' and texto[x]<='z':
            primera+=texto[x]
        elif texto[x]>='A' and texto[x]<='Z':
            primera+=chr(ord(texto[x])+32)
    for y in range(len(texto)): #SEGUNDA PALABRA
        if texto[-(y+1)]==' ':
            break
        elif texto[-(y+1)]>='a' and texto[-(y+1)]<='z':
            ultima+=texto[-(y+1)]
        elif texto[-(y+1)]>='A' and texto[-(y+1)]<='Z':
            ultima+=chr(ord(texto[-(y+1)])+32)
    if primera==ultima[::-1]: #FUNCION BOOLEANA
        return True

def main():
    texto=input('Ingrese texto: ')
    if principioFin(texto):
        print('El texto cumple la condición.')
    else:
        print('El texto NO cumple la condición.')
main()
