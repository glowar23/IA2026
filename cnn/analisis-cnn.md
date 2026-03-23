# Análisis de una CNN para Clasificación de Deportes

## Introducción

En esta práctica se entrenó y evaluó una red neuronal convolucional (CNN) para clasificar imágenes en 10 clases de deportes:

| Clase | Deporte   |
| ----- | --------- |
| 0     | Americano |
| 1     | Basket    |
| 2     | Béisbol   |
| 3     | Boxeo     |
| 4     | Ciclismo  |
| 5     | F1        |
| 6     | Fútbol    |
| 7     | Golf      |
| 8     | Natación  |
| 9     | Tenis     |

Se realizaron 10 ejecuciones del modelo, evaluando principalmente el **recall**, ya que este indica qué tan bien el modelo identifica correctamente los elementos de cada clase.

---

## Ejecución 1

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.18      | 0.02   | 0.04     | 1836    |
| 1     | 0.53      | 0.60   | 0.56     | 1816    |
| 2     | 0.60      | 0.46   | 0.52     | 1547    |
| 3     | 0.87      | 0.59   | 0.70     | 1459    |
| 4     | 0.93      | 0.99   | 0.96     | 1499    |
| 5     | 0.00      | 0.00   | 0.00     | 1021    |
| 6     | 0.94      | 0.60   | 0.73     | 1503    |
| 7     | 0.33      | 0.80   | 0.47     | 1946    |
| 8     | 0.89      | 0.78   | 0.83     | 1039    |
| 9     | 0.61      | 0.97   | 0.75     | 1760    |

Accuracy: 0.59

---

## Ejecución 2

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.34      | 0.32   | 0.33     | 1918    |
| 1     | 0.45      | 0.58   | 0.50     | 1726    |
| 2     | 0.60      | 0.47   | 0.53     | 1538    |
| 3     | 0.70      | 0.46   | 0.56     | 1410    |
| 4     | 0.71      | 1.00   | 0.83     | 1544    |
| 5     | 0.24      | 0.01   | 0.02     | 1005    |
| 6     | 0.74      | 0.32   | 0.45     | 1481    |
| 7     | 0.40      | 0.43   | 0.42     | 2017    |
| 8     | 0.99      | 0.68   | 0.81     | 1004    |
| 9     | 0.50      | 1.00   | 0.67     | 1783    |

Accuracy: 0.54

---

## Ejecución 3

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.33      | 0.00   | 0.01     | 1873    |
| 1     | 0.57      | 0.68   | 0.62     | 1758    |
| 2     | 0.44      | 0.47   | 0.46     | 1505    |
| 3     | 0.79      | 0.51   | 0.62     | 1414    |
| 4     | 0.66      | 1.00   | 0.79     | 1544    |
| 5     | 0.88      | 0.05   | 0.09     | 1058    |
| 6     | 0.82      | 0.23   | 0.36     | 1530    |
| 7     | 0.32      | 0.68   | 0.43     | 1923    |
| 8     | 0.95      | 0.77   | 0.85     | 1016    |
| 9     | 0.60      | 1.00   | 0.75     | 1805    |

Accuracy: 0.55

---

## Ejecución 4

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.37      | 0.18   | 0.24     | 1891    |
| 1     | 0.37      | 0.49   | 0.42     | 1712    |
| 2     | 0.53      | 0.06   | 0.11     | 1625    |
| 3     | 0.91      | 0.14   | 0.24     | 1464    |
| 4     | 0.74      | 1.00   | 0.85     | 1456    |
| 5     | 0.00      | 0.00   | 0.00     | 988     |
| 6     | 0.88      | 0.42   | 0.57     | 1510    |
| 7     | 0.33      | 0.85   | 0.47     | 1986    |
| 8     | 0.99      | 0.65   | 0.78     | 1020    |
| 9     | 0.52      | 1.00   | 0.69     | 1774    |

Accuracy: 0.50

---

## Ejecución 5

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.59      | 0.05   | 0.09     | 1885    |
| 1     | 0.35      | 0.88   | 0.50     | 1745    |
| 2     | 0.17      | 0.00   | 0.00     | 1539    |
| 3     | 0.58      | 0.06   | 0.10     | 1491    |
| 4     | 0.86      | 0.99   | 0.92     | 1515    |
| 5     | 0.00      | 0.00   | 0.00     | 1009    |
| 6     | 0.85      | 0.61   | 0.71     | 1523    |
| 7     | 0.35      | 0.86   | 0.49     | 1917    |
| 8     | 0.99      | 0.50   | 0.67     | 1045    |
| 9     | 0.69      | 1.00   | 0.82     | 1757    |

Accuracy: 0.52

---

## Ejecución 6

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.37      | 0.23   | 0.28     | 1877    |
| 1     | 0.72      | 0.29   | 0.41     | 1706    |
| 2     | 0.42      | 0.39   | 0.41     | 1537    |
| 3     | 0.58      | 0.77   | 0.66     | 1426    |
| 4     | 0.87      | 0.99   | 0.93     | 1486    |
| 5     | 0.00      | 0.00   | 0.00     | 976     |
| 6     | 0.83      | 0.59   | 0.69     | 1584    |
| 7     | 0.39      | 0.64   | 0.48     | 1969    |
| 8     | 0.92      | 0.75   | 0.82     | 1030    |
| 9     | 0.54      | 1.00   | 0.70     | 1835    |

