import pygame
import os
import random
import time

class Visualizacion:
    def __init__(self, entorno, agente):
        # INICIAMOS LA CLASE VISUALIZACION CON EL ENTORNO Y EL AGENTE
        self.entorno = entorno  # GUARDAR EL ENTORNO
        self.agente = agente    # GUARDAR EL AGENTE
        self.cell_size = 50     # TAMAÑO DE CADA CELDA EN PÍXELES PARA AJUSTAR NUESTRAS IMAGENS
        self.window_size = self.entorno.grid_size * self.cell_size  # TAMAÑO DE LA VENTANA
        self.ultimo_movimiento = time.time()
        self.intervalo_movimiento = 0.1  # Reducir el tiempo entre movimientos (en segundos)
        self.direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # DIRECCIONES POSIBLES

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

    def mostrar_mensaje(self, mensaje1, mensaje2):
        # MOSTRAR UN MENSAJE EN LA VENTANA DURANTE 3 SEGUNDOS
        fuente = pygame.font.Font(None, 36)  # FUENTE MÁS PEQUEÑA (TAMAÑO 36)
        
        # RENDERIZAR EL PRIMER MENSAJE (HABITACIÓN LIMPIA)
        texto1 = fuente.render(mensaje1, True, (0, 0, 0))  # TEXTO EN NEGRO
        texto1_rect = texto1.get_rect(center=(self.window_size // 2, self.window_size // 2 - 20))  # CENTRAR Y SUBIR UN POCO

        # RENDERIZAR EL SEGUNDO MENSAJE (OBJETOS RECOLECTADOS)
        texto2 = fuente.render(mensaje2, True, (0, 0, 0))  # TEXTO EN NEGRO
        texto2_rect = texto2.get_rect(center=(self.window_size // 2, self.window_size // 2 + 20))  # CENTRAR Y BAJAR UN POCO

        # DIBUJAR UN FONDO BLANCO PARA EL MENSAJE
        fondo_ancho = max(texto1_rect.width, texto2_rect.width) + 40  # ANCHO DEL FONDO
        fondo_alto = texto1_rect.height + texto2_rect.height + 40  # ALTO DEL FONDO
        fondo_rect = pygame.Rect(0, 0, fondo_ancho, fondo_alto)
        fondo_rect.center = (self.window_size // 2, self.window_size // 2)  # CENTRAR EL FONDO
        pygame.draw.rect(self.screen, (255, 255, 255), fondo_rect)  # DIBUJAR EL FONDO BLANCO

        # DIBUJAR LOS TEXTOS EN LA PANTALLA
        self.screen.blit(texto1, texto1_rect)
        self.screen.blit(texto2, texto2_rect)
        pygame.display.flip()  # ACTUALIZAR LA PANTALLA

        time.sleep(3)  # ESPERAR 3 SEGUNDOS

    def run(self):
        # BUCLE PRINCIPAL DEL JUEGO
        running = True
        while running:
            tiempo_actual = time.time()
            
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Opcional: Pausa/continúa con espacio
                        self.intervalo_movimiento = 0 if self.intervalo_movimiento else 0.1

            # Movimiento inteligente
            if tiempo_actual - self.ultimo_movimiento >= self.intervalo_movimiento:
                basura_cercana = self.agente.detectar_basura_cercana()  # DETECTAR BASURA CERCANA
                if basura_cercana:
                    dx, dy = basura_cercana  # MOVERSE HACIA LA BASURA
                else:
                    dx, dy = random.choice(self.direcciones)  # MOVERSE ALEATORIAMENTE SI NO HAY BASURA CERCANA
                self.agente.mover(dx, dy)
                self.ultimo_movimiento = tiempo_actual

            # Dibujar el entorno y el agente
            self.dibujar_entorno()
            self.dibujar_agente()
            pygame.display.flip()

            # Verificar si todos los objetos han sido recolectados
            if self.agente.collected_objects == self.entorno.num_objects:
                mensaje1 = "¡Habitación limpia!"
                mensaje2 = f"Objetos recolectados: {self.agente.collected_objects}"
                self.mostrar_mensaje(mensaje1, mensaje2)  # MOSTRAR EL MENSAJE

                # ESPERAR A QUE EL USUARIO CIERRE LA VENTANA MANUALMENTE
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            break
                    if not running:
                        break

        # Cerrar Pygame después de salir del bucle
        pygame.quit()