def mayus(texto):
    caracter=0
    for x in range(len(texto)): #PRIMERA PALABRA
#        if texto[0]>='a' and texto [0]<='z':
 #           lm=chr(ord(texto[0])-32)
  #          texto=lm+texto[1:]
   #         caracter+=1
        if texto[x-1]==' ' and texto[x]>='a' and texto [x]<='z':
                lm=chr(ord(texto[x])-32)
                texto=texto[:x]+lm+texto[x+1:]
                caracter+=1
    return texto
def main():
    texto=input('Ingrese un texto: ')
    print(mayus(texto))
main()