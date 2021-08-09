print('Ejercicio 10')
b=int(input('Ingrese numero binario (5 bits max): '))
n=len(str(b))
z=b//10000%10*2**4
x=b//1000%10*2**3
c=b//100%10*2**2
v=b//10%10*2**1
n=b%10*2**0
t=x+c+v+n+z
print('Número en decimal: '+str(t))

