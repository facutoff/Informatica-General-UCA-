print('Ejercicio 11')
a=int(input('Ingrese número decimal (5 cifras max): '))
t1=a//8
t2=t1//8
t3=t2//8
t4=t3//8
t5=t4//8
t6=t5//8
t7=t6//8
d1=a%8
d2=t1%8
d3=t2%8
d4=t3%8
d5=t4%8
d6=t5%8
d7=t6%8
print('Numero en octal: '+str(d7)+str(d6)+str(d5)+str(d4)+str(d3)+str(d2)+str(d1))
