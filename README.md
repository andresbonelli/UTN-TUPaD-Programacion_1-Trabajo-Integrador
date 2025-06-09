# Trabajo Práctico Integrador - Programacion I
## Tecnicatura en Programación a Distancia - UTN

## Tema: Algoritmos de Búsqueda y Ordenamiento en Python

### Alumnos:
- Andrés Bonelli
- Matías Herrera

### Profesor: Prof. Cinthia Rigoni
### Tutor: Prof. Brian Lara
### Fecha de Entrega: 9 de Junio de 2025

El proyecto consiste en una comparación práctica de distintos algoritmos para calcular números de Fibonacci, con el objetivo de analizar sus diferencias en cuanto a eficiencia temporal y espacial.

Se desarrollaron cuatro versiones del algoritmo:

- Recursivo puro (exponencial)
- Recursivo con memoización (lineal + uso de caché)
- Iterativo con tabulación (lineal + uso de lista)
- Iterativo optimizado (lineal + espacio constante)

Además, se incluyó una herramienta para medir y comparar los tiempos de ejecución de cada enfoque y visualizar los resultados.

## 🧰 Requisitos

- [Python](https://www.python.org/downloads/) version 3.9 o superior.

## ⬇️ Descargar el repositorio 

```bash
git clone https://github.com/andresbonelli/UTN-TUPaD-Programacion_1-Trabajo-Integrador
```

## ▶️ Ejecución del programa
```bash
python analisis_algoritmos.py
```
o
```bash
python3 analisis_algoritmos.py
```

## 📊 Ejemplo de salida
```plaintext
Fibonacci recursivo: Resultado=832040, Tiempo=0.09398293 segundos.
Fibonacci con memo: Resultado=832040, Tiempo=0.00001788 segundos.
Fibonacci con tabulacion: Resultado=832040, Tiempo=0.00000691 segundos.
Fibonacci optimizado: Resultado=832040, Tiempo=0.00000095 segundos.
```

## 📌 Observaciones
Se utilizó la librería _time_ para mediciones simples de rendimiento.

Para n > 35, el algoritmo recursivo se vuelve impráctico por su complejidad exponencial.

## ▶️ Link al video explicativo

https://www.youtube.com/watch?v=o6Weov3TFaY
