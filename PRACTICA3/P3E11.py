def mensaje(u,c,t):
    p1=t//5
    p2=t%5+(p1-c)*5
    if p1<=c and p2==0:
        return '\nEs posible cubrir el tendido.\nSugerencia:\n{:d} unidades de caño de 5 metros'.format(t//5)
    elif p1<=c and p2>0:
        return '\nEs posible cubrir el tendido.\nSugerencia:\n{:d} unidades de caño de 5 metros\n{:d} unidades de caño de 1 metro'.format(p1,p2)
    elif p1>=c and p2>0:
        return '\nEs posible cubrir el tendido.\nSugerencia:\n{:d} unidades de caño de 5 metros\n{:d} unidades de caño de 1 metro'.format(c,p2)
    elif u+c>=t or u<p2 or p2<=0:
        return 'No es posible cubrir el tendido.'
def main():
    u=int(input('Cantidad de caños de 1 metro: '))
    c=int(input('Cantidad de caños de 5 metros: '))
    t=int(input('Metros totales a cubrir: '))
    print(mensaje(u,c,t))
main()