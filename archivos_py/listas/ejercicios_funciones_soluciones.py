# Soluciones - Ejercicios sobre Funciones en Python
## Nivel Básico e Intermedio

---

## NIVEL BÁSICO

### 1️⃣ Tu primera función - SOLUCIÓN

```python
# Definimos la función
def saludar():
    print("¡Hola, mundo!")

# Llamamos la función tres veces
saludar()
saludar()
saludar()
```

**Salida:**
```
¡Hola, mundo!
¡Hola, mundo!
¡Hola, mundo!
```

**Conceptos clave:**
- `def` define una función
- El cuerpo de la función está indentado
- Sin `()` no se ejecuta, se necesita `saludar()` para llamarla
- Puedes llamarla múltiples veces

---

### 2️⃣ Función con parámetros - SOLUCIÓN

```python
def saludar_persona(nombre):
    """Saluda a una persona por su nombre"""
    print(f"¡Hola, {nombre}!")

# Llamamos con diferentes parámetros
saludar_persona('Ana')
saludar_persona('Carlos')
saludar_persona('María')
```

**Salida:**
```
¡Hola, Ana!
¡Hola, Carlos!
¡Hola, María!
```

**Conceptos clave:**
- `nombre` es el parámetro (variable dentro de la función)
- `'Ana'` es el argumento (valor que pasamos)
- f-strings permiten insertar variables: `f"Texto {variable}"`

---

### 3️⃣ Función que devuelve un valor - SOLUCIÓN

```python
def suma(a, b):
    """Suma dos números y devuelve el resultado"""
    resultado = a + b
    return resultado

# Forma 1: Guardar el resultado en una variable
resultado = suma(5, 3)
print(resultado)  # 8

# Forma 2: Usar directamente el resultado
print(suma(10, 20))  # 30

# Forma 3: Más compacta (sin variable intermedia)
def suma(a, b):
    return a + b
```

**Conceptos clave:**
- `return` devuelve el valor de la función
- Puedes guardar el resultado o usarlo directamente
- La función sin `return` devuelve `None`

---

### 4️⃣ Área de un cuadrado - SOLUCIÓN

```python
def area_cuadrado(lado):
    """Calcula el área de un cuadrado"""
    area = lado * lado
    return area

# Pruebas
print(area_cuadrado(5))   # 25
print(area_cuadrado(10))  # 100

# Versión más compacta
def area_cuadrado(lado):
    return lado ** 2  # O: lado * lado
```

**Conceptos clave:**
- `**` es el operador de potencia
- `lado * lado` es equivalente a `lado ** 2`

---

### 5️⃣ Conversión de temperatura - SOLUCIÓN

```python
def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Pruebas
print(celsius_a_fahrenheit(0))    # 32.0
print(celsius_a_fahrenheit(100))  # 212.0
print(celsius_a_fahrenheit(-40))  # -40.0

# Versión compacta
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
```

**Conceptos clave:**
- Aplicar fórmula matemática dentro de una función
- Importancia del orden de operaciones (paréntesis)

---

### 6️⃣ Función con múltiples parámetros - SOLUCIÓN

```python
def presentarse(nombre, edad, ciudad):
    """Crea una presentación personalizada"""
    mensaje = f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}"
    return mensaje

# Pruebas
print(presentarse('Juan', 25, 'Madrid'))
print(presentarse('María', 30, 'Barcelona'))
print(presentarse('Pedro', 28, 'Valencia'))
```

**Salida:**
```
Me llamo Juan, tengo 25 años y vivo en Madrid
Me llamo María, tengo 30 años y vivo en Barcelona
Me llamo Pedro, tengo 28 años y vivo en Valencia
```

**Conceptos clave:**
- Múltiples parámetros separados por comas
- El orden importa cuando llamas la función
- f-strings con múltiples variables

---

### 7️⃣ Función que determina paridad - SOLUCIÓN

```python
def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0

# Pruebas
print(es_par(4))   # True
print(es_par(7))   # False
print(es_par(0))   # True
print(es_par(-5))  # False
print(es_par(-8))  # True
```

