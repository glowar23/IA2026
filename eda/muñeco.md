# EDA: Problema del muñeco y la bala

## 1. Descripción del problema

Tenemos un sistema donde:

* Una bala se mueve con cierta velocidad.
* El muñeco debe reaccionar.

Las acciones posibles del muñeco son:

* Brincar
* Agacharse
* Quedarse quieto

El objetivo es predecir qué acción debe tomar el muñeco según la altura de la bala.

---

## 2. Variables del problema

### Variables de entrada (X)

| Variable       | Descripción                  |
| -------------- | ---------------------------- |
| altura_bala    | Altura a la que pasa la bala |
| velocidad_bala | Qué tan rápido va la bala    |

### Variable de salida (y)

| Acción    |
| --------- |
| brincar   |
| agacharse |
| quedarse  |

---

## 3. Análisis de datos

### Distribución de altura

* Alturas bajas: peligro para piernas
* Alturas medias: peligro para torso
* Alturas altas: no hay peligro

---

## 4. Relación entre variables

| Altura | Acción esperada |
| ------ | --------------- |
| Baja   | brincar         |
| Media  | agacharse       |
| Alta   | quedarse        |

---

## 5. Posibles problemas

* Datos incorrectos (altura mal medida)
* Velocidad muy alta (menos tiempo de reacción)
* Casos en los límites (confusión entre brincar y agacharse)





