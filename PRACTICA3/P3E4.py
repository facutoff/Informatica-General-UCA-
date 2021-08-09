def res(a,b):
    if a>=b:
        return a-b 
    elif b>=a:
        return b-a
def condicion(a,b):
    if a>=b and res(a,b)>=b and res(a,b)<=a:
        return 'SI cumple condicion'
    elif b>=a and res(a,b)<=b and res(a,b)>=a:
        return 'SI cumple condicion'
    else:
        return 'NO cumple condicion'
def main():
    a=int(input('Ingrese numero A: '))
    b=int(input('Ingrese numero B: '))
    print(condicion(a,b))
main()