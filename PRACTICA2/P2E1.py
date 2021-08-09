def calcp (a,b,c):
    return (a+b+c)/2

def calcarea (a,b,c,d):
    return (d*(d-a)*(d-b)*(d-c))**(1/2)

def main():
    a=int(input('Ingrese lado 1: '))
    b=int(input('Ingrese lado 2: '))
    c=int(input('Ingrese lado 3: '))
    d=calcp(a,b,c)
    print('El area del triangulo es: ',calcarea(a,b,c,d))
    
main()
    


    