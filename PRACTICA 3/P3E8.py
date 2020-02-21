def PromGral(a,b,c):
    return (a+b+c)/3
def PromRec(a,b,c,d):
    return (a+b+c+d)/4
def main():
    n1=float(input('Ingrese la nota del primer parcial: '))
    n2=float(input('Ingrese la nota del segundo parcial: '))
    n3=float(input('Ingrese la nota del tercer parcial: '))
    if PromGral(n1,n2,n3)>=7:
        print('El alumno promociono la materia con un promedio de {:.2f}.'.format(PromGral(n1,n2,n3)))
    elif PromGral(n1,n2,n3)<7 and n1>4 and n2>4 and n3>4:
        print('Promedio general {:.2f}\nEl alumno debera rendir final'.format(PromGral(n1,n2,n3)))
    elif n1<4 or n2<4 or n3<4:
        r=(float(input('Ingrese la nota del recuperatorio: ')))
        if r>=4:
            print('Promedio general {:.2f}\nEl alumno debera rendir final'.format(PromRec(n1,n2,n3,r)))
        else:
            print('Promedio general {:.2f}\nEl alumno NO aprobo la materia'.format(PromRec(n1,n2,n3,r)))
main()
    
    
    