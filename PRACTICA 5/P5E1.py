def dos(palabra):
    return palabra[-2]+palabra[-1]
def main():
    palabra=input('Ingrese palabra: ')
    if len(palabra)<2:
        print('La función ha retornado una palabra vacía')
    else:
        print(3*dos(palabra))
main()