**Conceptos clave:**
- Operador módulo `%` devuelve el resto
- `==` compara y devuelve True o False
- La función devuelve directamente el resultado booleano

---

### 8️⃣ Máximo de dos números - SOLUCIÓN

**Método 1: Con if-else**
```python
def maximo(a, b):
    """Devuelve el número más grande"""
    if a > b:
        return a
    else:
        return b

# Pruebas
print(maximo(5, 10))    # 10
print(maximo(-3, -8))   # -3
print(maximo(7, 7))     # 7
```

**Método 2: Con operador ternario (más compacto)**
```python
def maximo(a, b):
    return a if a > b else b
```

**Método 3: Forma Pythónica (si se permite usar max())**
```python
def maximo(a, b):
    return max(a, b)
```

**Conceptos clave:**
- Operador ternario: `valor_si_verdadero if condicion else valor_si_falso`
- Es más compacto que if-else

---

### 9️⃣ Factorial de un número - SOLUCIÓN

**Método 1: Con un bucle for**
```python
def factorial(n):
    """Calcula el factorial de un número"""
    resultado = 1
    
    for i in range(1, n + 1):
        resultado = resultado * i
    
    return resultado

# Pruebas
print(factorial(5))  # 120 (5*4*3*2*1)
print(factorial(3))  # 6   (3*2*1)
print(factorial(1))  # 1
print(factorial(0))  # 1   (por convención)
```

**Método 2: Con while**
```python
def factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado
```

**Método 3: Recursivo (más avanzado)**
```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```

**Conceptos clave:**
- Variable acumuladora: `resultado = 1`
- `range(1, n + 1)` genera números del 1 al n (inclusive)
- `*=` es equivalente a `resultado = resultado * i`

---

### 1️⃣0️⃣ Función que repite un string - SOLUCIÓN

```python
def repetir(texto, veces):
    """Repite un texto el número de veces indicado"""
    return texto * veces

# Pruebas
print(repetir('Hola', 3))   # HolaHolaHola
print(repetir('*', 5))      # *****
print(repetir('ab', 4))     # abababab

# Alternativa con un bucle (menos eficiente)
def repetir(texto, veces):
    resultado = ""
    for i in range(veces):
        resultado += texto
    return resultado
```

**Conceptos clave:**
- En Python, `"texto" * 3` repite el string
- Es más eficiente que usar bucles
- Esto funciona también con listas: `[1, 2] * 3` da `[1, 2, 1, 2, 1, 2]`

---

## NIVEL INTERMEDIO

### 1️⃣1️⃣ Documentación de funciones (docstring) - SOLUCIÓN

```python
def sumar_lista(lista):
    """
    Suma todos los números de una lista.
    
    Parámetros:
        lista: una lista de números
    
    Retorna:
        Un número entero o float con la suma total
    
    Ejemplos:
        >>> sumar_lista([1, 2, 3])
        6
        >>> sumar_lista([10, 20])
        30
        >>> sumar_lista([])
        0
    """
    total = 0
    for numero in lista:
        total += numero
    return total

# Pruebas
print(sumar_lista([1, 2, 3]))     # 6
print(sumar_lista([10, 20]))      # 30
print(sumar_lista([]))            # 0

# Ver el docstring
print(sumar_lista.__doc__)
help(sumar_lista)
```

**Conceptos clave:**
- Docstring es un string triple entre comillas: `""" """ `
- Se coloca inmediatamente después de `def`
- Explica qué hace, parámetros, qué devuelve y ejemplos
- Accesible via `__doc__` o `help()`

---

### 1️⃣2️⃣ Parámetros por defecto - SOLUCIÓN

