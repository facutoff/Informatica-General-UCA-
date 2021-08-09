def mult(a,b):
    return a*b
def c1(a):
    return a//1%10
def c2(a):
    return a//10%10
def c3(a):
    return a//100%10
def main():
    a=int(input('Inserte multiplicando: '))
    b=int(input('Inserte multiplicador: '))
    l1=mult(c1(b),a)
    l2=mult(c2(b),a)
    l3=mult(c3(b),a)
    res=mult(a,b)
    print('{:>10d}\n{:7}{:d}\n{:10}\n{:>10}\n+{:>8}-\n{:>8}--\n{:10}\n{:>10}'.format(a,'x',b,'-'*10,l1,l2,l3,'-'*10,res))
main()
    