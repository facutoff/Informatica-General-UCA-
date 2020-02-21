def par(a):
    if a%2==0:
        return 'menor'
    else:
        return 'mayor'
def mm(a,b):
    if par(a)=='menor' and b<a or par(a)=='mayor' and b>a:
        return 'Correcto!'
    #elif par(a)=='mayor' and b>a:
#        return 'Correcto!'
    else:
        return 'Incorrecto!'
def main():
    a=int(input('Ingrese numero entero positivo: '))
    b=int(input('Ingrese numero {} que {:d}: '.format(par(a),a)))
    print(mm(a,b))
main()
        
