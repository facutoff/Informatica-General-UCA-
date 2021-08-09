def sep(caracter):
    caracter not in range(ord('A'),ord('z')+1)
def palabra(t,c):
    pos=0
    while pos<len(t):
        while pos<len(t) and sep(t[pos]):
            pos+=1
        ini=pos
        while pos<len(t) and not sep(t[pos]):
            pos+=1
        fin=pos
        palabra=t[ini:fin]
        l=0
        while len(c)==len(palabra):
            for i in range (len(c)):
                if palabra[i] in c:
                    l+=1
            if l==len(c):
                return True
       
def main():
    t=input('Ingrese el texto: ')
    c=input('Ingrese la palabra: ')
    if palabra(t,c):
        print('Se cumple con la condición')
    else:
        print('No se cumple con la condición')
main()
                
        