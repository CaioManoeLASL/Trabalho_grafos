#Lista indexada
grafo = {
    "AC": ["AM", "RO"],
    "AL": ["BA", "PE", "SE"],
    "AP": ["PA"],
    "AM": ["AC", "RO", "MT", "PA", "RR"],
    "BA": ["AL", "SE", "PE", "PI", "TO", "GO", "MG", "ES"],
    "CE": ["RN", "PB", "PE", "PI"],
    "DF": ["GO"],
    "ES": ["BA", "MG", "RJ"],
    "GO": ["MT", "MS", "MG", "BA", "TO", "DF"],
    "MA": ["PA", "TO", "PI"],
    "MG": ["BA", "ES", "RJ", "SP", "MS", "GO"],
    "MS": ["MT", "GO", "MG", "SP", "PR"],
    "MT": ["RO", "AM", "PA", "TO", "GO", "MS"],
    "PA": ["AP", "AM", "MT", "TO", "MA"],
    "PB": ["RN", "CE", "PE"],
    "PR": ["SP", "MS", "SC"],
    "PE": ["PB", "CE", "PI", "BA", "AL"],
    "PI": ["MA", "TO", "BA", "PE", "CE"],
    "RJ": ["ES", "MG", "SP"],
    "RN": ["CE", "PB"],
    "RO": ["AC", "AM", "MT"],
    "RR": ["AM", "PA"],
    "RS": ["SC"],
    "SC": ["PR", "RS"],
    "SE": ["AL", "BA"],
    "SP": ["RJ", "MG", "MS", "PR"],
    "TO": ["PA", "MT", "GO", "BA", "PI", "MA"]
}

print("Lista Indexada (Lista de Adjacência):\n")

for estado in sorted(grafo):
    print(f"{estado}: {', '.join(grafo[estado])}")

#Matrix de adjacência
estados = list(grafo.keys())
n = len(estados)

matriz_adj = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if estados[j] in grafo[estados[i]]:
            matriz_adj[i][j] = 1

print("\nMatriz de Adjacência:\n")

print("   ", " ".join(estados))

for i in range(n):
    print(estados[i], matriz_adj[i])

#Matrix de incidência
arestas = []

for estado in grafo:
    for vizinho in grafo[estado]:
        if estado < vizinho:
            arestas.append((estado, vizinho))

m = len(arestas)
matriz_inc = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if estados[i] in arestas[j]:
            matriz_inc[i][j] = 1

print("\nArestas:")
for i, aresta in enumerate(arestas):
    print(f"e{i}: {aresta}")

print("\nMatriz de Incidência:\n")

for i in range(n):
    linha = " ".join(str(x) for x in matriz_inc[i])
    print(f"{estados[i]}  {linha}")

# PARTE C: Graus máximo e mínimo

graus_lista = {estado: len(vizinhos) for estado, vizinhos in grafo.items()}
graus_matriz_adj = {estados[i]: sum(matriz_adj[i]) for i in range(n)}
graus_matriz_inc = {estados[i]: sum(matriz_inc[i]) for i in range(n)}

def analisar_extremos(dicionario_graus, nome_rep):
    val_max = max(dicionario_graus.values())
    val_min = min(dicionario_graus.values())
    
    est_max = [est for est, g in dicionario_graus.items() if g == val_max]
    est_min = [est for est, g in dicionario_graus.items() if g == val_min]
    
    print(f"\n--- Representação: {nome_rep} ---")
    print(f"Grau Máximo: {val_max} ({', '.join(est_max)})")
    print(f"Grau Mínimo: {val_min} ({', '.join(est_min)})")
    
# PARTE C: Listar vizinhos dos graus máximo e mínimo

    print("\nVizinhos - Grau Máximo:")
    for est in est_max:
        print(f"  {est}: {', '.join(grafo[est])}")
        
    print("Vizinhos - Grau Mínimo:")
    for est in est_min:
        print(f"  {est}: {', '.join(grafo[est])}")

analisar_extremos(graus_lista, "Lista Indexada")
analisar_extremos(graus_matriz_adj, "Matriz de Adjacência")
analisar_extremos(graus_matriz_inc, "Matriz de Incidência")

# PARTE C: Frequência dos graus e histograma

print("\nHISTOGRAMA DE FREQUÊNCIA")

todos_os_graus = list(graus_lista.values())
faixa_de_graus = range(min(todos_os_graus), max(todos_os_graus) + 1)

for g in faixa_de_graus:
    quantidade = todos_os_graus.count(g)
    barra = "*" * quantidade
    print(f"Grau {g}: {quantidade} estado(s) {barra}")