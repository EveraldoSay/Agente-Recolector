class Agente:
    def __init__(self, entorno):
        self.entorno = entorno
        self.x, self.y = 0, 0  # POSICIÓN INICIAL DEL AGENTE
        self.collected_objects = 0  # CONTADOR DE OBJETOS RECOLECTADOS

    def mover(self, dx, dy):
        # CALCULAR LA NUEVA POSICIÓN
        new_x = self.x + dx
        new_y = self.y + dy

        # VERIFICAR SI LA NUEVA POSICIÓN ES VÁLIDA (DENTRO DE LA CUADRÍCULA Y SIN OBSTÁCULOS)
        if 0 <= new_x < self.entorno.grid_size and 0 <= new_y < self.entorno.grid_size:
            if self.entorno.grid[new_x][new_y] != 2:  # SI NO ES UN OBSTÁCULO
                self.x, self.y = new_x, new_y  # ACTUALIZAR POSICIÓN
                if self.entorno.grid[self.x][self.y] == 1:  # SI HAY UN OBJETO
                    self.collected_objects += 1  # INCREMENTAR CONTADOR
                    self.entorno.grid[self.x][self.y] = 0  # ELIMINAR EL OBJETO

    def detectar_basura_cercana(self):
        # DETECTAR BASURA EN LAS CELDAS ADYACENTES (ARRIBA, ABAJO, IZQUIERDA, DERECHA)
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # ARRIBA, ABAJO, IZQUIERDA, DERECHA
        for dx, dy in direcciones:
            new_x = self.x + dx
            new_y = self.y + dy
            if 0 <= new_x < self.entorno.grid_size and 0 <= new_y < self.entorno.grid_size:
                if self.entorno.grid[new_x][new_y] == 1:  # SI HAY BASURA
                    return (dx, dy)  # DEVOLVER LA DIRECCIÓN DE LA BASURA
        return None  # NO HAY BASURA CERCANA