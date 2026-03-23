
# EDA: Clasificación de dígitos 1, 2 y 3

## 1. Descripción del problema

Se quiere identificar si una imagen contiene un número:

* 1
* 2
* 3

---

## 2. Variables

### Variables de entrada (X)

Son los píxeles de la imagen.

| Tipo                | Descripción              |
| ------------------- | ------------------------ |
| pixel_1 a pixel_784 | Intensidad de cada píxel |

---

### Variable de salida (y)

| Clase |
| ----- |
| 1     |
| 2     |
| 3     |

---

## 3. Análisis visual

* El número 1 es una línea vertical
* El número 2 tiene curva arriba y línea abajo
* El número 3 tiene dos curvas

---

## 4. Distribución de clases

Se debe revisar si hay la misma cantidad de ejemplos:

| Clase | Cantidad |
| ----- | -------- |
| 1     | similar  |
| 2     | similar  |
| 3     | similar  |

---

## 5. Problemas posibles

* El 2 y el 3 se pueden parecer
* Imágenes borrosas
* Diferentes formas de escribir números
