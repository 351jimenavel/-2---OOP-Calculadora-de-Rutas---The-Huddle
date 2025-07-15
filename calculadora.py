
from collections import deque
import time

class CalculadoraDeRutas:
    
    def __init__(self, mapa, entrada, salida):
        '''Constructor: guarda el tablero (mapa), la posición de entrada y salida.'''
        self.mapa = mapa            # objeto tipo Mapa
        self.matriz = mapa.matriz   # acceso directo a la matriz del mapa
        self.entrada = entrada
        self.salida = salida
        self.camino = self.generar_camino_valido()

    #--------métodos--------
    def generar_camino_valido(self):
        '''Recorre la matriz y guarda todas las celdas válidas para caminar (., E, S).'''
        camino = []
        for fila in range(self.mapa.filas):
            for columna in range(self.mapa.columnas):
                if self.matriz[fila][columna] in [".", "E", "S"]:
                    camino.append((fila, columna))
        return camino
    
    def resolver_bfs(self):
        '''Algoritmo BFS: busca el camino más corto entre entrada y salida.'''
        visitada = set()
        frontier = deque()
        solucion = {}

        frontier.append(self.entrada)    # Posicion inicial entra a la cola
        visitada.add(self.entrada)
        solucion[self.entrada] = None      # se marca que esa celda No tiene padre, ya que es el comienzo (no se llegó desde ni una celda)

        while frontier:
            x, y = frontier.popleft()       # celda actual 

            if self.matriz[x][y] == "S":
                break

            ## Se verifican celdas vecinas o adyacentes 
            ## Movimeintos: arriba, izquierda, abajo, derecha
            vecinos = [(x-1,y), (x,y-1),(x+1,y),(x,y+1)]
            for celda in vecinos:
                if celda in self.camino and celda not in visitada:   # no está fuera del tablero ni es obstáculo
                    solucion[celda] = (x,y)

                    frontier.append(celda)
                    visitada.add(celda)

                    if self.matriz[celda[0]][celda[1]] not in ("E","S"):
                        self.matriz[celda[0]][celda[1]] = "*"
                
                    self.mapa.mostrar_matriz()
                    time.sleep(0.1)
            
        if self.salida not in solucion:
            return None
        
        # Devuelve el diccionario solucion que guarda la ruta recorrida (cada celda sabe desde dónde se llegó a ella).
        return solucion

    def mostrar_camino(self, diccionario_solucion):
        '''Metodo que sirve para reconstruir el camino que BFS encontró desde la entrada (E) hacia la salida (S), usando el diccionario solucion.'''
        camino_recorrido = []
        x, y = self.salida
        
        while (x,y) != self.entrada: #Mientras no hayas llegado a la entrada, seguís retrocediendo.
            camino_recorrido.append((x,y))
            x,y = diccionario_solucion[(x,y)] # Busca en el diccionario solucion cuál fue la celda anterior desde donde llegó a (x, y) cuando BFS exploró. Luego, actualiza (x, y) para retroceder por ese camino.
        
        camino_recorrido.append(self.entrada)
        camino_recorrido.reverse()

        '''Se recorre la lista de coordenadas invertidas para marcar el camino'''
        for fila, columna in camino_recorrido:
            if self.matriz[fila][columna] not in ("E","S"):
                self.matriz[fila][columna] = "o"
                self.mapa.mostrar_matriz()
                time.sleep(0.2)