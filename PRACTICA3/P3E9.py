def bono(s):
    if s>2000:
        return s*0.15
    else:
        return s*0.2
def plus(s,c,h):
    if c==7 or c==8 or c==9:
        return plusC(s,c)
    else:
        return plusC(s,c)+plusH(s,h)
def plusH(s,h):
    if h=='s':
        return s*0.05
    else:
        return 0
def plusC(s,c):
    if c==1 or c==2 or c==3:
        return s*0.10
    elif c==4 or c==5 or c==6:
        return s*0.12
    elif c==7 or c==8 or c==9:
        return s*0.2
def main():
    s=float(input('Ingrese sueldo base: '))
    h=input('Tiene hijos (s/n)?: ')
    c=int(input('Ingrese categoría (1 - 9): '))
    print('\nEl sueldo total será de ${:.2f}'.format(s+bono(s)+plus(s,c,h)))
main()
    