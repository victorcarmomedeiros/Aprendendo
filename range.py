n = int(input("digite o numero que quer localizar: "))

for elemento in range(0, 10):
    print(elemento)
    if elemento == n:
        print(f"Elemento {n} localizado")
        break
    else:
        print("passando");
        