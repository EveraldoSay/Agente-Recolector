import pygame
import os

class Visualizacion:
    def __init__(self, entorno, agente):
        # INICIAMOS LA CLASE VISUALIZACION CON EL ENTORNO Y EL AGENTE
        self.entorno = entorno  # GUARDAR EL ENTORNO
        self.agente = agente    # GUARDAR EL AGENTE
        self.cell_size = 50     # TAMAÑO DE CADA CELDA EN PÍXELES PARA AJUSTAR NUESTRAS IMAGENS
        self.window_size = self.entorno.grid_size * self.cell_size  # TAMAÑO DE LA VENTANA

        # CARGAR IMG'S DE OBJETOS: CARPTA "ASSETS"
        self.agente_img = pygame.image.load(os.path.join("assets", "agente.png"))  # APARIENCIA DEL AGENTE
        self.obstaculo_imgs = [  # LISTA DE IMÁGENES OBSTACULOS
            pygame.image.load(os.path.join("assets", "obstaculo1.png")),  
            pygame.image.load(os.path.join("assets", "obstaculo2.png")), 
            pygame.image.load(os.path.join("assets", "obstaculo3.png")),  
            pygame.image.load(os.path.join("assets", "obstaculo4.png")), 
            pygame.image.load(os.path.join("assets", "obstaculo5.png")),  
            pygame.image.load(os.path.join("assets", "obstaculo6.png")),  
            pygame.image.load(os.path.join("assets", "obstaculo7.png")),  
            pygame.image.load(os.path.join("assets", "obstaculo8.png")), 
        ]
        self.basura_img = pygame.image.load(os.path.join("assets", "basura.png"))  # IMAGEN DE LO QUE RECOLECTA (BASURA)
        self.piso_img = pygame.image.load(os.path.join("assets", "piso_ceramico.jpg"))  # FONDO DE LA VENTANA

        # ADAPTAMOS IMG'S AL TAMAÑO DE LA CELDA Y FORMATO DE LA VENTANA
        self.agente_img = pygame.transform.scale(self.agente_img, (self.cell_size, self.cell_size))  
        self.obstaculo_imgs = [pygame.transform.scale(img, (self.cell_size, self.cell_size)) for img in self.obstaculo_imgs]  
        self.basura_img = pygame.transform.scale(self.basura_img, (self.cell_size, self.cell_size))  
        self.piso_img = pygame.transform.scale(self.piso_img, (self.window_size, self.window_size)) 

        # INICIALIZAR PYGAME PARA LANZAR VENTANA AL USER
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption("Agente Recolector")  # TÍTULO DE MI VENTANA

    def dibujar_entorno(self):
        # DIBUJAR EL PISO EN LA VENTANA
        self.screen.blit(self.piso_img, (0, 0))

        # DIBUJAR OBSTÁCULOS Y OBJETOS EN LA CUADRÍCULA
        for x in range(self.entorno.grid_size):  # RECORRER FILAS
            for y in range(self.entorno.grid_size):  # RECORRER COLUMNAS
                if self.entorno.grid[x][y] == 1:  # SI HAY UN OBJETO (BASURA)
                    self.screen.blit(self.basura_img, (y * self.cell_size, x * self.cell_size))  # DIBUJAR BASURA
                elif self.entorno.grid[x][y] == 2:  # SI HAY UN OBSTÁCULO
                    obstaculo_img = self.obstaculo_imgs[(x + y) % len(self.obstaculo_imgs)]  # SELECCIONAR IMAGEN DE OBSTÁCULO (ALEATORIO DE NUESTROS OBSTACULOS)
                    self.screen.blit(obstaculo_img, (y * self.cell_size, x * self.cell_size))  # DIBUJAR OBSTÁCULO

    def dibujar_agente(self):
        # DIBUJAR AL AGENTE EN SU POSICIÓN ACTUAL
        self.screen.blit(self.agente_img, (self.agente.y * self.cell_size, self.agente.x * self.cell_size))

    def run(self):
        # BUCLE PRINCIPAL DEL JUEGO
        running = True
        while running:
            for event in pygame.event.get():  # DETECTAR EVENTOS (TECLAS/CIERRE DE LA VENTANA)
                if event.type == pygame.QUIT:  # SI EL USER CIERRA LA VENTANA
                    running = False
                elif event.type == pygame.KEYDOWN:  # SI EL USER PRESIONA UNA TECLA
                    if event.key == pygame.K_UP:  # TECLA ARRIBA
                        self.agente.mover(-1, 0)  # MUEVE EL AGENTE ARRIBA
                    elif event.key == pygame.K_DOWN:  # TECLA ABAJO
                        self.agente.mover(1, 0)  # MUEVE EL AGENTE ABAJO
                    elif event.key == pygame.K_LEFT:  # TECLA IZQUIERDA
                        self.agente.mover(0, -1)  # MUEVE EL AGENTE A LA IZQ
                    elif event.key == pygame.K_RIGHT:  # TECLA DERECHA
                        self.agente.mover(0, 1)  # MUEVE EL AGENTE A LA DER

            # DIBUJAR EL ENTORNO Y EL AGENTE EN CADA ITERACIÓN DEL BUCLE
            self.dibujar_entorno()
            self.dibujar_agente()
            pygame.display.flip()  # ACTUALIZAR LA PANTALLA

        pygame.quit()  # CERRAR PYGAME AL SALIR DEL BUCLE