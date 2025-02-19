#Carrasco Medina Carlos Ivan
#Peña Vizcarra Jatniel Alejandro
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            actual = self.raiz
            while True:
                if valor < actual.valor:
                    if actual.izquierda is None:
                        actual.izquierda = Nodo(valor)
                        break
                    else:
                        actual = actual.izquierda
                else:
                    if actual.derecha is None:
                        actual.derecha = Nodo(valor)
                        break
                    else:
                        actual = actual.derecha

    def insertar_desde_input(self):
        num_inserciones = int(input("Ingrese el número de inserciones: "))
        for i in range(1, num_inserciones + 1):
            valor = int(input(f"Ingrese el número [{i}]: "))
            self.insertar(valor)
        print("Recorrido inorden:", self.recorrido_inorden(self.raiz))

    def recorrido_inorden(self, nodo, resultado=None):
        if resultado is None:
            resultado = []
        if nodo:
            self.recorrido_inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self.recorrido_inorden(nodo.derecha, resultado)
        return resultado

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar_desde_input()