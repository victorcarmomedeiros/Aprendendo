def triplo (num1):
    total = num1 * 3
    return total

valor = triplo(2)
print(valor)

def par (num1):
    par = num1 %2

    if par > 0:
        print (False)
    else:
        print (True)

par(3)
par(2)

def maior (num1, num2):
    if num1>num2:
        print(f"O maior número é {num1}")

    elif num1<num2:
        print(f"O maior número é {num2}")

    else: 
        print("São números iguais")

maior(4, 5)



def somar (lista):
    soma = 0

    for numero in lista:
        soma += numero

    print(soma)

numeros = [1, 2, 3, 4, 10]
somar(numeros)
