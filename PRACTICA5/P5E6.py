def palindroma(frase):
    p=''
    for x in range (len(frase)):
        if frase[x]>='A' and frase[x]<='Z':
            lmin=chr(ord(frase[x])+32)
            p=p+lmin
        elif frase[x]>='a' and frase[x]<='z':
            p=p+frase[x]
    if p==p[::-1]: #[::-1]a vuelta un STR
        return True

def main():
    frase=input('Ingrese una frase:')
    if palindroma(frase):
        print('La frase es palíndroma!')
    else:
        print('La frase no es palíndroma')
main()
