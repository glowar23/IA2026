## Actividad 1: La matriz de atención

### Enunciado
Frase de estudio: **EL | GATO | COME | PESCADO**

Desde la perspectiva de la palabra **COME**, puntuamos del 0 al 10 cuánto "importa" cada elemento de la oración para entender el verbo (10 = importancia máxima).

#### Paso 1: Fila de puntuación (Perspectiva de "COME")
| | EL | GATO | COME | PESCADO |
| :--- | :---: | :---: | :---: | :---: |
| **Desde COME →** | 1 | 8 | 4 | 7 |

#### Paso 2: Convertir a porcentajes (Mini-Softmax)
* **Suma total de puntuaciones:** $1 + 8 + 4 + 7 = 20$
* **Operación:** $(	ext{Puntuación} \div 20) 	imes 100$

| Palabra | Puntuación | ÷ Suma | × 100 ≈ % |
| :--- | :---: | :---: | :---: |
| **EL** | 1 | 0.05 | **5 %** |
| **GATO** | 8 | 0.40 | **40 %** |
| **COME** | 4 | 0.20 | **20 %** |
| **PESCADO** | 7 | 0.35 | **35 %** |
| **Total** | **20** | - | **100 %** |

### Paso 3: Interpretación y Cierre
* **¿A quién le diste más atención? ¿Tiene sentido para el verbo "come"?** *Le di más atención a **GATO** (40%) y a **PESCADO** (35%). Sí, tiene sentido lingüístico porque para entender la acción de "comer" es fundamental identificar al sujeto que la realiza (Gato) y al objeto que es consumido (Pescado).*
* **Si fueras la palabra PESCADO, ¿crees que tu fila de porcentajes sería igual? ¿Por qué sí o por no?** *No sería igual. La atención en los Transformers es asimétrica. La palabra "PESCADO" le daría mucha importancia a "COME" (el verbo que actúa sobre ella), pero sus proporciones cambiarían por completo al tener un rol gramatical y necesidades de contexto distintas.*

---

## Actividad 2: La palabra ambigua (dos contextos)

Demostración de cómo la palabra **BANCO** reasigna sus pesos de atención según los vectores de sus palabras vecinas.

### Frase A: FUIMOS AL BANCO DEL RIO
* **Suma de puntuaciones:** $2 + 1 + 3 + 4 + 10 = 20$

| Palabra | FUIMOS | AL | BANCO | DEL | RIO | Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Puntuación** | 2 | 1 | 3 | 4 | 10 | **20** |
| **Porcentaje** | 10% | 5% | 15% | 20% | **50%** | **100%** |

### Frase B: FUIMOS AL BANCO A SACAR DINERO
* **Suma de puntuaciones:** $2 + 1 + 3 + 1 + 6 + 7 = 20$

| Palabra | FUIMOS | AL | BANCO | A | SACAR | DINERO | Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Puntuación** | 2 | 1 | 3 | 1 | 6 | 7 | **20** |
| **Porcentaje** | 10% | 5% | 15% | 5% | **30%** | **35%** | **100%** |

### Preguntas de análisis
1. **¿En cuál frase BANCO le da más puntos a “RIO” / “DEL”?** En la Frase A (70% en conjunto).
2. **¿En cuál le da más a “DINERO” / “SACAR”?** En la Frase B (65% en conjunto).
3. **Conclusión en 3 líneas:** *Esto demuestra que un Transformer no utiliza un diccionario rígido de significados. La palabra "BANCO" actualiza su propia identidad matemática absorbiendo el contexto de sus palabras vecinas, diferenciando con precisión la geografía de las finanzas.*

---

## Actividad 3: Máscara causal (no hacer trampa)

### Matriz de Atención Causal (4×4)
Representa qué palabras del pasado y presente puede inspeccionar el modelo para generar secuencialmente la frase: **EL GATO COME PESCADO**.

| Palabra actual | EL | GATO | COME | PESCADO |
| :--- | :---: | :---: | :---: | :---: |
| **1º EL** | ✓ | ✗ | ✗ | ✗ |
| **2º GATO** | ✓ | ✓ | ✗ | ✗ |
| **3º COME** | ✓ | ✓ | ✓ | ✗ |
| **4º PESCADO** | ✓ | ✓ | ✓ | ✓ |