```python
def potencia(base, exponente=2):
    """
    Calcula la potencia de un número.
    
    Si no se especifica el exponente, asume 2 (cuadrado).
    """
    return base ** exponente

# Pruebas
print(potencia(3))        # 9   (3^2)
print(potencia(3, 3))     # 27  (3^3)
print(potencia(5, 2))     # 25  (5^2)
print(potencia(2, 8))     # 256 (2^8)

# Otro ejemplo
def imprimir_mensaje(mensaje, veces=1):
    for i in range(veces):
        print(mensaje)

imprimir_mensaje("Hola")       # Imprime 1 vez
imprimir_mensaje("Hola", 3)    # Imprime 3 veces
```

**Conceptos clave:**
- `exponente=2` establece un valor por defecto
- Si no pasas el parámetro, usa el valor por defecto
- Parámetros sin defecto deben venir antes
- ❌ `def f(a=1, b):` - INCORRECTO
- ✓ `def f(a, b=1):` - CORRECTO

---

### 1️⃣3️⃣ Función que devuelve múltiples valores - SOLUCIÓN

```python
def minimo_maximo(lista):
    """Devuelve el mínimo y máximo de una lista"""
    minimo = min(lista)
    maximo = max(lista)
    return minimo, maximo

# Desempaquetar los valores
minimo, maximo = minimo_maximo([3, 1, 4, 1, 5, 9])
print(minimo, maximo)  # 1 9

# Otra forma
resultado = minimo_maximo([10, 20, 15])
print(resultado)  # (10, 20) - una tupla

# Acceder a cada valor
print(resultado[0])  # 10
print(resultado[1])  # 20

# Versión sin funciones incorporadas
def minimo_maximo(lista):
    minimo = lista[0]
    maximo = lista[0]
    
    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero
    
    return minimo, maximo
```

**Conceptos clave:**
- Una función puede devolver múltiples valores separados por coma
- Python automáticamente crea una tupla
- Puedes desempaquetar: `a, b = funcion()`
- O acceder como tupla: `tupla[0]`, `tupla[1]`

---

### 1️⃣4️⃣ Función recursiva - Fibonacci - SOLUCIÓN

**Método 1: Recursión simple (pero lenta)**
```python
def fibonacci(n):
    """
    Devuelve el n-ésimo número de Fibonacci.
    
    Serie: 0, 1, 1, 2, 3, 5, 8, 13, 21...
    """
    # Caso base
    if n <= 1:
        return n
    # Caso recursivo
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pruebas
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(5))   # 5
print(fibonacci(6))   # 8
print(fibonacci(7))   # 13
```

**Método 2: Iterativo (más eficiente)**
```python
def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci(10))  # 55 (rápido)
```

**Método 3: Recursivo con memoización (rápido)**
```python
def fibonacci(n, memo={}):
    """Fibonacci optimizado con memoización"""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(30))  # Rápido incluso para números grandes
```

**Conceptos clave:**
- Recursión: la función se llama a sí misma
- Necesita un caso base (cuándo parar)
- Necesita un caso recursivo (llamada a sí misma)
- La recursión simple es lenta (calcula lo mismo muchas veces)
- Memoización guarda resultados para no recalcular

---

### 1️⃣5️⃣ Verificar contraseña - SOLUCIÓN

```python
def es_contraseña_valida(contraseña):
    """
    Valida si una contraseña cumple los requisitos:
    - Al menos 8 caracteres
    - Al menos una mayúscula
    - Al menos un número
    """
    # Verificar longitud
    if len(contraseña) < 8:
        return False
    
    # Verificar si tiene mayúscula
    tiene_mayuscula = False
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
            break
    
    if not tiene_mayuscula:
        return False
    
    # Verificar si tiene número
    tiene_numero = False
    for caracter in contraseña:
        if caracter.isdigit():
            tiene_numero = True
            break
    
    if not tiene_numero:
        return False
    
    # Si pasó todas las verificaciones
    return True

# Pruebas
print(es_contraseña_valida('abc123'))       # False (< 8 caracteres)
print(es_contraseña_valida('Abc12345'))     # True
print(es_contraseña_valida('abcd1234'))     # False (sin mayúscula)
print(es_contraseña_valida('ABCD1234'))     # True
```

