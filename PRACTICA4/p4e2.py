def main():
    num=int(input('Ingrese numeros enteros positivos (finalice con 0):\n'))
    while num<0:
        print('Error. Ingrese numero mayor a 0:')
        num=int(input())
    if num>0:
        max=num
        min=num
        while num!=0:
            if max<num:
                max=num
            elif num<0:
                print('Error. Ingrese numero mayor a 0:')
            elif min>num:
                min=num
            num=int(input())
    if num==0:
        print('El menor es {:d} y el mayor {:d}'.format(min,max))
main()
        
            