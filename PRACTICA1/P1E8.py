print('Ejercicio 8')
print(' ')
seg=int(input('Ingrese los segundos: '))
print(' ')

dia=(seg//86400)
hora=(seg//3600-dia*24)
min=((seg-dia*86400-hora*3600)//60)
seg1=((seg-dia*86400-hora*3600-min*60))

print(str(dia)+' dia(s), '+str(hora)+' hora(s), '+str(min)+' minuto(s), '+str(seg1)+' segundo(s).')

