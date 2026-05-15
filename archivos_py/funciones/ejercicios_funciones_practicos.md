# Ejercicios Prácticos - Funciones en Python
## Actividades para clase y evaluación

---

## 🎯 EJERCICIOS QUICK (5-10 minutos cada uno)

Ideales para repaso rápido o evaluación formativa.

### QA1: Llamar funciones
```python
# Completa el código
def saludar(nombre):
    print(f"Hola, {nombre}")

# Llama la función con tu nombre
# Tu código aquí
```

**Solución:**
```python
saludar('Juan')
```

---

### QA2: Return vs Print
```python
# ¿Cuál es la diferencia?

def funcion1(x):
    print(x * 2)

def funcion2(x):
    return x * 2

resultado1 = funcion1(5)  # ¿Qué es resultado1?
resultado2 = funcion2(5)  # ¿Qué es resultado2?

print(resultado1)  # ¿Qué imprime?
print(resultado2)  # ¿Qué imprime?
```

**Respuestas esperadas:**
```
10        # resultado1 imprime pero resultado1 = None
10        # resultado2 devuelve 10
None      # resultado1 es None
10        # resultado2 es 10
```

---

### QA3: Parámetros por defecto
```python
# Completa la función
def crear_usuario(nombre, edad=18):
    return f"{nombre} tiene {edad} años"

# Llamadas
print(crear_usuario('Ana'))           # ¿Resultado?
print(crear_usuario('Bob', 25))       # ¿Resultado?
print(crear_usuario('Clara', 30))     # ¿Resultado?
```

**Resultados esperados:**
```
Ana tiene 18 años
Bob tiene 25 años
Clara tiene 30 años
```

---

### QA4: Múltiples parámetros
```python
def area_rectangulo(base, altura):
    return base * altura

# Completa las llamadas
# Calcula el área de un rectángulo de 5x3
# Calcula el área de un rectángulo de 10x7
```

**Solución:**
```python
print(area_rectangulo(5, 3))   # 15
print(area_rectangulo(10, 7))  # 70
```

---

### QA5: Condicionales en funciones
```python
def es_positivo(numero):
    if numero > 0:
        return True
    else:
        return False

# Simplifica esta función en una sola línea
# Pista: return puede devolver directamente la comparación

# Tu código aquí
```

**Solución:**
```python
def es_positivo(numero):
    return numero > 0
```

---

## 📝 EJERCICIOS DE PROGRAMACIÓN (15-30 minutos)

### PA1: Función de descuento
**Enunciado:**
Crea una función `aplicar_descuento(precio, descuento=10)` que:
- Reciba un precio y un porcentaje de descuento (por defecto 10%)
- Devuelva el precio final con descuento aplicado

**Ejemplo:**
```
>>> aplicar_descuento(100)
90.0

>>> aplicar_descuento(100, 20)
80.0

>>> aplicar_descuento(50, 5)
47.5
```

**Pista:** Precio final = Precio × (1 - descuento/100)

---

### PA2: Validador de número PIN
**Enunciado:**
Crea una función `validar_pin(pin)` que:
- Verifique que el PIN tenga exactamente 4 dígitos
- Todos sean números
- Devuelva True o False

**Ejemplo:**
```
>>> validar_pin('1234')
True

>>> validar_pin('12345')
False

>>> validar_pin('123a')
False

>>> validar_pin('123')
False
```

---

### PA3: Estadísticas de notas
**Enunciado:**
Crea funciones para analizar notas:

```python
def calcular_promedio(notas):
    # Devuelve el promedio

def nota_mas_alta(notas):
    # Devuelve la nota máxima

def nota_mas_baja(notas):
    # Devuelve la nota mínima

def contar_aprobados(notas, minimo=6):
    # Devuelve cuántas notas >= minimo
```

**Ejemplo de uso:**
```python
notas = [7, 8, 5, 9, 6, 8]

print(f"Promedio: {calcular_promedio(notas)}")
print(f"Máxima: {nota_mas_alta(notas)}")
print(f"Mínima: {nota_mas_baja(notas)}")
print(f"Aprobados: {contar_aprobados(notas)}")
```

---

### PA4: Convertidor de temperaturas
**Enunciado:**
Crea funciones para convertir temperaturas:

```python
def celsius_a_fahrenheit(celsius):
    # Tu código

def fahrenheit_a_celsius(fahrenheit):
    # Tu código

def celsius_a_kelvin(celsius):
    # Tu código
```

**Fórmulas:**
- C → F: F = (C × 9/5) + 32
- F → C: C = (F - 32) × 5/9
- C → K: K = C + 273.15

**Ejemplo:**
```
>>> celsius_a_fahrenheit(0)
32.0

>>> fahrenheit_a_celsius(32)
0.0

>>> celsius_a_kelvin(0)
273.15
```

---

### PA5: Generador de contraseña
**Enunciado:**
Crea una función `generar_contraseña(longitud=8)` que:
- Genere una contraseña aleatoria
- De la longitud especificada
- Con una mezcla de mayúsculas, minúsculas, números y símbolos

**Hint:** Usa `random` y `string`

```python
import random
import string

def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(caracteres) for _ in range(longitud))
```

---

## 🏆 EJERCICIOS DE DESAFÍO (30-45 minutos)

### DA1: Conversión de sistemas numéricos
**Enunciado:**
Crea funciones para convertir entre sistemas numéricos:

```python
def decimal_a_binario(numero):
    # Convierte decimal a binario

def binario_a_decimal(binario_str):
    # Convierte binario a decimal

def decimal_a_hexadecimal(numero):
    # Convierte decimal a hexadecimal
```

