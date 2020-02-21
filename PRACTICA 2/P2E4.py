import math

def areacirc(d):
    e=math.pow((d/6),2)*math.pi*2
    r=math.pow(((d-(d/3))/2),2)*math.pi
    return e+r

def areacuad(l):
    return math.pow(l,2)

def areanegra(d):
    return areacuad(d)-areacirc(d)
    
def main():
    d=int(input('Ingrese lado: '))
    a=areanegra(d)/areacuad(d)*100
    print('El area negra es {:2.2f} y es un {:2.2f}% del total del cuadrado'.format(a,areanegra(d)))
main()
