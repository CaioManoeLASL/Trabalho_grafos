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