**Versión más compacta (con `any()`):**
```python
def es_contraseña_valida(contraseña):
    return (
        len(contraseña) >= 8 and
        any(c.isupper() for c in contraseña) and
        any(c.isdigit() for c in contraseña)
    )
```

**Conceptos clave:**
- `isupper()` verifica si es mayúscula
- `isdigit()` verifica si es dígito
- `any()` devuelve True si al menos un elemento cumple la condición

---

### 1️⃣6️⃣ Calculadora simple - SOLUCIÓN

```python
def calcular(a, b, operacion):
    """
    Realiza una operación matemática.
    
    Operaciones válidas: '+', '-', '*', '/'
    """
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        if b == 0:
            return "Error: división por cero"
        return a / b
    else:
        return "Error: operación desconocida"

# Pruebas
print(calcular(10, 5, '+'))   # 15
print(calcular(10, 5, '-'))   # 5
print(calcular(10, 5, '*'))   # 50
print(calcular(10, 5, '/'))   # 2.0
print(calcular(10, 0, '/'))   # Error: división por cero
```

**Versión con diccionario (más elegante):**
```python
def calcular(a, b, operacion):
    operaciones = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error"
    }
    
    if operacion in operaciones:
        return operaciones[operacion](a, b)
    else:
        return "Error: operación desconocida"
```

**Conceptos clave:**
- Usar diccionarios para mapear operaciones
- Lambda es una función anónima: `lambda x, y: x + y`

---

### 1️⃣7️⃣ Aplicar función a una lista - SOLUCIÓN

```python
def aplicar_a_todos(funcion, lista):
    """Aplica una función a cada elemento de una lista"""
    resultado = []
    
    for elemento in lista:
        resultado.append(funcion(elemento))
    
    return resultado

# Ejemplo 1: Duplicar
def doble(x):
    return x * 2

print(aplicar_a_todos(doble, [1, 2, 3]))  # [2, 4, 6]

# Ejemplo 2: Cuadrado
def cuadrado(x):
    return x ** 2

print(aplicar_a_todos(cuadrado, [1, 2, 3, 4]))  # [1, 4, 9, 16]

# Ejemplo 3: Con lambda
print(aplicar_a_todos(lambda x: x * 3, [1, 2, 3]))  # [3, 6, 9]
```

**Versión con list comprehension (más Pythónica):**
```python
def aplicar_a_todos(funcion, lista):
    return [funcion(elemento) for elemento in lista]
```

**Versión con map() (built-in):**
```python
def aplicar_a_todos(funcion, lista):
    return list(map(funcion, lista))
```

**Conceptos clave:**
- Funciones como parámetros (función de orden superior)
- Lambda para funciones anónimas rápidas
- List comprehension es Pythónica y eficiente

---

### 1️⃣8️⃣ Contar palabras que cumplen condición - SOLUCIÓN

```python
def contar_si(condicion, lista):
    """Cuenta cuántos elementos cumplen la condición"""
    contador = 0
    
    for elemento in lista:
        if condicion(elemento):
            contador += 1
    
    return contador

# Ejemplo 1: Números mayores que 5
def es_mayor_que_5(x):
    return x > 5

print(contar_si(es_mayor_que_5, [3, 6, 2, 8, 4, 9]))  # 3

# Ejemplo 2: Números pares
def es_par(x):
    return x % 2 == 0

print(contar_si(es_par, [1, 2, 3, 4, 5, 6]))  # 3

# Ejemplo 3: Con lambda
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contar_si(lambda x: x > 5, numeros))  # 5
```

**Versión compacta con sum() y generator:**
```python
def contar_si(condicion, lista):
    return sum(1 for elemento in lista if condicion(elemento))
```

**Conceptos clave:**
- `sum(1 for ... if ...)` es compacta y eficiente
- Generator expression (similar a list comprehension pero sin crear lista)

---

### 1️⃣9️⃣ Análisis de texto - SOLUCIÓN

