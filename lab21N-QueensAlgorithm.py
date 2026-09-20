def dfs_n_queens(n):
    if n < 1:
        return []
    soluciones = []
    tablero = []
    def es_seguro(tablero, fila, columna):
        for f in range(len(tablero)):
            if tablero[f] == columna or abs(f - fila) == abs(tablero[f] - columna):
                return False
        return True
    def dfs(fila):
        if fila == n:
            soluciones.append(list(tablero))
            return
        for c in range(n):
            if es_seguro(tablero, fila, c):
                tablero.append(c)
                dfs(fila + 1)
                tablero.pop()
    dfs(0)
    return soluciones