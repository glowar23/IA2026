# ACTIVIDAD 2: EL ENIGMA DEL ORÁCULO SECUENCIAL  
## Anatomía de una Vanilla RNN

---

## 2.1 Actividad 2.1: Mapeo de Variables

Dada la ecuación:
$$
h_t = tanh(W_hx x_t + W_hh h_{t-1} + b)
$$
**Identificación de cada componente según el poema:**

- $x_$t  
  "Soy la novedad pura, el pulso del instante, la matriz de características que el mundo me da en este segundo."

- $h_${t-1}  
  "el fantasma del pasado, que trae consigo el resumen de todo lo que hemos vivido hasta ayer."

- W_hx, W_hh  
  "cruzamos por peajes inmutables, barreras que multiplican nuestra importancia y deciden qué tanto valemos."

- b  
  "un pequeño desvío inevitable"

- tanh  
  "chocamos contra un muro curvo que nos comprime entre el -1 y el 1, evitando que nuestra energía explote hacia el infinito."

- h_t  
  "Al salir de esa curva, nazco yo, una nueva identidad. Soy tu estado actual, la respuesta de hoy, y estoy listo para ser el fantasma de tu mañana."

---

## 2.2 Actividad 2.2: Análisis de Dimensionalidad

Datos:
- x_t ∈ R^20
- h_{t-1} ∈ R^64

1. Dimensión de W_hx

W_hx ∈ R^(64 x 20)

2. Dimensión de W_hh

W_hh ∈ R^(64 x 64)

3. Dimensión de h_t

h_t ∈ R^64

---

## 2.3 Actividad 2.3: La Estrofa Perdida

Soy el leve empujón que rompe la simetría,  
el susurro constante que evita el punto muerto.  
No dependo del instante ni del eco del pasado,  
pero inclino la balanza para que el destino no nazca en cero.

---

## 2.4 Actividad 2.4: Análisis de Saturación

f(z) = tanh(z)  
f'(z) = 1 - tanh^2(z)

Para z = 500:

tanh(500) ≈ 1  
f'(500) = 0

Explicación:

Cuando la función se satura, su derivada tiende a cero, provocando el problema de vanishing gradient, donde la red deja de aprender porque los gradientes desaparecen.

---

## 2.5 Actividad 2.5: El Eco del Castigo

El error debe atravesar:

- La función tanh (derivada)
- Las matrices W_hh
- El estado h_{t-1}

Operación matemática: regla de la cadena.

Problema: desaparición del gradiente por multiplicaciones sucesivas.

---

## 2.6 Actividad 2.6: Depuración del Oráculo

Error:

Uso de * (multiplicación elemento a elemento) en lugar de producto matricial.

Corrección:

```
def paso_rnn_correcto(x_t, h_prev, W_hx, W_hh, b):
    combinacion = np.dot(W_hx, x_t) + np.dot(W_hh, h_prev) + b
    return np.tanh(combinacion)
```

Alternativa:

```
combinacion = (W_hx @ x_t) + (W_hh @ h_prev) + b
```
