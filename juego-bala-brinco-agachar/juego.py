import os
import csv
import random
from collections import deque
from dataclasses import dataclass
from typing import List

import numpy as np
import pygame

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

# =========================================
# CONFIG
# =========================================

BASE_W = 1080
BASE_H = 720

FPS = 45

# =========================================
# DATASET
# =========================================

@dataclass
class Sample:
    velocidad_bala: float
    distancia: float
    altura_relativa: float
    tiempo_colision: float
    accion: int
    # 0 = nada
    # 1 = salto
    # 2 = agacharse


# =========================================
# JUEGO
# =========================================

class Juego:

    def __init__(self):

        pygame.init()

        self.w = BASE_W
        self.h = BASE_H

        self.pantalla = pygame.display.set_mode(
            (self.w, self.h)
        )

        pygame.display.set_caption(
            "Juego IA - Aprendizaje"
        )

        self.clock = pygame.time.Clock()

        # =========================================
        # COLORES
        # =========================================

        self.BLANCO = (255, 255, 255)
        self.NEGRO = (0, 0, 0)
        self.GRIS = (180, 180, 180)
        self.AMARILLO = (255, 220, 120)

        # =========================================
        # ESTADO
        # =========================================

        self.corriendo = True

        self.modo_auto = False

        # =========================================
        # IA
        # =========================================

        self.modelo = None
        self.scaler = None

        self.modelo_entrenado = False

        self.datos_modelo: List[Sample] = []

        # =========================================
        # PERSONAJE
        # =========================================

        self.player_w = 44
        self.player_h = 58

        self.player_h_duck = 34

        self.margin = 120

        self.ground_y = self.h - 130

        self.jugador = pygame.Rect(
            self.margin,
            self.ground_y,
            self.player_w,
            self.player_h
        )

        # =========================================
        # BALA
        # =========================================

        self.bullet_size = 18

        self.bala = pygame.Rect(
            self.w - 180,
            self.ground_y,
            self.bullet_size,
            self.bullet_size
        )

        self.bala_disparada = False

        self.velocidad_bala = -12

        # =========================================
        # NAVE
        # =========================================

        self.ship_size = 100

        self.nave = pygame.Rect(
            self.w - 240,
            self.ground_y - 80,
            self.ship_size,
            self.ship_size
        )

        # =========================================
        # SALTO
        # =========================================

        self.salto = False
        self.en_suelo = True

        self.salto_vel_inicial = 18
        self.salto_vel = self.salto_vel_inicial

        self.gravedad = 1.1

        # =========================================
        # AGACHARSE
        # =========================================

        self.agachado = False

        self.duracion_agachado = 18
        self.tiempo_agachado = 0
        self.cooldown_agachado = 0
        self.duracion_cooldown_agachado = 2   # ~9 frames ≈ 200ms a 45 FPS

        # =========================================
        # FONDO
        # =========================================

        self.fondo_speed = 4

        self.fondo_x1 = 0
        self.fondo_x2 = self.w

        # =========================================
        # MEMORIA IA
        # =========================================

        self.historial_acciones = deque(maxlen=35)

        # =========================================
        # ASSETS
        # =========================================

        self._cargar_assets()

        self.current_frame = 0
        self.frame_count = 0
        self.frame_speed = 8

        # =========================================
        # REGISTRO
        # =========================================

        self.accion_actual = 0

        self.ultimo_registro = -999

        self._reset_estado_juego()

    # =========================================
    # ASSETS
    # =========================================

    def _safe_load(self, path, size, color):

        try:

            img = pygame.image.load(path).convert_alpha()

            return pygame.transform.smoothscale(
                img,
                size
            )

        except Exception:

            surf = pygame.Surface(size, pygame.SRCALPHA)

            surf.fill(color)

            return surf

    def _cargar_assets(self):

        base = os.path.dirname(__file__)

        self.jugador_frames = [

            self._safe_load(
                os.path.join(
                    base,
                    "assets/sprites/mono_frame_1.png"
                ),
                (self.player_w, self.player_h),
                (255, 255, 255, 255)
            ),

            self._safe_load(
                os.path.join(
                    base,
                    "assets/sprites/mono_frame_2.png"
                ),
                (self.player_w, self.player_h),
                (255, 255, 255, 255)
            ),

            self._safe_load(
                os.path.join(
                    base,
                    "assets/sprites/mono_frame_3.png"
                ),
                (self.player_w, self.player_h),
                (255, 255, 255, 255)
            ),

            self._safe_load(
                os.path.join(
                    base,
                    "assets/sprites/mono_frame_4.png"
                ),
                (self.player_w, self.player_h),
                (255, 255, 255, 255)
            ),
        ]

        self.bala_img = self._safe_load(
            os.path.join(
                base,
                "assets/sprites/purple_ball.png"
            ),
            (self.bullet_size, self.bullet_size),
            (180, 100, 255, 255)
        )

        self.fondo_img = self._safe_load(
            os.path.join(
                base,
                "assets/game/fondo2.png"
            ),
            (self.w, self.h),
            (40, 40, 40, 255)
        )

        self.nave_img = self._safe_load(
            os.path.join(
                base,
                "assets/game/ufo.png"
            ),
            (self.ship_size, self.ship_size),
            (100, 255, 180, 255)
        )

    # =========================================
    # RESET
    # =========================================

    def _reset_estado_juego(self):

        self.jugador.x = self.margin

        self.jugador.y = self.ground_y

        self.jugador.height = self.player_h

        self.salto = False

        self.en_suelo = True

        self.salto_vel = self.salto_vel_inicial

        self.agachado = False

        self.tiempo_agachado = 0

        self.bala.x = self.w - 180

        self._generar_altura_bala()

        self.bala_disparada = False

    # =========================================
    # ALTURA BALA
    # =========================================

    def _generar_altura_bala(self):

        # salto
        baja = self.ground_y + 12

        # agacharse
        media = self.ground_y - 8

        # neutral
        alta = self.ground_y - 48

        self.bala.y = random.choice([
            baja,
            media,
            alta
        ])

        # nave sigue la bala

        self.nave.y = self.bala.y - 35

    # =========================================
    # BALA
    # =========================================

    def disparar_bala(self):

        if not self.bala_disparada:

            self.velocidad_bala = random.randint(
                -12,
                -9
            )

            self._generar_altura_bala()

            self.bala_disparada = True

    def reset_bala(self):

        self.bala.x = self.w - 180

        self._generar_altura_bala()

        self.bala_disparada = False

    # =========================================
    # SALTO
    # =========================================

    def iniciar_salto(self):

        if self.en_suelo and not self.agachado:

            self.salto = True

            self.en_suelo = False

            self.accion_actual = 1

    def manejar_salto(self):

        if self.salto:

            self.jugador.y -= int(
                self.salto_vel
            )

            self.salto_vel -= self.gravedad

            if self.jugador.y >= self.ground_y:

                self.jugador.y = self.ground_y

                self.salto = False

                self.en_suelo = True

                self.salto_vel = (
                    self.salto_vel_inicial
                )

    # =========================================
    # AGACHARSE
    # =========================================

    def iniciar_agacharse(self):

        if self.en_suelo and not self.agachado and self.cooldown_agachado == 0:

            self.agachado = True

            altura_original = self.jugador.height

            self.jugador.height = (
                self.player_h_duck
            )

            self.jugador.y += (
                altura_original -
                self.jugador.height
            )

            self.tiempo_agachado = (
                self.duracion_agachado
            )

            self.accion_actual = 2

    def manejar_agacharse(self):

        if self.cooldown_agachado > 0:
            self.cooldown_agachado -= 1

        if self.agachado:

            self.tiempo_agachado -= 1

            if self.tiempo_agachado <= 0:

                diferencia = (
                    self.player_h -
                    self.jugador.height
                )

                self.jugador.y -= diferencia

                self.jugador.height = self.player_h

                self.agachado = False
                
                self.cooldown_agachado = self.duracion_cooldown_agachado

    # =========================================
    # REGISTRO
    # =========================================

    def registrar_decision_manual(self):

        if self.modo_auto:
            return

        if not self.bala_disparada:
            return

        distancia = abs(
            self.jugador.x -
            self.bala.x
        )

        # solo registrar cuando importa

        if distancia > 210:
            return

        # evitar spam

        if abs(
            distancia -
            self.ultimo_registro
        ) < 14:
            return

        # =====================================
        # ACCION REAL
        # =====================================

        if self.salto:
            accion = 1

        elif self.agachado:
            accion = 2

        else:
            accion = 0

        # Subimos el límite para evitar el desbalance de clases.
        # 180 registros equivalen a agacharse varias veces de forma natural
        # sin saturar el modelo.
        if accion == 2:
            duck_count = sum(1 for s in self.datos_modelo if s.accion == 2)
            if duck_count >= 180:  
                self.ultimo_registro = distancia
                return
        # =====================================
        # FEATURES
        # =====================================
    
        altura_relativa = (
            self.bala.y -
            self.ground_y
        )

        tiempo_colision = (
            distancia /
            abs(self.velocidad_bala)
        )

        # Guardamos la muestra de forma segura
        self.datos_modelo.append(
            Sample(
                velocidad_bala=float(
                    self.velocidad_bala
                ),

                distancia=float(
                    distancia
                ),

                altura_relativa=float(
                    altura_relativa
                ),

                tiempo_colision=float(
                    tiempo_colision
                ),

                accion=accion
            )       
        )

        self.historial_acciones.append(
            accion
        )
        
        self.ultimo_registro = distancia

    # =========================================
    # ENTRENAR
    # =========================================

    def entrenar_modelo(self):

        if len(self.datos_modelo) < 25:

            return (
                False,
                "Necesitas más datos."
            )

        X = [
            [
                s.velocidad_bala,
                s.distancia,
                s.altura_relativa,
                s.tiempo_colision
            ]
            for s in self.datos_modelo
        ]

        y = [
            s.accion
            for s in self.datos_modelo
        ]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        scaler = StandardScaler()

        X_train = scaler.fit_transform(
            X_train
        )

        X_test = scaler.transform(
            X_test
        )

        mlp = MLPClassifier(
            hidden_layer_sizes=(64, 32),
            activation="relu",
            solver="adam",
            max_iter=3000,
            early_stopping=True,
            random_state=42
        )

        tree = DecisionTreeClassifier(
            max_depth=6,
            random_state=42
        )

        ensemble = VotingClassifier(
            estimators=[
                ("mlp", mlp),
                ("tree", tree)
            ],
            voting="soft"
        )

        ensemble.fit(
            X_train,
            y_train
        )

        acc = ensemble.score(
            X_test,
            y_test
        )

        self.modelo = ensemble

        self.scaler = scaler

        self.modelo_entrenado = True

        return (
            True,
            f"Accuracy ≈ {acc:.3f}"
        )

    # =========================================
    # IA
    # =========================================

    def decision_auto(self):
 
        if not self.modelo_entrenado:
            return
 
        # Igual que en manual: no decidir mientras
        # hay una acción en curso o en pausa neutral
        if not self.en_suelo:
            return
 
        if self.agachado or self.cooldown_agachado > 0:
            return
 
        distancia = abs(
            self.jugador.x -
            self.bala.x
        )
 
        altura_relativa = (
            self.bala.y -
            self.ground_y
        )
        tiempo_colision = (
            distancia /
            abs(self.velocidad_bala)
        )
 
        X = [[
            float(self.velocidad_bala),
            float(distancia),
            float(altura_relativa),
            float(tiempo_colision)
        ]]
 
        Xs = self.scaler.transform(X)
 
        accion = int(
            self.modelo.predict(Xs)[0]
        )
 
        # =========================================
        # ACCIÓN
        # =========================================
 
        if accion == 1:
 
            self.iniciar_salto()
 
        elif accion == 2:
 
            self.iniciar_agacharse()

    # =========================================
    # CSV
    # =========================================

    def exportar_csv(self):

        if not self.datos_modelo:

            return "No hay datos."

        ruta = os.path.join(
            os.path.dirname(__file__),
            "datos_ia.csv"
        )

        with open(
            ruta,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "velocidad_bala",
                "distancia",
                "altura_relativa",
                "accion"
            ])

            for s in self.datos_modelo:

                writer.writerow([
                    s.velocidad_bala,
                    s.distancia,
                    s.altura_relativa,
                    s.accion
                ])

        return "CSV exportado."

    # =========================================
    # FUENTE
    # =========================================

    def fuente(
        self,
        texto,
        size,
        color
    ):

        font = pygame.font.SysFont(
            "Arial",
            size
        )

        return font.render(
            texto,
            True,
            color
        )

    # =========================================
    # MENU
    # =========================================

    def _dibujar_menu(self, msg=""):

        self.pantalla.fill(
            self.NEGRO
        )

        titulo = self.fuente(
            "MENU PRINCIPAL",
            40,
            self.BLANCO
        )

        self.pantalla.blit(
            titulo,
            (
                self.w // 2 -
                titulo.get_width() // 2,
                70
            )
        )

        opciones = [

            "M - Manual",

            "A - Automatico",

            "T - Entrenar IA",

            "C - Exportar CSV",

            "SPACE - Saltar",

            "DOWN - Agacharse",

            "ESC - Menu",

            "Q - Salir"
        ]

        y = 180

        for op in opciones:

            txt = self.fuente(
                op,
                28,
                self.BLANCO
            )

            self.pantalla.blit(
                txt,
                (90, y)
            )

            y += 50

        datos = self.fuente(
            f"Datos: {len(self.datos_modelo)}",
            24,
            self.GRIS
        )

        self.pantalla.blit(
            datos,
            (90, y + 20)
        )

        modo = (
            "AUTO"
            if self.modo_auto
            else "MANUAL"
        )

        estado = self.fuente(
            f"Modo actual: {modo}",
            24,
            self.GRIS
        )

        self.pantalla.blit(
            estado,
            (90, y + 60)
        )

        if msg:

            mensaje = self.fuente(
                msg,
                24,
                self.AMARILLO
            )

            self.pantalla.blit(
                mensaje,
                (90, y + 120)
            )

        pygame.display.flip()

    def mostrar_menu(self):

        esperando = True

        mensaje = ""

        while esperando and self.corriendo:

            self._dibujar_menu(
                mensaje
            )

            for e in pygame.event.get():

                if e.type == pygame.QUIT:

                    self.corriendo = False

                    esperando = False

                elif e.type == pygame.KEYDOWN:

                    if e.key == pygame.K_m:

                        # BORRAR TODO

                        self.modo_auto = False

                        self.datos_modelo.clear()

                        self.historial_acciones.clear()

                        self.modelo = None

                        self.scaler = None

                        self.modelo_entrenado = False

                        self._reset_estado_juego()

                        esperando = False

                    elif e.key == pygame.K_a:

                        if not self.modelo_entrenado:

                            mensaje = (
                                "Primero entrena."
                            )

                        else:

                            self.modo_auto = True

                            self._reset_estado_juego()

                            esperando = False

                    elif e.key == pygame.K_t:

                        ok, mensaje = (
                            self.entrenar_modelo()
                        )

                    elif e.key == pygame.K_c:

                        mensaje = (
                            self.exportar_csv()
                        )

                    elif e.key == pygame.K_q:

                        self.corriendo = False

                        esperando = False

    # =========================================
    # UPDATE
    # =========================================

    def _update_frame(self):

        # fondo se mueve

        self.fondo_x1 -= self.fondo_speed
        self.fondo_x2 -= self.fondo_speed

        if self.fondo_x1 <= -self.w:
            self.fondo_x1 = self.w

        if self.fondo_x2 <= -self.w:
            self.fondo_x2 = self.w

        self.pantalla.blit(
            self.fondo_img,
            (self.fondo_x1, 0)
        )

        self.pantalla.blit(
            self.fondo_img,
            (self.fondo_x2, 0)
        )

        # animacion

        self.frame_count += 1

        if self.frame_count >= self.frame_speed:

            self.current_frame = (
                self.current_frame + 1
            ) % len(self.jugador_frames)

            self.frame_count = 0

        jugador_img = pygame.transform.scale(
            self.jugador_frames[
                self.current_frame
            ],
            (
                self.jugador.width,
                self.jugador.height
            )
        )

        self.pantalla.blit(
            jugador_img,
            (
                self.jugador.x,
                self.jugador.y
            )
        )

        self.pantalla.blit(
            self.nave_img,
            (
                self.nave.x,
                self.nave.y
            )
        )

        # bala

        if self.bala_disparada:

            self.bala.x += (
                self.velocidad_bala
            )

        if self.bala.x < -50:

            self.reset_bala()

        self.pantalla.blit(
            self.bala_img,
            (
                self.bala.x,
                self.bala.y
            )
        )

        # colision

        if self.jugador.colliderect(
            self.bala
        ):

            self._reset_estado_juego()

        txt = self.fuente(
            (
                "AUTO"
                if self.modo_auto
                else "MANUAL"
            ),
            24,
            self.AMARILLO
        )

        self.pantalla.blit(
            txt,
            (20, 20)
        )

    # =========================================
    # LOOP
    # =========================================

    def loop(self):

        self.mostrar_menu()

        while self.corriendo:

            for e in pygame.event.get():

                if e.type == pygame.QUIT:

                    self.corriendo = False

                elif e.type == pygame.KEYDOWN:

                    if e.key == pygame.K_q:

                        self.corriendo = False

                    elif e.key == pygame.K_ESCAPE:

                        self.mostrar_menu()

                    elif (
                        e.key == pygame.K_SPACE
                        and not self.modo_auto
                    ):

                        self.iniciar_salto()

                    elif (
                        e.key == pygame.K_DOWN
                        and not self.modo_auto
                    ):

                        self.iniciar_agacharse()

            # =========================================
            # IA
            # =========================================

            if self.modo_auto:

                self.decision_auto()

            else:

                self.registrar_decision_manual()

            # =========================================
            # MOVIMIENTO
            # =========================================

            self.manejar_salto()

            self.manejar_agacharse()

            # =========================================
            # BALA
            # =========================================

            if not self.bala_disparada:

                self.disparar_bala()

            # =========================================
            # RENDER
            # =========================================

            self._update_frame()

            pygame.display.flip()

            self.clock.tick(FPS)

        pygame.quit()


# =========================================
# MAIN
# =========================================

def main():

    juego = Juego()

    juego.loop()


if __name__ == "__main__":

    main()