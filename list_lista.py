lista1 = [1, 2, 3, 4, 3, 2]
lista2 = [3, 5, 6, 1, 6, 7]
lista3 = lista1 + lista2

lista_sem_repetidos = list(set(lista3))
listafinal = sorted(lista_sem_repetidos)
print("Lista final sem repetidos e ordenada:", listafinal)