```python
def analizar_texto(texto):
    """Analiza un texto y devuelve estadísticas"""
    
    # Caracteres (incluyendo espacios y saltos de línea)
    caracteres = len(texto)
    
    # Palabras (dividiendo por espacios)
    palabras = len(texto.split())
    
    # Líneas
    lineas = len(texto.split('\n'))
    
    # Vocales
    vocales = 0
    for caracter in texto.lower():
        if caracter in 'aeiou':
            vocales += 1
    
    # Retornar diccionario
    return {
        'caracteres': caracteres,
        'palabras': palabras,
        'lineas': lineas,
        'vocales': vocales
    }

# Prueba
texto = "Hola\nMundo"
resultado = analizar_texto(texto)

print(resultado['caracteres'])  # 10 (H o l a \n M u n d o)
print(resultado['palabras'])    # 2
print(resultado['lineas'])      # 2
print(resultado['vocales'])     # 3 (o, a, u)
```

**Versión con métodos de string:**
```python
def analizar_texto(texto):
    import re
    
    return {
        'caracteres': len(texto),
        'palabras': len(texto.split()),
        'lineas': texto.count('\n') + 1,
        'vocales': sum(1 for c in texto.lower() if c in 'aeiou')
    }
```

**Conceptos clave:**
- `.split()` divide por espacios por defecto
- `.split('\n')` divide por líneas
- Devolver diccionario es útil para múltiples valores nombrados
- `.lower()` convierte a minúsculas

---

### 2️⃣0️⃣ Variables locales y globales - SOLUCIÓN

```python
# Variable global
contador = 0

def incrementar():
    """Intenta modificar la variable global"""
    # Esto causa error: UnboundLocalError
    contador += 1
    return contador

try:
    incrementar()
except UnboundLocalError as e:
    print(f"Error: {e}")

# ❌ Forma incorrecta
# contador += 1 trata contador como local, pero aún no está definida

# ✓ Forma correcta 1: Usar 'global'
def incrementar():
    global contador  # Declara que usaremos la global
    contador += 1
    return contador

print(incrementar())  # 1
print(incrementar())  # 2

# ✓ Forma correcta 2: Devolver el valor
contador = 0

def incrementar(valor):
    return valor + 1

contador = incrementar(contador)
print(contador)  # 1

# Ejemplo de variable local
def funcion_local():
    variable_local = 10  # Solo existe dentro de la función
    print(variable_local)

funcion_local()  # Funciona
# print(variable_local)  # Error: no existe fuera
```

**Conceptos clave:**
- Variable **local**: creada dentro de la función, solo existe ahí
- Variable **global**: creada fuera, accesible desde cualquier lado
- `global palabra_clave` permite modificar global desde función
- Mejor práctica: devolver valores en lugar de modificar globales

---

### 2️⃣1️⃣ Funciones anidadas - SOLUCIÓN

```python
def operaciones(x, y):
    """Contiene funciones internas (anidadas)"""
    
    # Funciones internas
    def suma():
        return x + y
    
    def resta():
        return x - y
    
    def multiplicacion():
        return x * y
    
    def division():
        if y != 0:
            return x / y
        else:
            return "Error: división por cero"
    
    # Devolver tupla con los resultados
    return suma(), resta(), multiplicacion(), division()

# Prueba
print(operaciones(10, 5))  # (15, 5, 50, 2.0)

# Versión que devuelve diccionario
def operaciones(x, y):
    def suma():
        return x + y
    
    def resta():
        return x - y
    
    return {
        'suma': suma(),
        'resta': resta(),
        'producto': x * y,
        'division': x / y if y != 0 else None
    }

resultado = operaciones(10, 5)
print(resultado['suma'])     # 15
print(resultado['resta'])    # 5
```

**Ventajas de funciones anidadas:**
- Encapsulación: la función interna no es accesible desde afuera
- Acceso a variables de la función externa (clausura/closure)
- Código más organizado

**Conceptos clave:**
- Las funciones anidadas pueden acceder a variables de la función externa
- Son útiles para código auxiliar que solo se usa internamente

---

### 2️⃣2️⃣ Función que valida datos - SOLUCIÓN