**Ejemplo:**
```
>>> decimal_a_binario(10)
'1010'

>>> binario_a_decimal('1010')
10

>>> decimal_a_hexadecimal(255)
'ff'
```

---

### DA2: Gestor de contactos
**Enunciado:**
Crea un sistema de funciones para gestionar contactos:

```python
contactos = {}  # Diccionario global

def agregar_contacto(nombre, telefono, email):
    # Agrega un contacto

def obtener_contacto(nombre):
    # Devuelve info del contacto

def listar_contactos():
    # Devuelve todos los contactos

def eliminar_contacto(nombre):
    # Elimina un contacto

def buscar_por_telefono(telefono):
    # Busca por número de teléfono
```

---

### DA3: Calculadora científica
**Enunciado:**
Crea funciones para operaciones matemáticas avanzadas:

```python
from math import sqrt, sin, cos, pi

def raiz_cuadrada(numero):
    pass

def seno(angulo_grados):
    # Convertir grados a radianes
    pass

def coseno(angulo_grados):
    pass

def distancia_entre_puntos(x1, y1, x2, y2):
    # Fórmula: d = sqrt((x2-x1)^2 + (y2-y1)^2)
    pass
```

---

### DA4: Analizador de texto avanzado
**Enunciado:**
Crea funciones para análisis profundo de texto:

```python
def contar_palabras(texto):
    # Número de palabras

def palabra_mas_comun(texto):
    # Devuelve la palabra que más se repite

def promedio_longitud_palabra(texto):
    # Promedio de caracteres por palabra

def es_pangrama(texto):
    # Verifica si contiene todas las letras

def contar_repeticiones_palabra(texto, palabra):
    # Cuántas veces aparece una palabra
```

---

### DA5: Sistema de puntuación (gamificación)
**Enunciado:**
Crea un sistema de puntuación para un juego:

```python
jugadores = {}  # {nombre: puntuación}

def registrar_jugador(nombre):
    # Crea un jugador con 0 puntos

def sumar_puntos(nombre, puntos):
    # Suma puntos a un jugador

def obtener_ranking():
    # Devuelve jugadores ordenados por puntos

def obtener_estadisticas(nombre):
    # Devuelve info del jugador

def reiniciar_juego():
    # Borra todos los datos
```

---

## 📊 RÚBRICA DE EVALUACIÓN

### Criterios básicos (0-10 puntos):
- ✓ La función funciona sin errores (4 puntos)
- ✓ Tiene parámetros apropiados (2 puntos)
- ✓ Devuelve los valores correctos (2 puntos)
- ✓ Tiene docstring/comentarios (2 puntos)

### Criterios intermedios (extra):
- ✓ Maneja excepciones (+1 punto)
- ✓ Usa parámetros por defecto (+1 punto)
- ✓ Código limpio y legible (+1 punto)
- ✓ Eficiente (no repeticiones) (+1 punto)

---

## 💡 ACTIVIDADES PARA CLASE

### Actividad 1: Detección de errores
Muestra código con errores y pide que los identifiquen:

```python
# Error 1: Falta parámetro
def sumar(a, b):
    return a + b

resultado = sumar(5)  # ¿Qué error?

# Error 2: Sin return
def multiplicar(a, b):
    a * b

print(multiplicar(3, 4))  # ¿Qué imprime?

# Error 3: Scope
contador = 0

def incrementar():
    contador += 1  # ¿Qué error?

# Error 4: Parámetro por defecto
def func(a=1, b):  # ¿Qué error?
    pass
```

---

### Actividad 2: Refactorización
Muestra código sin funciones y pide que lo refactorice:

```python
# Original (sin funciones)
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
ciudad = input("¿Dónde vives? ")

print(f"Te llamas {nombre}")
print(f"Tienes {edad} años")
print(f"Vives en {ciudad}")

# Refactorizar con funciones
```

---

### Actividad 3: Competencia de programación
Crea una serie de ejercicios de dificultad creciente:

**Nivel 1:** Función simple (2 min)
```python
# Crea función que devuelva el doble de un número
```

**Nivel 2:** Con condicionales (3 min)
```python
# Crea función que determine si es mayor/menor de edad
```

**Nivel 3:** Con bucles (5 min)
```python
# Crea función que calcule factorial
```

---

### Actividad 4: Preguntas de comprensión

1. ¿Qué diferencia hay entre `return` y `print`?
2. ¿Cuándo deberías usar parámetros por defecto?
3. ¿Qué es una función recursiva? Da un ejemplo.
4. ¿Cuál es la diferencia entre parámetro y argumento?
5. ¿Por qué es buena práctica devolver valores en lugar de modificar globales?

---

## 🎓 PROYECTO INTEGRADOR

Crea un "Sistema de biblioteca" usando funciones:

```python
# Base de datos simulada
libros = [
    {'titulo': 'Python 101', 'autor': 'John Doe', 'disponible': True},
    {'titulo': '1984', 'autor': 'George Orwell', 'disponible': False},
]

# Funciones necesarias:
def agregar_libro(titulo, autor):
    pass

def buscar_libro(titulo):
    pass

def prestar_libro(titulo):
    pass

def devolver_libro(titulo):
    pass

def listar_disponibles():
    pass

def estadisticas():
    pass

# Menú interactivo
def menu():
    while True:
        print("""
        1. Agregar libro
        2. Buscar libro
        3. Prestar libro
        4. Devolver libro
        5. Ver disponibles
        6. Estadísticas
        7. Salir
        """)
        # Procesar opción
```

---

