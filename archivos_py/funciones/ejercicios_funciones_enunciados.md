# Ejercicios sobre Funciones en Python
## Nivel Básico e Intermedio

---

## NIVEL BÁSICO

### 1️⃣ Tu primera función
**Enunciado:**
Crea una función llamada `saludar()` que imprima "¡Hola, mundo!".
Luego llámala tres veces.

**Resultado esperado:**
```
¡Hola, mundo!
¡Hola, mundo!
¡Hola, mundo!
```

---

### 2️⃣ Función con parámetros
**Enunciado:**
Crea una función `saludar_persona(nombre)` que reciba un nombre como parámetro e imprima "¡Hola, [nombre]!".

**Ejemplo:**
```
>>> saludar_persona('Ana')
¡Hola, Ana!

>>> saludar_persona('Carlos')
¡Hola, Carlos!
```

---

### 3️⃣ Función que devuelve un valor
**Enunciado:**
Crea una función `suma(a, b)` que reciba dos números y **devuelva** su suma.

**Ejemplo:**
```
>>> resultado = suma(5, 3)
>>> print(resultado)
8

>>> print(suma(10, 20))
30
```

---

### 4️⃣ Área de un cuadrado
**Enunciado:**
Crea una función `area_cuadrado(lado)` que calcule y devuelva el área de un cuadrado.

**Ejemplo:**
```
>>> area_cuadrado(5)
25

>>> area_cuadrado(10)
100
```

---

### 5️⃣ Conversión de temperatura
**Enunciado:**
Crea una función `celsius_a_fahrenheit(celsius)` que convierta grados Celsius a Fahrenheit.

**Fórmula:** F = (C × 9/5) + 32

**Ejemplo:**
```
>>> celsius_a_fahrenheit(0)
32.0

>>> celsius_a_fahrenheit(100)
212.0
```

---

### 6️⃣ Función con múltiples parámetros
**Enunciado:**
Crea una función `presentarse(nombre, edad, ciudad)` que devuelva un string con la presentación de una persona.

**Ejemplo:**
```
>>> presentarse('Juan', 25, 'Madrid')
'Me llamo Juan, tengo 25 años y vivo en Madrid'

>>> presentarse('María', 30, 'Barcelona')
'Me llamo María, tengo 30 años y vivo en Barcelona'
```

---

### 7️⃣ Función que determina paridad
**Enunciado:**
Crea una función `es_par(numero)` que devuelva `True` si el número es par, y `False` si es impar.

**Ejemplo:**
```
>>> es_par(4)
True

>>> es_par(7)
False

>>> es_par(0)
True
```

---

### 8️⃣ Máximo de dos números
**Enunciado:**
Crea una función `maximo(a, b)` que devuelva el número más grande entre dos números. **No puedes usar la función `max()` de Python.**

**Ejemplo:**
```
>>> maximo(5, 10)
10

>>> maximo(-3, -8)
-3

>>> maximo(7, 7)
7
```

---

### 9️⃣ Factorial de un número
**Enunciado:**
Crea una función `factorial(n)` que calcule el factorial de un número usando un bucle.
(El factorial de 5 es 5 × 4 × 3 × 2 × 1 = 120)

**Ejemplo:**
```
>>> factorial(5)
120

>>> factorial(3)
6

>>> factorial(1)
1
```

---

### 1️⃣0️⃣ Función que repite un string
**Enunciado:**
Crea una función `repetir(texto, veces)` que devuelva el texto repetido el número de veces indicado.

**Ejemplo:**
```
>>> repetir('Hola', 3)
'HolaHolaHola'

>>> repetir('*', 5)
'*****'
```

---

## NIVEL INTERMEDIO

### 1️⃣1️⃣ Documentación de funciones (docstring)
**Enunciado:**
Crea una función `sumar_lista(lista)` con documentación (docstring) que:
- Sume todos los números de una lista
- Tenga un docstring explicando qué hace
- Incluya ejemplos en el docstring

**Ejemplo:**
```python
def sumar_lista(lista):
    '''
    Suma todos los números de una lista
    
    >>> sumar_lista([1, 2, 3])
    6
    >>> sumar_lista([10, 20])
    30
    '''
    # Tu código aquí
```

---

### 1️⃣2️⃣ Parámetros por defecto
**Enunciado:**
Crea una función `potencia(base, exponente=2)` que calcule la potencia de un número.
Si no se especifica el exponente, debe ser 2 (cuadrado).

**Ejemplo:**
```
>>> potencia(3)
9

>>> potencia(3, 3)
27

>>> potencia(5, 2)
25
```

---

### 1️⃣3️⃣ Función que devuelve múltiples valores
**Enunciado:**
Crea una función `minimo_maximo(lista)` que devuelva tanto el número mínimo como el máximo de una lista.

**Ejemplo:**
```
>>> minimo, maximo = minimo_maximo([3, 1, 4, 1, 5, 9])
>>> print(minimo, maximo)
1 9

>>> a, b = minimo_maximo([10, 20, 15])
>>> print(a, b)
10 20
```

---

### 1️⃣4️⃣ Función recursiva - Fibonacci
**Enunciado:**
Crea una función recursiva `fibonacci(n)` que devuelva el n-ésimo número de Fibonacci.

La serie es: 0, 1, 1, 2, 3, 5, 8, 13...
Donde cada número es la suma de los dos anteriores.

**Ejemplo:**
```
>>> fibonacci(5)
5

>>> fibonacci(6)
8

>>> fibonacci(0)
0
```

**Pista:** Una función recursiva necesita:
- Caso base (cuándo parar)
- Caso recursivo (llamada a sí misma)

---

