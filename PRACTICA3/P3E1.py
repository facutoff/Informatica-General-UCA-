def sum(a,b):
    return a+b
def res(a,b):
    return a-b
def div(a,b):
    return a/b
def prod(a,b):
    return a*b

def main():
    n1=int(input('Ingrese numero 1: '))
    n2=int(input('Ingrese numero 2: '))
    o=input('Ingrese operacion (+,-,/,*): ')
    if o=='+':
        print('Resultado:',sum(n1,n2))
    if o=='-':
        print('Resultado:',res(n1,n2))
    if o=='/':
        print('Resultado:',div(n1,n2))
    if o=='*':
        print('Resultado:',prod(n1,n2))
main()
            
    