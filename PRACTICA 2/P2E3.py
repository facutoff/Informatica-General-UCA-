def paridad(z):
    a=(z//1%10)
    c=(z//10%10)
    d=(z//100%10)
    e=(z//1000%10)
    f=(z//10000%10)
    g=(z//100000%10)
    h=(z//1000000%10)
    i=(z//10000000%10)
    return (a+c+d+e+f+g+h+i)%2

def main():
    z=int(input('Ingrese numero binario (8b max): '))
    print('El bit de paridad generado es:''{:d}'.format(paridad(z)))
    
main()
