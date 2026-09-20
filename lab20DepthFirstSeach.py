def dfs(matrix, node):
    inicio = [node]
    visitados = []
    while inicio:
        nodo_actual = inicio.pop()
        if nodo_actual not in visitados:
            visitados.append(nodo_actual)
            for i in range(len(matrix)):
                if matrix[nodo_actual][i] == 1:
                    inicio.append(i)
    return visitados

