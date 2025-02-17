class Agente:
    def __init__(self, entorno):
        # INICIAMOS AGENTE CON EL ENTORNO
        self.entorno = entorno  # GUARDAR ENTORNO AGENTE
        self.x, self.y = 0, 0   # POSICIÓN INICIAL AGENTE (FILA 0, COLUMNA 0)
        self.collected_objects = 0  # CONTADOR DE OBJ'S RECOLECTADOS (INICIA 0)

    def mover(self, dx, dy):
        # CALCULAR LA NUEVA POSICION DEL AGENTE
        new_x = self.x + dx  # NUEVA FILA (dx ES EL CAMBIO EN LA FILA: -1 PARA ARRIBA, 1 PARA ABAJO)
        new_y = self.y + dy  # NUEVA COLUMNA (dy ES EL CAMBIO EN LA COLUMNA: -1 PARA IZQUIERDA, 1 PARA DERECHA)

        # VERIFICAMOS SI LA NUEVA POSICIÓN ESTÁ DENTRO DE LOS LÍMITES DE LA CUADRÍCULA
        if 0 <= new_x < self.entorno.grid_size and 0 <= new_y < self.entorno.grid_size:
            # VERIFICAMOS SI LA NUEVA POSICIÓN NO CONCUERDE CON LA DE UN OSTACULO
            if self.entorno.grid[new_x][new_y] != 2:
                # ACTUALIZAR LA POSICIÓN AGENTE
                self.x, self.y = new_x, new_y

                # VERIFICAMOS QUE EN NUEVA POSICION NO CONCUERDE CON LA POSICION D OBJETO RECOLECTABLE (VALOR 1 EN LA CUADRÍCULA)
                if self.entorno.grid[self.x][self.y] == 1:
                    # INCREMENTAMOS CONTADOR DE OBJ'S RECOLECTADOS
                    self.collected_objects += 1
                    # MARCAR LA CELDA COMO VACÍA (VALOR 0) LUEGO DE RECOLECTAR OBJETO
                    self.entorno.grid[self.x][self.y] = 0