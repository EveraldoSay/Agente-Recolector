import random

class Entorno:
    def __init__(self, grid_size, num_objects, num_obstacles):
        # INICIALIZAR EL ENTORNO CON EL TAMAÑO DE LA CUADRÍCULA, NÚMERO DE OBJETOS Y NÚMERO DE OBSTÁCULOS
        self.grid_size = grid_size  # TAMAÑO DE LA CUADRÍCULA (N x N)
        self.num_objects = num_objects  # NÚMERO DE OBJETOS EN EL ENTORNO
        self.num_obstacles = num_obstacles  # NÚMERO DE OBSTÁCULOS EN EL ENTORNO
        self.grid = self._crear_entorno(num_objects, num_obstacles)  # CREAR LA CUADRÍCULA CON OBJETOS Y OBSTÁCULOS

    def _crear_entorno(self, num_objects, num_obstacles):
        # CREAR UNA CUADRÍCULA VACÍA (LLENA DE CEROS)
        grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # COLOCAR OBJETOS EN LA CUADRÍCULA
        for _ in range(num_objects):
            # GENERAR COORDENADAS ALEATORIAS (x, y) PARA COLOCAR UN OBJETO
            x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            # VERIFICAR QUE LA CELDA ESTÉ VACÍA (VALOR 0), SI NO, GENERAR NUEVAS COORDENADAS
            while grid[x][y] != 0:
                x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            # COLOCAR EL OBJETO EN LA CELDA (VALOR 1)
            grid[x][y] = 1

        # COLOCAR OBSTÁCULOS EN LA CUADRÍCULA
        for _ in range(num_obstacles):
            # GENERAR COORDENADAS ALEATORIAS (x, y) PARA COLOCAR UN OBSTÁCULO
            x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            # VERIFICAR QUE LA CELDA ESTÉ VACÍA (VALOR 0), SI NO, GENERAR NUEVAS COORDENADAS
            while grid[x][y] != 0:
                x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            # COLOCAR EL OBSTÁCULO EN LA CELDA (VALOR 2)
            grid[x][y] = 2

        # DEVOLVER LA CUADRÍCULA CON OBJETOS Y OBSTÁCULOS COLOCADOS
        return grid