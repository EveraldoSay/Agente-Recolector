from entorno.entorno import Entorno  # IMPORTAMOS CLASE Entorno PARA CREAR ENTORNO
from agente.agente import Agente    # IMPORTAMOS CLASE Agente PARA CREAR EL AGENTE
from visualizacion.visualizacion import Visualizacion  # IMPORTAMOS CLASE Visualizacion PARA MOSTRAR EL GAME

def main():
    # CREAMOS ENTORNO
    entorno = Entorno(grid_size=10, num_objects=5, num_obstacles=10)
    
    # CREAR AGENTE 
    agente = Agente(entorno)
    
    # CREAMOS INTERFAZ PARA VISUALIZACION
    visualizacion = Visualizacion(entorno, agente)
    
    # INICIAMOS BUCLE
    visualizacion.run()

if __name__ == "__main__":
    main()  # EJECUTAMOS FUNCION main() 