# Listas em Python

# Listas podem conter elementos de diferentes tipos
# Exemplo:
lista_mista = [1, "texto", 3.14, True]

# Podem conter listas aninhadas
# Exemplo:
lista_aninhada = [[1, 2], [3, 4], [5, 6]]

# Podem ser indexadas
# Exemplo:
lista_indexada = ["primeiro", "segundo", "terceiro"]
print(lista_indexada[0]) # Saída: primeiro

# Podem ser modificadas
# Exemplo:
lista_modificada = [1, 2, 3]
lista_modificada[0] = "um"
print(lista_modificada) # Saída: ['um', 2, 3]

# Podem ser adicionadas elementos
# Exemplo:
lista_adicionada = [1, 2, 3]
lista_adicionada.append(4)
print(lista_adicionada) # Saída: [1, 2, 3, 4]

# Podem ser removidos elementos
# Exemplo:
lista_removida = [1, 2, 3]
lista_removida.remove(2)
print(lista_removida) # Saída: [1, 3]

# Podem ser ordenadas
# Exemplo:
lista_ordenada = [3, 1, 2]
lista_ordenada.sort()
print(lista_ordenada) # Saída: [1, 2, 3]

# Podem ser invertidas
# Exemplo:
lista_invertida = [1, 2, 3]
lista_invertida.reverse()
print(lista_invertida) # Saída: [3, 2, 1]

# Podem ser concatenadas
# Exemplo:
lista_concatenada1 = [1, 2, 3]
lista_concatenada2 = [4, 5, 6]
lista_concatenada = lista_concatenada1 + lista_concatenada2
print(lista_concatenada) # Saída: [1, 2, 3, 4, 5, 6]

# Podem ser copiadas
# Exemplo:
lista_copiada = lista_concatenada.copy()
print(lista_copiada) # Saída: [1, 2, 3, 4, 5, 6]

# Podem ser contadas
# Exemplo:
lista_contada = [1, 2, 2, 3, 3, 3]
print(lista_contada.count(2)) # Saída: 2

# Podem ser verificadas a existência de um elemento
# Exemplo:
print(2 in lista_contada) # Saída: True

# Podem ser iteradas
# Exemplo:
for elemento in lista_contada:
    print(elemento)
# Saída:
# 1
# 2
# 2
# 3
# 3
# 3