### 1️⃣5️⃣ Verificar contraseña
**Enunciado:**
Crea una función `es_contraseña_valida(contraseña)` que verifique si una contraseña cumple estos requisitos:
- Tiene al menos 8 caracteres
- Contiene al menos una mayúscula
- Contiene al menos un número

Devuelve `True` o `False`.

**Ejemplo:**
```
>>> es_contraseña_valida('abc123')
False  # Menos de 8 caracteres

>>> es_contraseña_valida('Abc12345')
True

>>> es_contraseña_valida('abcd1234')
False  # Sin mayúscula
```

---

### 1️⃣6️⃣ Calculadora simple
**Enunciado:**
Crea una función `calcular(a, b, operacion)` que realice operaciones matemáticas.
El parámetro `operacion` será un string: '+', '-', '*' o '/'.

**Ejemplo:**
```
>>> calcular(10, 5, '+')
15

>>> calcular(10, 5, '-')
5

>>> calcular(10, 5, '*')
50

>>> calcular(10, 5, '/')
2.0
```

**Manejo de errores:** Si la operación es desconocida, devuelve `None` o un mensaje de error.

---

### 1️⃣7️⃣ Aplicar función a una lista
**Enunciado:**
Crea una función `aplicar_a_todos(funcion, lista)` que:
- Reciba una función y una lista
- Aplique la función a cada elemento de la lista
- Devuelva una nueva lista con los resultados

**Ejemplo:**
```python
def doble(x):
    return x * 2

>>> aplicar_a_todos(doble, [1, 2, 3])
[2, 4, 6]

def cuadrado(x):
    return x ** 2

>>> aplicar_a_todos(cuadrado, [1, 2, 3, 4])
[1, 4, 9, 16]
```

---

### 1️⃣8️⃣ Contar palabras que cumplen condición
**Enunciado:**
Crea una función `contar_si(condicion, lista)` que:
- Reciba una función (condición) y una lista
- Cuente cuántos elementos cumplen la condición
- Devuelva el conteo

**Ejemplo:**
```python
def es_mayor_que_5(x):
    return x > 5

>>> contar_si(es_mayor_que_5, [3, 6, 2, 8, 4, 9])
3  # Hay 3 números mayores que 5

def es_par(x):
    return x % 2 == 0

>>> contar_si(es_par, [1, 2, 3, 4, 5, 6])
3  # Hay 3 números pares
```

---

### 1️⃣9️⃣ Análisis de texto
**Enunciado:**
Crea una función `analizar_texto(texto)` que devuelva un diccionario con:
- Número de caracteres
- Número de palabras
- Número de líneas
- Número de vocales

**Ejemplo:**
```python
>>> resultado = analizar_texto("Hola\nMundo")
>>> resultado['caracteres']
10
>>> resultado['palabras']
2
>>> resultado['lineas']
2
>>> resultado['vocales']
3
```

---

### 2️⃣0️⃣ Variables locales y globales
**Enunciado:**
Responde las preguntas y crea funciones que demuestren tu comprensión:

1. ¿Cuál es la diferencia entre variable local y global?
2. Crea una función que use una variable local
3. Crea una función que intente modificar una variable global (y observa qué ocurre)

**Ejemplo:**
```python
contador = 0  # Variable global

def incrementar():
    contador += 1  # ¿Qué ocurre aquí?
    return contador

incrementar()  # ¿Qué error aparece?
```

---

### 2️⃣1️⃣ Funciones anidadas
**Enunciado:**
Crea una función externa que contenga funciones internas (anidadas).

**Ejemplo:**
```python
def operaciones(x, y):
    
    def suma():
        return x + y
    
    def resta():
        return x - y
    
    def multiplicacion():
        return x * y
    
    return suma(), resta(), multiplicacion()

>>> operaciones(10, 5)
(15, 5, 50)
```

---

### 2️⃣2️⃣ Función que valida datos
**Enunciado:**
Crea una función `validar_edad(edad)` que:
- Verifique que sea un número entero
- Devuelva `True` si es válida (0-150)
- Devuelva `False` en caso contrario

**Intenta también:**
Crea `validar_email(email)` que compruebe que contiene '@' y '.'

---

### 2️⃣3️⃣ Generar serie
**Enunciado:**
Crea una función `generar_serie(inicio, fin, paso=1)` que devuelva una lista con números desde inicio hasta fin.

**Ejemplo:**
```
>>> generar_serie(1, 5)
[1, 2, 3, 4, 5]

>>> generar_serie(0, 10, 2)
[0, 2, 4, 6, 8, 10]

>>> generar_serie(10, 1, -1)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

---

### 2️⃣4️⃣ Memoización (optimización)
**Enunciado:**
La función de Fibonacci del ejercicio 14 es muy lenta para números grandes.
Crea una versión mejorada usando memoización (guardar resultados ya calculados).

**Pista:** Usa un diccionario para guardar resultados.

```python
def fibonacci_rapido(n, memo={}):
    if n in memo:
        return memo[n]
    
    # Tu código aquí
    resultado = ...
    memo[n] = resultado
    return resultado
```

---

### 2️⃣5️⃣ Desafío: Juego interactivo
**Enunciado:**
Crea un sistema de funciones para un juego de adivinanza:

```python
def nuevo_juego():
    # Inicia un nuevo juego
    pass

def hacer_intento(numero):
    # Recibe un intento
    # Devuelve si es correcto, muy alto o muy bajo
    pass

def obtener_estadisticas():
    # Devuelve cuántos intentos hizo
    pass
```

El programa debe:
- Elegir un número al azar (1-100)
- Permitir múltiples intentos
- Dar pistas ("muy alto", "muy bajo")
- Contar los intentos
- Permitir jugar de nuevo

---

