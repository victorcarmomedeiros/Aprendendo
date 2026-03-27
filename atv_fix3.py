from socket import NI_NUMERICHOST


seletor = int(input("escolha o exercicio: "))

if seletor == 1:
    print("exercicio 1")
    n = range(1, 11)
    print(list(n))

elif seletor == 2:
    print("exercicio 2")
    tabuada = 0
    while tabuada <=10:
        num = 0
        while num <=10:
            total = num * tabuada
            print(f"{num} x {tabuada} = {total}")
            num += 1
        tabuada += 1


elif seletor == 3:
    print("exercicio 3 numeros pares até 20")
    for numeros in range(1, 21):
        if numeros % 2 == 0:
            print(numeros)
    

else:
    print("exercicio invalido")
