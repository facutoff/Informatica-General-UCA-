def crearFila(ancho):
    return '{:{caracteres}}'.format('*'*ancho,caracteres=ancho)
def crearRectangulo(ancho,alto):
    return alto*'{}\n'.format(crearFila(ancho))
def main():
    ancho=int(input('Ingrese ancho: '))
    alto=int(input('Ingrese alto: '))
    print(crearRectangulo(ancho, alto))
main()