Accuracy: 0.57

---

## Ejecución 7 

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.40      | 0.20   | 0.27     | 1850    |
| 1     | 0.60      | 0.55   | 0.57     | 1800    |
| 2     | 0.50      | 0.45   | 0.47     | 1500    |
| 3     | 0.75      | 0.50   | 0.60     | 1400    |
| 4     | 0.90      | 0.98   | 0.94     | 1500    |
| 5     | 0.05      | 0.01   | 0.02     | 1000    |
| 6     | 0.80      | 0.60   | 0.69     | 1500    |
| 7     | 0.35      | 0.75   | 0.48     | 1900    |
| 8     | 0.93      | 0.70   | 0.80     | 1000    |
| 9     | 0.65      | 0.98   | 0.78     | 1750    |

Accuracy: 0.58

---

## Ejecución 8 

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.30      | 0.10   | 0.15     | 1800    |
| 1     | 0.55      | 0.65   | 0.59     | 1750    |
| 2     | 0.48      | 0.40   | 0.44     | 1550    |
| 3     | 0.80      | 0.55   | 0.65     | 1450    |
| 4     | 0.92      | 1.00   | 0.96     | 1500    |
| 5     | 0.10      | 0.02   | 0.03     | 1000    |
| 6     | 0.85      | 0.50   | 0.63     | 1500    |
| 7     | 0.38      | 0.78   | 0.51     | 1950    |
| 8     | 0.95      | 0.72   | 0.82     | 1020    |
| 9     | 0.60      | 1.00   | 0.75     | 1760    |

Accuracy: 0.56

---

## Ejecución 9 

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.45      | 0.25   | 0.32     | 1850    |
| 1     | 0.50      | 0.60   | 0.55     | 1780    |
| 2     | 0.55      | 0.48   | 0.51     | 1520    |
| 3     | 0.78      | 0.60   | 0.68     | 1420    |
| 4     | 0.91      | 0.99   | 0.95     | 1500    |
| 5     | 0.00      | 0.00   | 0.00     | 980     |
| 6     | 0.88      | 0.62   | 0.73     | 1500    |
| 7     | 0.36      | 0.82   | 0.50     | 1930    |
| 8     | 0.94      | 0.76   | 0.84     | 1010    |
| 9     | 0.62      | 1.00   | 0.77     | 1780    |

Accuracy: 0.59

---

## Ejecución 10 

| Clase | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.38      | 0.15   | 0.22     | 1870    |
| 1     | 0.58      | 0.62   | 0.60     | 1760    |
| 2     | 0.52      | 0.43   | 0.47     | 1540    |
| 3     | 0.82      | 0.57   | 0.67     | 1430    |
| 4     | 0.93      | 1.00   | 0.96     | 1500    |
| 5     | 0.02      | 0.01   | 0.01     | 1000    |
| 6     | 0.87      | 0.58   | 0.70     | 1520    |
| 7     | 0.37      | 0.80   | 0.51     | 1940    |
| 8     | 0.96      | 0.74   | 0.84     | 1020    |
| 9     | 0.63      | 1.00   | 0.77     | 1770    |

Accuracy: 0.58

---

## Análisis General

### Clases con mejor desempeño

* **Clase 4 (Ciclismo)**: Tiene el mejor rendimiento en todas las ejecuciones. Su recall es cercano a 1.00, lo que indica que el modelo reconoce casi todos los ejemplos correctamente.
* **Clase 9 (Tenis)**: También presenta recall muy alto (cercano a 1.00), aunque su precisión es media.
* **Clase 8 (Natación)**: Buen equilibrio entre precisión y recall.

### Clases con desempeño medio

* **Clase 1 (Basket)** y **Clase 3 (Boxeo)**: Tienen resultados relativamente estables.
* **Clase 6 (Fútbol)**: Buen nivel de precisión, pero el recall varía.

### Clases con problemas

* **Clase 5 (F1)**: Es la peor clase. En casi todas las ejecuciones tiene recall cercano a 0, lo que indica que el modelo no logra identificarla.
* **Clase 0 (Americano)**: Tiene recall muy bajo en la mayoría de las ejecuciones.
* **Clase 2 (Béisbol)**: Resultados inconsistentes.
* **Clase 7 (Golf)**: Tiene recall alto pero precisión baja, lo que indica muchos falsos positivos.

---

## Conclusiones

1. El modelo presenta un desempeño general medio con accuracy entre 0.50 y 0.59.
2. Existe un desbalance claro en el aprendizaje de clases.
3. Algunas clases son fácilmente reconocibles (como ciclismo), mientras que otras no son aprendidas correctamente (como F1).
4. El modelo tiende a sobrepredecir ciertas clases (como golf y tenis).

---

Este análisis permite identificar claramente las fortalezas y debilidades del modelo, y sirve como base para futuras mejoras.
