from mapa import Mapa
from calculadora import CalculadoraDeRutas
import time

def main():

    '''_____________CONF. INICIAL_____________'''

    #_________________tablero_________________
    filas_usuario = int(input("Ingresa la cantidad de filas para el tablero: "))
    columnas_usuario = int(input("Ingresa la cantidad de columnas para el tablero: "))

    #_________________objeto 1_________________
    mapa = Mapa(filas_usuario,columnas_usuario)

    #_________________entrada_________________
    while True:
        print("Intentando colocar entrada...")
        coord_fila_entrada = int(input("Ingresa en que fila estará la ENTRADA: "))
        coord_columna_entrada = int(input("Ingresa en que columna estará la ENTRADA: "))
        if mapa.colocar_entrada(coord_fila_entrada,coord_columna_entrada):
            break
    
    #__________________salida__________________
    while True:
        print("Intentando colocar salida...")
        coord_fila_salida = int(input("Ingresa en que fila estará la SALIDA: "))
        coord_columna_salida = int(input("Ingresa en que columna estará la SALIDA: "))
        
        if mapa.colocar_salida(coord_fila_salida,coord_columna_salida):
            break

    mapa.mostrar_matriz()
    time.sleep(1)

    #________________obstaculos________________
    while True:
        print("Intentando colocar obstaculo...")
        print("Qué obstaculos quieres agregar")
        print("(1) Edificios. (2) Agua. (3) Muros.")
        eleccion_obstaculos_usuario = int(input("Elige: "))

        cantidad_obs = int(input("Elige la cantidad de obstaculos que quieres agregar: "))
        for _ in range(cantidad_obs):
            print("Agregando obs...")
            coord_fila_obstaculo = int(input("Ingresa en que fila estará el obstaculo: "))
            coord_columna_obstaculo = int(input("Ingresa en que columna estará el obstaculo: "))
            mapa.colocar_obstaculos(coord_fila_obstaculo, coord_columna_obstaculo, eleccion_obstaculos_usuario)
            mapa.mostrar_matriz()
            time.sleep(0.5)

        # Opcion de seguir agregando obs.
        seguir_agregando = input("Quieres seguir agregando obstaculos? s/n ").lower()

        if seguir_agregando == "s":
            continue
        break

    mapa.mostrar_matriz()

    #__________________objeto 2__________________
    buscador = CalculadoraDeRutas(mapa, mapa.entrada, mapa.salida)
    diccionario_solucion = buscador.resolver_bfs()  

    #_______________mostrar camino_______________
    if diccionario_solucion is None:
        print("No se encontró un camino entre Entrada y Salida")
    else:
        buscador.mostrar_camino(diccionario_solucion)

if __name__ == '__main__':
    main()
