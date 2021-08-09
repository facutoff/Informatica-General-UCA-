def perfecto(num):
    a=0
    for i in range(1,num):
        if num%i==0:
            a+=i
    if a==num:
        return True
    else:
        return False

def main():
    num=int(input('Ingrese un numero positivo: '))
    while num<0:
        print('Error. Ingrese numero MAYOR a cero')
        num=int(input())
    if perfecto(num)==True:
        print('El numero {:d} es perfecto.'.format(num))
    elif perfecto(num)==False:
        print('El numero {:d} NO es perfecto.'.format(num))
    cont=0
    print("Los primeros cuatro numeros perfectos son:\n")
    if cont<=4:
        for n in range (1,10000):
            if perfecto(n)==True:
                cont+=1
                print('\t{:d}'.format(n),end='')
                
main()
            
        
            