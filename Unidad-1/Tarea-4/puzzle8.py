import time
from collections import deque

class Nodo:
    def __init__(self, estado, padre=None):
        self.estado = estado
        self.padre = padre

    def get_estado(self):
        return self.estado

#imprime cada movimiento
def imprimir_estado(estado):
    for fila in estado:
        print("{" + "}{".join(map(str, fila)) + "}")
    print("")


def ubicar_posicion_cero(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return (i, j)
    return None

def clonar_estado(estado):
    return [list(fila) for fila in estado]

def buscar_solucion(inicio, solucion):
    expandidos = deque()
    visitados = set()
    expandidos.append(inicio)
    cont = 0

    while expandidos:
        revisar = expandidos.popleft()
        estado_actual = revisar.get_estado()
        cont += 1

        if estado_actual == solucion:
            print("******** Solución Encontrada ********")
            return revisar

        visitados.add(tuple(map(tuple, estado_actual)))
        pcero = ubicar_posicion_cero(estado_actual)

        # Movimientos posibles
        movimientos = [
            ("arriba", (pcero[0] - 1, pcero[1])),
            ("abajo", (pcero[0] + 1, pcero[1])),
            ("izquierda", (pcero[0], pcero[1] - 1)),
            ("derecha", (pcero[0], pcero[1] + 1))
        ]

        for movimiento, (i, j) in movimientos:
            if 0 <= i < 3 and 0 <= j < 3:
                nuevo_estado = clonar_estado(estado_actual)
                nuevo_estado[pcero[0]][pcero[1]] = nuevo_estado[i][j]
                nuevo_estado[i][j] = 0

                if tuple(map(tuple, nuevo_estado)) not in visitados:
                    expandidos.append(Nodo(nuevo_estado, revisar))

    return None


def main():
    # Estado inicial y solución
    inicio = [[1, 5, 3], 
              [6, 0, 4],
              [7, 2, 8]]
    solucion = [[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 0]]

    # Inicia el temporizador
    start_time = time.time()

    nodo_inicial = Nodo(inicio)
    sol = buscar_solucion(nodo_inicial, solucion)
    cont = 1


    pila = []
    while sol:
        pila.append(sol)
        sol = sol.padre

    while pila:
        actual = pila.pop()
        print("--------------------------------------------------------------------------------")
        print("Movimiento Nro:", cont)
        imprimir_estado(actual.get_estado())
        cont += 1
    
    #imprime el tiempo que tarda en la ejecución
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")


if __name__ == "__main__":
    main()