from spanningTree import Grafo

grafo = Grafo(4)

# ponemos aristas con sus pesos
grafo.agregar_arista(0, 1, 2)
grafo.agregar_arista(0, 3, 6)
grafo.agregar_arista(1, 2, 3)
grafo.agregar_arista(1, 3, 8)
grafo.agregar_arista(2, 3, 4)

arbol = grafo.prim_arbol_exp_minima()

# Imprimimos
print("Las aristas son:")
for u, v in arbol:
    print(u, v)
