def cargarConjuntos():
    lista=[]
    print('Ingresar numeros,o 0 (cero ) para terminar: ')
    numero=int(input())
    while numero!=0:
        while numero<0 and numero!=0:
            print('Error, numero NO positivo.')
            numero=int(input())
        while numero in lista and numero!=0:
            print('Error, número repetido.')
            numero=int(input())
        lista.append(numero)
        numero=int(input())
    return lista
    
def union(a,b):
    c=[]
    for n in range (0,len(a)):
        if a[n] not in b and a[n] not in c:
            c.append(a[n])
    for n in range (0,len(b)):
        if b[n] not in a and b[n] not in c:
            c.append(b[n])
    print('Union=',c)
    
def interseccion(a,b):
    d=[]
    for n in range (0,len(b)):
        if b[n] in a:
            d.append(b[n])
    print('Intersección = ',d)
    
def diferencia(a,b):
    d=[]
    for n in range (0,len(a)):
        if a[n] not in b:
            d.append(a[n])
    print('Diferencia (A-B) =',d)
    
#def diferenciaSimétrica(a,b):
 #   d=[]
  #  for n in range (0,len(a)):
   #     if 
    #print('Diferencia Simétrica =',d)

def main(): #MAIN
    print('1. CARGAR CONJUNTOS\n2. UNION\n3. INTERSECCION\n4. DIFERENCIA (A-B)\n5. DIFERENCIA SIMÉTRICA\n6. SALIR')
    n=int(input('Ingrese el valor de la opción: '))
    while n!=6:
        while n==1:
            l1=cargarConjuntos()
            l2=cargarConjuntos()
            print('CONJUNTOS CARGADOS:\n{}\n{}\n'.format(l1,l2))
            n=int(input('Ingrese el valor de la opción: '))
        while n==2:
            union(l1,l2)
            n=int(input('Ingrese el valor de la opción: '))
        while n==3:
            interseccion(l1,l2)
            n=int(input('Ingrese el valor de la opción: '))
        while n==4:
            diferencia(l1,l2)
            n=int(input('Ingrese el valor de la opción: '))
        while n==5:
            deferenciaSimétrica(l1,l2)
            n=int(input('Ingrese el valor de la opción: '))
main()
