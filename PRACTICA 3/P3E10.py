def multa(v,p,t):
    if t=='N' and t=='n':
        if v<p and v>p/2:
            return 'No recibe multa'
        elif v>p and v<p*1.15:
            return 'Advertencia'
        elif v>p*1.15:
            return 'Recibe multa por exceso de velocidad'
    else:
        if v<p/2 and v>p/2-p/2*0.15:
            return 'Advertencia'
        elif v<p/2-p/2*0.15:
            return 'Recibe multa por entorpecer el tránsito'
        else:
            return 'No recibe multa'
def main():
    v=float(input('Velocidad del vehículo: '))
    p=float(input('Velocidad máxima: '))
    t=input('Emergencia (s/n): ')
    print('\n{}'.format(multa(v,p,t)))
main()
    