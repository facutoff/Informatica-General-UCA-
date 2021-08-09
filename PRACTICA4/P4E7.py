def main():
    nota=int(input('Ingrese nota: '))
    while nota<0 or nota>10:
        nota=int(input('ERROR. Ingrese nota valida (1 a 10): '))
    total=0
    aplazos=0
    aprobados=0
    promocionados=0
    prom=nota
    while nota!=0:
        if nota>=1 and nota<=10:
            total+=1
            prom+=nota
            if nota>=4 and nota<=7:
                aprobados+=1
            elif nota>7:
                promocionados+=1
            elif nota<4:
                aplazos+=1
        nota=int(input('Ingrese nota: '))
        while nota<0 or nota>10:
            nota=int(input('ERROR. Ingrese nota valida (1 a 10): '))
    print('Cantidad de aplazos: {:d} ({:.2f}%)'.format(aplazos,aplazos/total*100))
    print('Cantidad de aprobados: {:d} ({:.2f}%)'.format(aprobados,aprobados/total*100))
    print('Cantidad de promocionados: {:d} ({:.2f}%)'.format(promocionados,promocionados/total*100))
    print('Promedio general: {:.2f}'.format(prom/total))
main()
    