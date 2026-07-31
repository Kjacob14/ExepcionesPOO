# ExepcionesPOO

Práctica de manejo de excepciones en Python. Incluye 10 ejercicios que cubren el uso de `try/except`, excepciones específicas (`ZeroDivisionError`, `IndexError`, `KeyError`, `ValueError`, `TypeError`), el uso de `raise`, y la creación de excepciones personalizadas con clases propias.

## Requisitos

Python 3.14.5 (versión usada para el desarrollo y prueba de estos ejercicios)

Puedes verificar la versión instalada con el comando:


python --version


No se requieren librerías externas, todo el código usa únicamente la biblioteca estándar de Python.

## Contenido

| Archivo | Descripción |
|---|---|
| `ejercicio1.py` | División entre dos números, maneja `ZeroDivisionError`. |
| `ejercicio2.py` | Acceso a una lista de colores por índice, maneja `IndexError`. |
| `ejercicio3.py` | Consulta de inventario de medicamentos por nombre, maneja `KeyError`. |
| `ejercicio4.py` | Conversión de edad ingresada por teclado, maneja `ValueError` con reintento (`while True`). |
| `ejercicio5.py` | Suma de dos valores, maneja `TypeError` al mezclar tipos incompatibles. |
| `ejercicio6.py` | Registro de edad con validación manual usando `raise ValueError`. |
| `ejercicio7.py` | Venta de medicamentos con validación de stock usando `raise Exception`. |
| `ejercicio8.py` | Registro de calificaciones, valida rango de 0 a 10 con `raise ValueError`. |
| `ejercicio9.py` | Venta de medicamentos con excepción personalizada `StockInsuficienteError`. |
| `ejercicio10.py` | Validación de formato de correo electrónico, maneja `ValueError` personalizado. |
