def selection_sort(lista):
    for i in range(len(lista) -1):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista




