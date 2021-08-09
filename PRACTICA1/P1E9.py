print('Ejercicio 9')
n=(int(input('Ingrese num con cantidad impar de cifras (al menos 3): ')))
m=len(str(n))
print('El numero ingresado tiene '+str(m)+' cifras')
ultima=n%10
medio=m//2
central=((n//10**medio))%10
primera=n//10**(m-1)
print('La ultima cifra es '+str(ultima)+' la cifra central es '+str(central)+' y la primera es '+str(primera))
