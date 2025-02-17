import unittest
from entorno.entorno import Entorno  # IMPORTAMOS CLASE Entorno PARA CREAR ENTORNO
from agente.agente import Agente     # IMPORTAMOS CLASE Agente PARA CREAR AGENTE

class TestAgente(unittest.TestCase):
    def setUp(self):
        """CONFIGURAR EL ENTORNO Y EL AGENTE ANTES DE CADA PRUEBA."""
        self.grid_size = 10  # TAMAÑO DE LA CUADRÍCULA
        self.num_objects = 5  # NUM OBJETOS EN ENTORNO
        self.num_obstacles = 10  # NUM OBSTÁCULOS EN ENTORNO
        self.entorno = Entorno(self.grid_size, self.num_objects, self.num_obstacles)  # CREAR ENTORNO
        self.agente = Agente(self.entorno)  # CREAR AGENTE EN EL ENTORNO

    def test_agente_inicia_en_posicion_correcta(self):
        """VERIFICAR QUE EL AGENTE INICIA EN LA POSICIÓN (0, 0)."""
        self.assertEqual(self.agente.x, 0)  # VERIFICAR FILA INICIAL
        self.assertEqual(self.agente.y, 0)  # VERIFICAR COLUMNA INICIAL

    def test_agente_mueve_correctamente(self):
        """VERIFICAR QUE EL AGENTE SE MUEVE CORRECTAMENTE."""
        self.agente.mover(1, 0)  # MOVER HACIA ABAJO
        self.assertEqual(self.agente.x, 1)  # VERIFICAR NUEVA FILA
        self.assertEqual(self.agente.y, 0)  # VERIFICAR COLUMNA

        self.agente.mover(0, 1)  # MOVER HACIA LA DERECHA
        self.assertEqual(self.agente.x, 1)  # VERIFICAR FILA 
        self.assertEqual(self.agente.y, 1)  # VERIFICAR NUEVA COLUMNA

    def test_agente_recolecta_objetos(self):
        """VERIFICAR QUE EL AGENTE RECOLECTA OBJETOS CORRECTAMENTE."""
        # COLOCAR UN OBJETO EN LA POSICIÓN (0, 1)
        self.entorno.grid[0][1] = 1
        self.agente.mover(0, 1)  # MOVER HACIA LA DERECHA
        self.assertEqual(self.agente.collected_objects, 1)  # VERIFICAR QUE RECOGIO OBJETO
        self.assertEqual(self.entorno.grid[0][1], 0)  # VERIFICAR QUE DESAPAREZCA LA IMAGEN CUANDO YA RECOGIO

    def test_agente_evita_obstaculos(self):
        """VERIFICAR QUE EL AGENTE NO PUEDE MOVERSE A UNA CELDA CON UN OBSTÁCULO."""
        # COLOCAR UN OBSTÁCULO EN LA POSICIÓN (1, 0)
        self.entorno.grid[1][0] = 2
        self.agente.mover(1, 0)  # INTENTAR MOVER HACIA ABAJO
        self.assertEqual(self.agente.x, 0)  # VERIFICAR QUE AGENTE NO SE MOVIÓ (FILA)
        self.assertEqual(self.agente.y, 0)  # VERIFICAR QUE AGENTE NO SE MOVIÓ (COLUMNA)

if __name__ == "__main__":
    unittest.main()  # EJECUTAR LAS PRUEBAS CUANDO SE CORRE EL ARCHIVO