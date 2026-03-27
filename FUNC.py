def maior (num1, num2):
    if num1>num2:
        print(f"O maior número é {num1}")

    elif num1<num2:
        print(f"O maior número é {num2}")

    else: 
        print("São números iguais")

maior(4, 5)


def retorno (num1, num2):
    if num1>num2:
        return num1

    elif num1<num2:
        return num2

    else: 
        return "são iguais"

parametro1= int(input("defina o primeiro numero :"))
parametro2= int(input("defina o segundo numero :"))


print("testando o retorno")
valor = retorno(parametro1, parametro2)
print(valor)

