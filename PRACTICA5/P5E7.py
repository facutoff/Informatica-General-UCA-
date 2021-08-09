def verificar(largo,corto):
    contador=0
    for x in range(len(largo)):
        palabra=largo[x:x+len(corto)]
        if palabra==corto:
            contador+=1
    return contador
def main():
    largo=input('Ingrese el texto largo: ')
    corto=input('Ingrese el texto corto: ')
    print('El texto corto se encontró {:d} veces en el texto largo'.format(verificar(largo,corto)))
main()