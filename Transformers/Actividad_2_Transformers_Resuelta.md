# Solución: Actividad manual Parte 2 — Entender Transformers

## Actividad 6 — Matriz de atención completa

**Paso 1 y 2 — Matriz Puntuada y Normalizada (%)**
*(Valores de ejemplo simplificados donde cada fila suma 100%)*

| Desde ↓ / Hacia → | LA | NIÑA | PEQUEÑA | COME | FRUTA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LA** | 10% | **60%** | 10% | 10% | 10% |
| **NIÑA** | 10% | 10% | 20% | **50%** | 10% |
| **PEQUEÑA** | 10% | **60%** | 10% | 10% | 10% |
| **COME** | 5% | 35% | 10% | 10% | **40%** |
| **FRUTA** | 5% | 10% | 5% | **60%** | 20% |

**Paso 3 — Preguntas de análisis**
1. **¿La fila de COME se parece a la de FRUTA?** No. COME (verbo) atiende a quién hace la acción (NIÑA) y qué recibe la acción (FRUTA). FRUTA (objeto) atiende casi exclusivamente a la acción (COME).
2. **¿Fila con atención pareja?** COME, porque como verbo transitivo necesita conectar toda la idea (sujeto y objeto) para tener contexto.
3. **100 palabras:** Tendría 10,000 celdas (100 x 100). El crecimiento es cuadrático, lo que satura la memoria RAM en textos muy largos.

---

## Actividad 7 — Softmax a mano

**Paso 2 — Dividir cada uno entre la suma (25.68)**

| Palabra | Exponencial | ÷ 25.68 | ≈ % |
| :--- | :--- | :--- | :--- |
| **NIÑA** | 20.09 | 20.09 / 25.68 | **78 %** |
| **PEQUEÑA**| 1.65 | 1.65 / 25.68 | **6 %** |
| **COME** | 1.22 | 1.22 / 25.68 | **5 %** |
| **FRUTA** | 2.72 | 2.72 / 25.68 | **11 %** |

**Pregunta:**
¿Por qué no dividir directo? Porque Softmax (al usar exponenciales) maneja números negativos y **amplifica las diferencias**. Hace que el modelo "tome una decisión" más clara en lugar de dudar entre valores cercanos.

---

## Actividad 8 — Mezcla de "vectores contenido"

**Cálculo de la suma ponderada para COME:**
* LA: 0.05 × (1, 1) = (0.05, 0.05)
* NIÑA: 0.35 × (4, 5) = (1.40, 1.75)
* PEQUEÑA: 0.10 × (3, 4) = (0.30, 0.40)
* COME: 0.10 × (5, 1) = (0.50, 0.10)
* FRUTA: 0.40 × (6, 3) = (2.40, 1.20)

**Vector resultante de COME:** 
* Suma X: 0.05 + 1.40 + 0.30 + 0.50 + 2.40 = **4.65**
* Suma Y: 0.05 + 1.75 + 0.40 + 0.10 + 1.20 = **3.50**
* **Salida = (4.65, 3.50)** 
*(En un mapa, este punto quedaría en medio de FRUTA y NIÑA, fusionando su significado).*

---

## Actividad 9 — Máscara de padding

* **¿Por qué Frase 2 no necesita tantas celdas tachadas?** Porque ocupa los 5 espacios con palabras reales, no tiene relleno.
* **¿Qué pasaría si el modelo atendiera a PAD?** Aprendería patrones falsos y ruido. Las palabras reales mezclarían información de "vacío", arruinando su vector de significado.

---

## Actividad 10 — Atención cruzada (Cross-attention)

**Matriz para la Palabra 3 (hueco = COFFEE)**

| Desde (inglés) ↓ / Español → | YO | QUIERO | CAFE |
| :--- | :--- | :--- | :--- |
| **Palabra 3 (hueco)** | 5% | 15% | **80%** |

**Respuestas:**
1. **¿CAFE debería ganar?** Sí, porque es la traducción directa que dicta qué debe generar el decoder a continuación.
2. **¿La fila de I mira a YO?** Sí, tiene total sentido para traducir el pronombre.
3. **Diferencia clave:** En Cross-attention miramos de un idioma a otro (Decoder → Encoder).

---

## Actividad 11 — Adivinar la palabra tapada (BERT)

* **¿Por qué COME debería superar a VERDE?** Porque gramaticalmente y semánticamente tiene sentido que un gato "coma" pescado. "Verde" no encaja.
* **¿DUERME tiene sentido?** Tendría sentido aislado con GATO, pero choca con la palabra de la derecha (PESCADO). 
* **¿Por qué ver PESCADO?** Porque el contexto posterior es lo que define la acción real. Esa es la ventaja bidireccional de BERT.

---

## Actividad 12 — Dos capas de atención

**Reflexión FRUTA (Capa 2):**
En la segunda capa, la palabra FRUTA ya no solo atiende al texto original. Ahora "sabe" que COME tiene un perfil enriquecido (perfil 7), el cual ya contiene información de la NIÑA. FRUTA atiende fuerte a COME para entender el evento completo: *una niña comiéndola*.

---

## Actividad 13 — RNN vs Transformer

1. **Saltos para llegar de A a E:**
   * RNN: 4 saltos (secuencial).
   * Atención: 1 salto (conexión directa en la matriz).
2. **Con 100 palabras:** Los 100 enlaces de la RNN crecen lento (lineal), mientras que la Atención salta a 10,000 celdas (cuadrático).
3. **¿Por qué usar Transformers?** Por el **paralelismo** (se calcula todo a la vez, haciéndolo rapidísimo en GPUs) y porque al tener **1 solo salto**, no hay pérdida de información o "amnesia" en frases largas.

---

## Actividad 14 — Escalar para evitar saturación

**Ejercicio numérico:**
1. Softmax de [8, 2, 2, 2]: El 8 domina por completo (ej. 99% vs 0.3%). Se satura y el modelo deja de aprender de las demás palabras.
2. Softmax de [4, 1, 1, 1] (dividido por 2): El 4 sigue ganando (ej. 87%), pero los "1" (4.3%) todavía tienen suficiente porcentaje para aportar algo a la mezcla de vectores.
3. **Conclusión:** Escalar (dividir entre la raíz cuadrada de la dimensión) evita que la función exponencial se dispare, manteniendo un reparto de atención más equilibrado y sano.