```python
def validar_edad(edad):
    """Valida si la edad es un número entre 0 y 150"""
    
    try:
        # Intentar convertir a entero
        edad = int(edad)
        # Verificar rango
        return 0 <= edad <= 150
    except (ValueError, TypeError):
        # Si no es un número
        return False

# Pruebas
print(validar_edad(25))       # True
print(validar_edad("25"))     # True (convierte string)
print(validar_edad("abc"))    # False
print(validar_edad(-5))       # False
print(validar_edad(200))      # False

def validar_email(email):
    """Valida si tiene formato básico de email"""
    
    # Verificar que tenga @ y .
    if '@' not in email or '.' not in email:
        return False
    
    # Verificar que @ esté antes de .
    if email.index('@') > email.rindex('.'):
        return False
    
    # Verificar que no esté vacío antes/después de @
    if email.count('@') != 1:
        return False
    
    return True

# Pruebas
print(validar_email('usuario@email.com'))     # True
print(validar_email('usuario@email'))         # False
print(validar_email('usuarioemail.com'))      # False
print(validar_email('usuario@@email.com'))    # False
```

**Versión con expresiones regulares (más robusta):**
```python
import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None
```

**Conceptos clave:**
- `try-except` para manejo de errores
- `.index()` y `.rindex()` para buscar posiciones
- `.count()` para contar ocurrencias

---

### 2️⃣3️⃣ Generar serie - SOLUCIÓN

```python
def generar_serie(inicio, fin, paso=1):
    """
    Genera una lista de números desde inicio hasta fin
    
    Parámetros:
        inicio: número inicial
        fin: número final (inclusive)
        paso: incremento entre números (por defecto 1)
    """
    serie = []
    
    if paso > 0:
        numero = inicio
        while numero <= fin:
            serie.append(numero)
            numero += paso
    elif paso < 0:
        numero = inicio
        while numero >= fin:
            serie.append(numero)
            numero += paso
    
    return serie

# Pruebas
print(generar_serie(1, 5))           # [1, 2, 3, 4, 5]
print(generar_serie(0, 10, 2))       # [0, 2, 4, 6, 8, 10]
print(generar_serie(10, 1, -1))      # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(generar_serie(0, 10, 3))       # [0, 3, 6, 9]
```

**Versión con range() (más Pythónica):**
```python
def generar_serie(inicio, fin, paso=1):
    return list(range(inicio, fin + 1, paso))

# Pero range es exclusivo del final, así que:
# range(0, 11, 2) da [0, 2, 4, 6, 8, 10]
```

**Versión con list comprehension:**
```python
def generar_serie(inicio, fin, paso=1):
    if paso > 0:
        return [n for n in range(inicio, fin + 1, paso)]
    else:
        return [n for n in range(inicio, fin - 1, paso)]
```

**Conceptos clave:**
- `range(inicio, fin, paso)` - fin NO es inclusive
- Necesitamos `fin + 1` para incluir el fin
- Con paso negativo, decrementamos

---

### 2️⃣4️⃣ Memoización (optimización) - SOLUCIÓN

```python
# Versión SIN memoización (muy lenta)
def fibonacci_lento(n):
    if n <= 1:
        return n
    return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)

# Prueba: fibonacci_lento(35) tarda varios segundos

# Versión CON memoización (instantánea)
def fibonacci_rapido(n, memo={}):
    """Fibonacci optimizado guardando resultados previos"""
    
    # Si ya calculamos este número, devolver el resultado
    if n in memo:
        return memo[n]
    
    # Caso base
    if n <= 1:
        return n
    
    # Calcular y guardar en memo
    memo[n] = fibonacci_rapido(n - 1, memo) + fibonacci_rapido(n - 2, memo)
    return memo[n]

# Pruebas
print(fibonacci_rapido(10))   # 55 (rápido)
print(fibonacci_rapido(100))  # 354224848179261915075 (rápido)

# Versión alternativa con decorador
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

print(fibonacci_cached(100))  # Muy rápido
```

