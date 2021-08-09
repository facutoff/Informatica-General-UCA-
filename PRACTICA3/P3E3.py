def signo(n):
    if n>0:
        return 'positivo'
    elif n==0:
        return 'cero'
    elif n<0:
        return 'negativo'
        
def tnum(n):
    entero=int(n)
    if entero==n:
        if entero>0:
            return 'entero natural'
        elif entero<0:
            return 'entero'
    else:
        return 'real'
    
def main():
    n=float(input('Ingrese numero: '))
    s=signo(n)
    r=tnum(n)
    print('El número es {} y {}'.format(s,r))
main()
    