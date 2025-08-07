# Calculadora en Python

Proyecto de calculadora escrita en Python. 
El objetivo es permitir al usuario realizar operaciones matemáticas básicas y combinadas de forma sencilla.

## Características

La calculadora incluye las siguientes funciones:

- Menú interactivo para elegir la operación deseada
- Suma de dos números
- Resta del segundo número al primero
- Multiplicación de dos números
- División del primer número entre el segundo
- Operación módulo entre dos números
- Suma de tres números
- Combinacion de operaciones con 3 o más números


## Estructura del proyecto

El código está dividido en dos partes:

### Primera parte: Suma básica
Solicita dos números al usuario y muestra el resultado de su suma.
```
n1 = float(input("Escribe el primer número: "))
n2 = float(input("Escribe el segundo número: "))
print(f"{n1} + {n2} = {n1 + n2}")
```

### Segunda parte: Funciones y menú interactivo
Define funciones para cada operación y despliega un menú para que el usuario elija qué desea hacer.
Funciones disponibles:
```
- suma(a, b)
- resta(a, b)
- multiplicacion(a, b)
- division(a, b)
- modulo(a, b)
- suma3(a, b, c)
- expresion_libre(expr) → Usa eval() para interpretar expresiones como texto
```

### Consideraciones
• 	La división entre cero está controlada para evitar errores.
• 	Las expresiones libres se evalúan con , por lo que se recomienda ingresar operaciones válidas y seguras.

### Requisitos
• 	Python 3.x
• 	Terminal o consola para ejecutar el script

### Ejecución
Para ejecutar el programa, simplemente corre el archivo en tu terminal:
```python calculadora.py```

### 🧠 Asistencia con IA

Este proyecto fue desarrollado con el apoyo de herramientas de inteligencia artificial, que ayudaron a:

- Generar ideas para la estructura del programa y archivo README
- Validar la lógica de las funciones matemáticas
- Generar ideas para realizar las operaciones combinadas

La colaboración con IA permitió acelerar el desarrollo y mejorar la calidad del código y la documentación.
