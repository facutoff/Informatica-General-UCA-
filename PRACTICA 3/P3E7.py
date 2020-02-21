def calcMed(a,b,c):
    h=a-b
    i=b-c 
    j=c-a
    k=a-c
    l=c-b
    if a>=b>=c and h==i or c>=a>=b and j==h or b>=c>=a and i==j or a>=c>=b and k==l:
        return 'Están igualmente distanciados!'
    else:
        return 'No Están igualmente distanciados'
def main():
    a=int(input('Ingrese el primer número: '))
    b=int(input('Ingrese el segundo número: '))
    c=int(input('Ingrese el tercer número: '))
    print(calcMed(a,b,c))
main()