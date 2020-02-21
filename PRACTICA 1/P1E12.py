def suma(a,b,c):
    return a+b+c

def main():
    a=int(input('Ingrese numero: '))
    b=int(input('Ingrese numero: '))
    c=int(input('Ingrese numero: '))
    res=suma(a,b,c)
    print('{:=10d}\n{:=10d}\n{:=10d}\n----------\n{:=10d}'.format(a,b,c,res))
main()