**Conceptos clave:**
- Memoización: guardar resultados para no recalcular
- Diccionario para almacenar: `{entrada: salida}`
- `@lru_cache` es un decorador que hace memoización automáticamente
- Reduce complejidad de O(2^n) a O(n)

---

### 2️⃣5️⃣ Desafío: Juego interactivo - SOLUCIÓN

```python
import random

# Variables globales del juego
numero_secreto = None
intentos_actuales = 0

def nuevo_juego():
    """Inicia un nuevo juego con un número al azar"""
    global numero_secreto, intentos_actuales
    numero_secreto = random.randint(1, 100)
    intentos_actuales = 0
    print("¡Nuevo juego iniciado!")
    print("He pensado un número entre 1 y 100.")
    print("¿Puedes adivinarlo?")

def hacer_intento(numero):
    """Procesa un intento y devuelve pista"""
    global intentos_actuales
    
    if numero_secreto is None:
        return "Debe iniciar un nuevo juego primero"
    
    intentos_actuales += 1
    
    if numero == numero_secreto:
        return f"¡CORRECTO! Lo adivinaste en {intentos_actuales} intentos"
    elif numero < numero_secreto:
        return "Es MAYOR que tu número"
    else:
        return "Es MENOR que tu número"

def obtener_estadisticas():
    """Devuelve estadísticas del juego actual"""
    return {
        'intentos': intentos_actuales,
        'numero': numero_secreto
    }

# Usar el juego
def jugar():
    nuevo_juego()
    
    while True:
        try:
            numero = int(input("Adivina el número (1-100): "))
            
            if numero < 1 or numero > 100:
                print("Por favor, ingresa un número entre 1 y 100")
                continue
            
            resultado = hacer_intento(numero)
            print(resultado)
            
            if "CORRECTO" in resultado:
                stats = obtener_estadisticas()
                print(f"Intentos totales: {stats['intentos']}")
                
                respuesta = input("¿Deseas jugar de nuevo? (s/n): ")
                if respuesta.lower() == 's':
                    nuevo_juego()
                else:
                    print("¡Gracias por jugar!")
                    break
        
        except ValueError:
            print("Por favor, ingresa un número válido")

# Ejecutar
if __name__ == "__main__":
    jugar()
```

**Versión más limpia (sin variables globales):**
```python
class Juego:
    def __init__(self):
        self.numero_secreto = None
        self.intentos = 0
    
    def nuevo_juego(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
    
    def hacer_intento(self, numero):
        self.intentos += 1
        if numero == self.numero_secreto:
            return f"¡CORRECTO en {self.intentos} intentos!"
        elif numero < self.numero_secreto:
            return "Es MAYOR"
        else:
            return "Es MENOR"

juego = Juego()
juego.nuevo_juego()
print(juego.hacer_intento(50))
```

**Conceptos clave:**
- `global` para modificar variables globales
- `if __name__ == "__main__":` para ejecutar solo si se ejecuta directo
- Clases como alternativa más elegante

---

## NOTAS PARA EL PROFESOR

### Errores comunes:

1. **Olvidar return:**
   - ❌ `def suma(a, b): print(a + b)` - no devuelve nada
   - ✓ `def suma(a, b): return a + b`

2. **Parámetros sin defecto después de con defecto:**
   - ❌ `def f(a=1, b):` - Error
   - ✓ `def f(a, b=1):`

3. **Confundir parámetro con argumento:**
   - `def f(x):` - x es el parámetro
   - `f(5)` - 5 es el argumento

4. **Scope de variables:**
   - ❌ Crear local y pensar que modifica global
   - ✓ Usar `global` si necesitas modificar global

5. **Recursión sin caso base:**
   - ❌ Infinito y error: RecursionError
   - ✓ Siempre incluir condición de parada

### Preguntas de evaluación:

1. ¿Cuál es la diferencia entre parámetro y argumento?
2. ¿Qué es un valor por defecto y cómo se usa?
3. ¿Cuándo deberías usar una función vs código inline?
4. ¿Qué es una función recursiva? Ventajas y desventajas
5. ¿Qué es memoización y por qué es útil?

---

