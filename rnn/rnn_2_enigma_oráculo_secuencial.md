# ACTIVIDAD 2: EL ENIGMA DEL ORÁCULO SECUENCIAL  
## Anatomía de una Vanilla RNN

---

## 2.1 Actividad 2.1: Mapeo de Variables

Dada la ecuación:

$$
h_t = \tanh\left( W_{hx} \cdot x_t \;+\; W_{hh} \cdot h_{t-1} \;+\; b \right)
$$


**Identificación de cada componente según el poema:**

- $x_t$  
  "Soy la novedad pura, el pulso del instante, la matriz de características que el mundo me da en este segundo."

- $h_{t-1}$  
  "Soy el fantasma del pasado, que trae consigo el resumen de todo lo que hemos vivido hasta ayer."

- $W_{hx}, W_{hh}$  
  "Cruzamos por peajes inmutables, barreras que multiplican nuestra importancia y deciden qué tanto valemos."

- $b$  
  "Soy un pequeño desvío inevitable."

- $\tanh$  
  "Chocamos contra un muro curvo que nos comprime entre el -1 y el 1, evitando que nuestra energía explote hacia el infinito."

- $h_t$  
  "Al salir de esa curva, nazco yo, una nueva identidad. Soy tu estado actual, la respuesta de hoy, y estoy listo para ser el fantasma de tu mañana."

---

## 2.2 Actividad 2.2: Análisis de Dimensionalidad

**Datos:**

- $x_t \in \mathbb{R}^{20}$
- $h_{t-1} \in \mathbb{R}^{64}$

**1. Dimensión de $W_{hx}$**

$$
W_{hx} \in \mathbb{R}^{64 \times 20}
$$

**2. Dimensión de $W_{hh}$**

$$
W_{hh} \in \mathbb{R}^{64 \times 64}
$$

**3. Dimensión de $h_t$**

$$
h_t \in \mathbb{R}^{64}
$$

---

## 2.3 Actividad 2.3: La Estrofa Perdida

> Soy el leve empujón que rompe la simetría,  
> el susurro constante que evita el punto muerto.  
> No dependo del instante ni del eco del pasado,  
> pero inclino la balanza para que el destino no nazca en cero.

---

## 2.4 Actividad 2.4: Análisis de Saturación

Sea:

$$
f(z) = \tanh(z)
$$

$$
f'(z) = 1 - \tanh^2(z)
$$

**Para $z = 500$:**

$$
\tanh(500) \approx 1
$$

$$
f'(500) \approx 0
$$

**Explicación:**

Cuando la función se satura, su derivada tiende a cero, provocando el problema de *vanishing gradient*, donde la red deja de aprender porque los gradientes desaparecen durante la retropropagación.

---

## 2.5 Actividad 2.5: El Eco del Castigo

El error debe atravesar:

- La función $\tanh$ (a través de su derivada)
- Las matrices $W_{hh}$
- El estado $h_{t-1}$

**Operación matemática involucrada:**

Regla de la cadena.

**Problema:**

La desaparición del gradiente debido a multiplicaciones sucesivas de valores pequeños (especialmente en secuencias largas).

---

## 2.6 Actividad 2.6: Depuración del Oráculo

**Error detectado:**

Uso de `*` (multiplicación elemento a elemento) en lugar de producto matricial.

**Corrección:**

```
def paso_rnn_correcto(x_t, h_prev, W_hx, W_hh, b):
    combinacion = np.dot(W_hx, x_t) + np.dot(W_hh, h_prev) + b
    return np.tanh(combinacion)
´´´
