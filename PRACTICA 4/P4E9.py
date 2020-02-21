def capicua(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
    
def main():
    n=int(input('Ingrese numero: '))
    while len(str(n))>9 or n<0:
        print('Ingrese un numero POSITIVO de hasta 9 cifras')
        n=int(input())
    print(capicua(n))
main()
