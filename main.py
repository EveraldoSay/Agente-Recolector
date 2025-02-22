import random  # IMPORTAR EL MÓDULO RANDOM PARA GENERAR NUM ALEATORIOS DE BASURA
from entorno.entorno import Entorno
from agente.agente import Agente
from visualizacion.visualizacion import Visualizacion

def main():
    # Crear el entorno con un número aleatorio de objetos (entre 1 y  max 6)
    num_objects = random.randint(1, 6)  # NÚMERO ALEATORIO DE OBJETOS
    entorno = Entorno(grid_size=10, num_objects=num_objects, num_obstacles=10)
    
    # CREAMOS el agente
    agente = Agente(entorno)
    
    # CREAMOS la visualización
    visualizacion = Visualizacion(entorno, agente)
    
    # BUCLE principal del juego
    visualizacion.run()

if __name__ == "__main__":
    main()  # EJECUTAMOS FUNCION main()