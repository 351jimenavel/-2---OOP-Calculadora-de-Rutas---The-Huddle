## OJO: SRP – Single Responsibility Principle: "Una función/método debería tener una sola razón para cambiar."

import os

class Mapa:

    def __init__(self, filas, columnas):
        '''Método constructor de la clase Mapa'''
        self.filas = filas
        self.columnas = columnas
        self.matriz = [["." for _ in range(columnas)] for _ in range(filas)]
        self.entrada = None
        self.salida = None
        self.obstaculos = set()

    #--------métodos--------
    def validar_coordenada(self, fila, columna):
        '''Método que describe los parámetros de validez dentro del tablero'''
        return 0 <= fila < self.filas and 0 <= columna < self.columnas
    
    def colocar_entrada(self, fila_e, columna_e):
        '''Método para posicionar a Entrada validando lo ingresado por el usuario'''
        # validaciones
        if not self.validar_coordenada(fila_e,columna_e):
            print("Las coordenadas para ENTRADA deben estar dentro del tablero")
            return False
        
        if (fila_e, columna_e) == self.salida:
            print("Las coordenadas de ENTRADA no pueden coincidir con las de SALIDA")
            return False
        
        # Si se puede entonces...
        self.entrada = (fila_e, columna_e)
        self.matriz[fila_e][columna_e] = "E"
        return True

    def colocar_salida(self, fila_s, columna_s):
        '''Método para posicionar a Salida validando lo ingresado por el usuario'''
        # validaciones
        if not self.validar_coordenada(fila_s,columna_s):
            print("Las coordenadas para SALIDA deben estar dentro del tablero")
            return False
        
        if (fila_s, columna_s) == self.entrada:
            print("Las coordenadas de SALIDA no pueden coincidir con las de ENTRADA")
            return False
        
        # Si se puede entonces...
        self.salida = (fila_s, columna_s)
        self.matriz[fila_s][columna_s] = "S"
        return True

    def colocar_obstaculos(self, fila, columna, tipo):
        '''Método para posicionar a los Obstaculos validando lo ingresado por el usuario'''
        # validaciones
        if not self.validar_coordenada(fila, columna):
            print("Las coordenadas para el OBSTACULO deben estar dentro del tablero")
            return False
        
        if (fila, columna) in self.obstaculos or (fila, columna) in [self.entrada, self.salida]:
            print("OCUPADO")
            return False

        if tipo in [1,2,3]:
        # Si se puede entonces...
            self.obstaculos.add((fila, columna))
            self.matriz[fila][columna] = tipo
            return True
        else:
            print("Las opciones son: (1) Edificios, (2) Agua, (3) Muros")
            return False
        
    def _limpiar_consola(self):
        '''Funcion para limpiar la terminal, así se simula un solo tablero'''
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def mostrar_matriz(self):
        '''Método para mostrar visualmente la matriz con todos sus elementos'''
        
        self._limpiar_consola()
        for x in self.matriz:
            for y in x:
                if y == "E":
                    print("E", end=" ")
                elif y == "S":
                    print("S", end=" ")
                elif y == 1:
                    print("X", end=" ")
                elif y == 2:
                    print("~", end=" ")
                elif y == 3:
                    print("#", end=" ")
                elif y == "*":
                    print("*", end=" ")
                elif y == "o":
                    print("o", end=" ")
                else:
                    print(".", end=" ")
            print()