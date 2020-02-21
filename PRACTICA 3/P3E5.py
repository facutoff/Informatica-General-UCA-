def fecha(d,m,a):
    if a%4==0 and m==2 and d>=0 and d<=29:
        return 'La fecha es correcta.'
    elif a%4!=0 and m==2 and d>=0 and d<=28:
        return 'La fecha es correcta.'
    elif m>=1 and m<=12 and m!=2 and m%2==0 and d>=1 and d<=30:
        return 'La fecha es correcta.'
    elif m>=1 and m<=12 and m!=2 and m%2!=0 and d>=1 and d<=31:
        return 'La fecha es correcta.'
    else:
        return 'La fecha es incorrecta.'
def main():
    d=int(input('Ingrese dia: '))
    m=int(input('Ingrese mes: '))
    a=int(input('Ingrese ano: '))
    print(fecha(d,m,a))
main()