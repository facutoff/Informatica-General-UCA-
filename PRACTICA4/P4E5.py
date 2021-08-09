def condicion(num):
    cuarta=num//10%10
    tercera=num//100%10
    segunda=num//1000%10
    primera=num//1000%10
    if cuarta+segunda==tercera+primera:
        return True
    else:
        return False

def main():
    cont=0
    for i in range(1000,10000):
        if condicion(i)==True:
            print('\t {}'.format(i),end='')
            cont+=1
main()
    
    