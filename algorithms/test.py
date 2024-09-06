import random

# Tamaño del mapa
ANCHO = 20
ALTO = 20

# Definimos los tipos de terreno
AGUA = '~'        # Representa agua
PASTO = '.'       # Representa pasto
MONTAÑA = '^'     # Representa montaña

# Definimos una lista de terrenos
TERRENOS = [AGUA, PASTO, MONTAÑA]

# Función para elegir el terreno basado en los vecinos
def elegir_terreno_con_adyacentes(mapa, x, y):
    # Pesos iniciales para los tipos de terreno
    pesos = {AGUA: 2, PASTO: 30, MONTAÑA: 10}
    
    # Revisar los vecinos y aumentar los pesos para terrenos coincidentes
    vecinos = obtener_vecinos(mapa, x, y)
    for vecino in vecinos:
        if vecino in pesos:
            pesos[vecino] += 4  # Aumentamos la probabilidad según los vecinos

    # Elegir el terreno basado en los pesos
    total = sum(pesos.values())
    rand = random.uniform(0, total)
    acumulado = 0
    for terreno, peso in pesos.items():
        acumulado += peso
        if rand <= acumulado:
            return terreno
    return PASTO  # Valor por defecto

# Función para obtener los vecinos de una celda
def obtener_vecinos(mapa, x, y):
    vecinos = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),(-1, -1),(1, -1),(-1, 1),(1, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(mapa[0]) and 0 <= ny < len(mapa):
            vecinos.append(mapa[ny][nx])
    return vecinos

# Función para generar el mapa proceduralmente con áreas coherentes
def generar_mapa(ancho, alto):
    mapa = [[None for _ in range(ancho)] for _ in range(alto)]
    for y in range(alto):
        for x in range(ancho):
            if x == 0 and y == 0:
                # Para la primera celda, elegimos un terreno al azar
                mapa[y][x] = random.choices(TERRENOS, [0.2, 0.6, 0.2])[0]
            else:
                # Elegimos el terreno basado en los vecinos
                mapa[y][x] = elegir_terreno_con_adyacentes(mapa, x, y)
    return mapa

# Función para imprimir el mapa
def imprimir_mapa(mapa):
    for fila in mapa:
        print(" ".join(fila))

# Generar y mostrar el mapa
mapa = generar_mapa(ANCHO, ALTO)
imprimir_mapa(mapa)
