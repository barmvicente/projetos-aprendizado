import sys

def binario_para_decimal(binario):
    binario = str(binario)
    decimal = 0
    e = 0
    for digito in binario[::-1]:
        digito = int(digito)
        if digito == 1:
            decimal += 2**e
        e += 1
    return decimal

if __name__ == '__main__':
    try:
        binario = sys.argv[1]
    except IndexError:
        print('Passar binario')
    print(binario_para_decimal(binario))
