#Ejercicio 2                                                          Practica 5
#Dado un string de dos caracteres denominado “extremos” (por ejemplo “<>” o “$$”)
#y
#strings
#en el
#elementos o en caso de qué “palabra” sea vacío, la función deberá retornar un string
#vacío. Desde el programa principal ingresar por teclado los extremos y la palabra,
#invocar a la función y mostrar por pantalla el resultado que retorna la función.
def poner(e,p):
    return e[0]+p+e[1]
def main():
    e=input('Ingrese los extremos: ')
    p=input('Ingrese palabra: ')
    if len(e)!=2:
        print('La función ha retornado una palabra vacía.')
    else:
        print('La función retornó:',poner(e,p))
main()