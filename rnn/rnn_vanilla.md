# El Termómetro de las Emociones (Vanilla RNN)

## Definición del modelo

Usamos una versión simplificada de una RNN:

$$
h_t = x_t + \alpha h_{t-1}
$$

Donde:
- $h_t$: estado emocional actual  
- $x_t$: evento del día  
- $\alpha$: factor de memoria (ej. 0.5 → recuerdas el 50%)  

---

# Misión 1: El Lunes Increíble

## Datos:
- $\alpha = 0.5$
- Día 1: $x_1 = 10$
- Día 2–5: $x_t = 0$

## Cálculo:

´´´
Día 1:
h1 = 10

Día 2:
h2 = 0 + 0.5(10) = 5

Día 3:
h3 = 0 + 0.5(5) = 2.5

Día 4:
h4 = 0 + 0.5(2.5) = 1.25

Día 5:
h5 = 0 + 0.5(1.25) = 0.625
´´´



## Resultado:

**Estado final = 0.625**

### Interpretación:
El evento fuerte se desvanece rápidamente. Esto es el problema clásico de *vanishing memory*.

---

# Misión 2: El Rescate Emocional

## Datos:
- $\alpha = 0.5$
- Día 1: -6  
- Día 2: -4  
- Día 3: 0  

## Cálculo:
´´´
Día 1:
h1 = -6

Día 2:
h2 = -4 + 0.5(-6) = -4 - 3 = -7

Día 3:
h3 = 0 + 0.5(-7) = -3.5
´´´

Queremos:

$$
h_4 = x_4 + 0.5(-3.5) > 0
$$

Resolviendo:

´´´
h4 = x4 - 1.75 > 0

x4 > 1.75
´´´



## Resultado:

**El evento del Día 4 debe ser mayor a 1.75**

### Interpretación:
Necesitas un evento positivo suficientemente fuerte para superar la inercia negativa acumulada.

---

# Misión 3: Constancia vs Pico

## Escenario A:
- Día 1: +10  
- Día 2–5: 0  

Resultado:
**h5 = 0.625**

---

## Escenario B:
- Todos los días: +3  

## Cálculo:
´´´
Día 1:
h1 = 3

Día 2:
h2 = 3 + 0.5(3) = 4.5

Día 3:
h3 = 3 + 0.5(4.5) = 5.25

Día 4:
h4 = 3 + 0.5(5.25) = 5.625

Día 5:
h5 = 3 + 0.5(5.625) = 5.8125
´´´


---

## Resultado final:

- Escenario A: **0.625**  
- Escenario B: **5.8125**

---

# Conclusión

- Las Vanilla RNN tienen memoria **corta**.
- Los eventos antiguos pierden peso exponencialmente.
- La red favorece:
  - información reciente
  - patrones constantes
