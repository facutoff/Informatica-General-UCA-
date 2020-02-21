def primo(cant):
    test=0
    while cant<0:
        print('Error. Ingrese numero positivo.')
        cant=int(input())
    for i in range (1,cant+1):
        if cant%i==0:
            test+=1
    if test==2:
        return True
    elif test!=2:
        return False
    
def main():
    cant=int(input('Ingrese cantidad (numero natural): '))
    num=1
    print('\nPrimos entre 1 y {:d}:'.format(cant))
    for i in range (1,cant+1):
        if primo(i)==True:
            print('\t{:d}'.format(i),end='')
    print('\n\nPrimeros {:d} primos:\n'.format(cant))
    #for i in range (1,cant+1):
    cont=0
    while cont<cant:
        if primo(num)==True:
            print('\t{:d}'.format(num),end='')
            cont+=1
        num+=1
        
main()
           
       
            