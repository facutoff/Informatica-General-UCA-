def cargarLstAlu():
    dni=int(input('Ingrese DNI: '))
    lst=[]
    lstAlu=[]
    while dni!=0:
        lst.append(dni)
        nombre=input('Ingrese nombre: ')
        lst.append(nombre)
        edad=int(input('Ingrese edad: '))
        lst.append(edad)
        dni=int(input('Ingrese DNI: '))
        lstAlu.append(lst)
        lst=[]
    return lstAlu

def ordenarAluXDNI(lstAlu):
    for i in range (len(lstAlu)-1):
        for j in range (i+1,len(lstAlu)):
            if lstAlu[i][0]>lstAlu[j][0]:
                temp=lstAlu[i]
                lstAlu[i]=lstAlu[j]
                lstAlu[j]=temp
    return lstAlu
    
def main():
    lst=cargarLstAlu()
    print(ordenarAluXDNI(lst))
main()
    