### Preguntas de análisis
* **¿Cuántos ✓ hay en la fila de la última palabra (PESCADO)?** *Hay 4 ✓. Al ser la última, dispone de todo el historial de palabras previas generadas.*
* **¿Cuántos ✓ hay en la fila de la primera palabra (EL)?** *Hay 1 ✓. Solo se puede atender a sí misma porque no hay un pasado disponible.*
* **¿Por qué la máscara causal (forma de triángulo inferior) es necesaria para escribir texto?** *Es obligatoria porque, si el modelo pudiera "ver el futuro" durante su entrenamiento, aprendería a copiar las respuestas en lugar de aprender el arte de predecir la siguiente palabra basándose únicamente en lo que ya se ha dicho.*

---

## Actividad 4: Varias cabezas (varios criterios)

Frase de estudio: **MARIA | NO | COMIO | PORQUE | ESTABA | ENFERMA**

Cada "Cabeza de Atención" evalúa de manera independiente la fila del verbo **COMIO** bajo un filtro exclusivo.

#### Cabeza A - Criterio: ¿Quién explica el porqué? (Causa)
* Suma: $0 + 1 + 2 + 5 + 3 + 9 = 20$
* **Porcentajes:** MARIA (0%) | NO (5%) | COMIO (10%) | **PORQUE (25%)** | ESTABA (15%) | **ENFERMA (45%)**

#### Cabeza B - Criterio: ¿Quién es el sujeto de la acción?
* Suma: $10 + 4 + 2 + 0 + 0 + 0 = 16$
* **Porcentajes:** **MARIA (62.5%)** | NO (25%) | COMIO (12.5%) | PORQUE (0%) | ESTABA (0%) | ENFERMA (0%)

#### Cabeza C - Criterio: ¿Quién está junto al verbo? (Vecinos inmediatos)
* Suma: $0 + 10 + 4 + 10 + 0 + 0 = 24$
* **Porcentajes:** MARIA (0%) | **NO (41.7%)** | COMIO (16.6%) | **PORQUE (41.7%)** | ESTABA (0%) | ENFERMA (0%)

### Preguntas de análisis
* **¿Las tres filas son iguales?** No, enfocan su atención en objetivos completamente distintos.
* **¿Qué ventaja tiene ver la frase desde tres criterios y no solo uno?** *El lenguaje es multidimensional. Al procesar la frase con múltiples cabezas en paralelo, el Transformer puede descifrar simultáneamente la gramática local (vecinos), la estructura de los actores (sujeto) y la lógica del mensaje (causalidad), logrando un entendimiento integral imposible de conseguir con un único punto de vista.*

---

## Actividad 5: Encoder vs Decoder (role-play)

### Resumen de la Dinámica en Clase
El **Encoder** es el sistema que procesa y digiere una frase oculta y completa enviando pistas semánticas complejas (vectores codificados). El **Decoder** toma estas pistas e intenta reconstruir secuencialmente el texto original en base a lo que ya escribió y a la información destilada que le provee el Encoder.

### Debrief (Preguntas para el Plenario)
1. **¿Qué fue más fácil: leer todo (Encoder) o escribir de a poco (Decoder)?** *Leer todo es más sencillo porque el contexto completo está disponible de golpe. Escribir paso a paso exige planeación lógica, recordar lo estructurado con anterioridad y asegurar concordancia sintáctica dinámica.*
2. **¿En qué momento el Decoder “necesitó” mirar atrás?** *Cada vez que debía elegir la siguiente palabra (como adjetivos o complementos), necesitando verificar si correspondía en género, número y sentido con las primeras palabras elegidas.*
3. **¿Cómo se relaciona esto con traducir o con un chatbot?** *En **traducción**, el Encoder analiza todo el texto en el idioma origen (ej. Inglés) y el Decoder genera de forma secuencial su contraparte (ej. Español). En un **chatbot**, la pregunta que ingresas (Prompt) pasa por el Encoder para ser comprendida, mientras que la respuesta fluida que ves aparecer en pantalla se genera palabra por palabra mediante el Decoder.*
Taller_Completo_
