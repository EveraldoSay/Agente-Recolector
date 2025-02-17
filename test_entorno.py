import unittest
from entorno.entorno import Entorno  # IMPORTAMOS CLASE Entorno PARA CREAR ENTORNO

class TestEntorno(unittest.TestCase):
    def setUp(self):
        """CONFIGURAR EL ENTORNO ANTES DE CADA PRUEBA."""
        self.grid_size = 10  # TAMAÑO DE LA CUADRÍCULA 
        self.num_objects = 5  # NUM DE OBJETOS EN ENTORNO
        self.num_obstacles = 10  # NUM DE OBSTÁCULOS EN ENTORNO
        self.entorno = Entorno(self.grid_size, self.num_objects, self.num_obstacles)  # CREAR ENTORNO

    def test_entorno_creado_correctamente(self):
        """VERIFICAR QUE EL ENTORNO SE CREA CON EL TAMAÑO CORRECTO."""
        self.assertEqual(len(self.entorno.grid), self.grid_size)  # VERIFICAR NUM DE FILAS
        self.assertEqual(len(self.entorno.grid[0]), self.grid_size)  # VERIFICAR NUM DE COLUMNAS

    def test_objetos_colocados_correctamente(self):
        """VERIFICAR QUE LOS OBJETOS SE COLOCAN EN EL ENTORNO."""
        object_count = sum(row.count(1) for row in self.entorno.grid)  # CONTAR OBJETOS (VALOR 1)
        self.assertEqual(object_count, self.num_objects)  # VERIFICAR QUE HAY N OBJETOS (def setUp EN test_agente)

    def test_obstaculos_colocados_correctamente(self):
        """VERIFICAR QUE LOS OBSTÁCULOS SE COLOCAN EN EL ENTORNO."""
        obstacle_count = sum(row.count(2) for row in self.entorno.grid)  # CONTAR OBSTÁCULOS (VALOR 2)
        self.assertEqual(obstacle_count, self.num_obstacles)  # VERIFICAR QUE HAY N OBSTÁCULOS (def setUp EN test_agente)

    def test_celda_vacia(self):
        """VERIFICAR QUE LAS CELDAS VACÍAS ESTÉN MARCADAS COMO 0."""
        for x in range(self.grid_size):  # RECORRER FILAS
            for y in range(self.grid_size):  # RECORRER COLUMNAS
                if self.entorno.grid[x][y] not in [1, 2]:  # SI NO ES OBJETO NI OBSTÁCULO
                    self.assertEqual(self.entorno.grid[x][y], 0)  # DEBE SER VACÍA (VALOR 0)

if __name__ == "__main__":
    unittest.main()  # EJECucioon de pruebas