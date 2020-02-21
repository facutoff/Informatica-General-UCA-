def factorial(n):
    factorial=1
    if n==0:
        factorial=1
    else:
        for i in range(0,n):
            if i!=n:
                factorial=factorial*(n-i)
    return factorial
def main():
    n=int(input('Ingrese un número entero: '))
    while n<0:
        print('No se puede calcular el factorial de un número negativo.')
        n=int(input('Ingrese un número entero: '))
    print('El factorial de {:d} es: {}.'.format(n,factorial(n)))
main()
        