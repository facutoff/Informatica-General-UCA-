def main():
    n1=int(input('Ingrese n1: '))
    n2=int(input('Ingrese n2: '))
    n3=int(input('Ingrese n3: '))
    if n1>=n2 and n2>=n3:
        print('Los números ordenados en forma ascendente son:\n{:d}\n{:d}\n{:d}'.format(n1,n2,n3))
    if n2>=n1 and n1>=n3:
        print('Los números ordenados en forma ascendente son:\n{:d}\n{:d}\n{:d}'.format(n2,n1,n3))
    if n2>=n3 and n3>=n1:
        print('Los números ordenados en forma ascendente son:\n{:d}\n{:d}\n{:d}'.format(n2,n3,n1))
    if n1>=n3 and n3>=n2:
        print('Los números ordenados en forma ascendente son:\n{:d}\n{:d}\n{:d}'.format(n1,n3,n2))
    if n3>=n1 and n1>=n2:
        print('Los números ordenados en forma ascendente son:\n{:d}\n{:d}\n{:d}'.format(n3,n1,n2))
    if n3>=n2 and n2>=n1:
        print('Los números ordenados en forma ascendente son:\n{:f}\n{:f}\n{:f}'.format(n3,n2,n1))
main()