print("Bem vindo para a terceira lista de exercicios de linguagem de programação")

seletor = int(input("Selecione o exercicio que deseja ver em execução: "))

#ETAPA ENTRADA E PROCESSAMENTO
if seletor == 1:
    num_int = float(input("Informe o número que deseja descobrir o dobro: "))
    print(f"O dobro de {num_int} é {num_int * 2}")

elif seletor == 2:
    number = float(input("Informe um número inteiro: "))
    number2 = float(input("Informe outro número inteiro: "))
    print(f"A soma de {number} e {number2} é {number + number2}")

elif seletor == 3:
    media1 = int(input("Informe a primeira nota: "))
    media2 = int(input("Informe a segunda nota: "))
    print(f"A média de {media1} e {media2} é {(media1 + media2) / 2}")

elif seletor == 4:
    raio = float(input("Informe o raio do círculo: "))
    area = 3.14 * raio ** 2
    print(f"A área do círculo com raio {raio} é {area}")

elif seletor == 5:
    lado = float(input("Informe o lado do quadrado: "))
    area = lado ** 2
    perimetro = 4 * lado
    print(f"A área do quadrado com lado {lado} é {area} e o perímetro é {perimetro}")

elif seletor == 6:
    real= float(input("Informe um valor em reais: "))
    dolar = real / 5.32
    print(f"O valor de R${real} em dólares é ${dolar}")

elif seletor == 7:
    idade = int(input("Informe sua idade: "))
    print(f"Sua idade em dias é {idade * 365}")


elif seletor == 8:
    base = float(input("Informe a base: "))
    altura = float(input("Informe a altura: "))
    print(f"A área do triângulo com base {base} e altura {altura} é {base * altura / 2}")

elif seletor == 9:
    preco = float(input("Informe o preço do produto: "))
    print(f"O preço do produto com desconto de 10% é {preco * 0.90}")

elif seletor == 10:
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    print(f"A média das notas é {(nota1 + nota2) / 2}")

#ETAPA SELEÇÃO IF E ELSE
elif seletor == 11:
    numero_parImpar = int(input("Informe um número: "))
    if numero_parImpar % 2 == 0:
        print(f"O número {numero_parImpar} é par")
    else:
        print(f"O número {numero_parImpar} é ímpar")

elif seletor == 12:
    numero_positivoNegativo = int(input("Informe um número: "))
    if numero_positivoNegativo > 0:
        print(f"O número {numero_positivoNegativo} é positivo")
    elif numero_positivoNegativo < 0:
        print(f"O número {numero_positivoNegativo} é negativo")
    else:
        print(f"O número {numero_positivoNegativo} é zero")

elif seletor == 13:
    numero_maior = int(input("Informe um número: "))
    numero_menor = int(input("Informe outro número: "))
    if numero_maior > numero_menor:
        print(f"O número {numero_maior} é maior que {numero_menor}")
    elif numero_maior < numero_menor:
        print(f"O número {numero_menor} é maior que {numero_maior}")
    else:
        print(f"Os números {numero_maior} e {numero_menor} são iguais")

elif seletor == 14:
    numero1 = int(input("Informe um número: "))
    numero2 = int(input("Informe outro número: "))
    numero3 = int(input("Informe mais um número: "))
    if numero1 < numero2 and numero1 < numero3:
        print(f"O número {numero1} é o menor")
    elif numero2 < numero1 and numero2 < numero3:
        print(f"O número {numero2} é o menor")
    else:
        print(f"O número {numero3} é o menor")

elif seletor == 15:
    idade = int(input("Informe sua idade: "))
    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")

elif seletor == 16:
    nota = float(input("Informe sua nota: "))
    if nota >= 7:
        print("Você foi aprovado")
    else:
        print("Você foi reprovado")

elif seletor == 17:
    numero = int(input("Informe um número: "))
    if numero >= 1 and numero <= 100:
        print("O número está entre 1 e 100")
    else:
        print("O número não está entre 1 e 100")

elif seletor == 18:
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Você foi aprovado")
    else:
        print("Você foi reprovado")

elif seletor == 19:
    ano = int(input("Informe o ano: "))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")

elif seletor == 20:
    num1 = int(input("Informe um número: "))
    num2 = int(input("Informe outro número: "))
    
    if num1 > num2:
        print(f"A diferença absoluta entre os números é {abs(num1 - num2)}")
    elif num2 > num1:
        print(f"A diferença absoluta entre os números é {abs(num2 - num1)}")
    else:
        print("Os números são iguais")

elif seletor == 21:
    inicio = 1
    for n in range(1, 21):
        print(inicio)
        inicio += 1

elif seletor == 22:
    inicio = 20
    while inicio >= 1:
        print(inicio)
        inicio -= 1

elif seletor == 23:
    for i in range(1, 51):
        par: bool = i % 2 == 0  
        
        if par == True:
            print(f"{i} é par")
        else:
            pass

