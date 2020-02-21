def justificando(a,b):
    return '{:{alinear}{con}}'.format(a,alinear='>',con=b-2)

def main():
    fra=input('Ingrese la frase: ')
    ancho=int(input('Ingrese el ancho total a ser usado: '))
    print('"'+justificando(fra,ancho)+'"')
main()
    
