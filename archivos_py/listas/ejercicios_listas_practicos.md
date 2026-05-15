# Ejercicios Prácticos - Listas en Python
## Actividades para clase y evaluación

---

## 🎯 EJERCICIOS QUICK (5-10 minutos cada uno)

Ideales para inicio de clase, repaso o evaluación rápida.

### QA1: Acceso rápido
```python
# Completa el código para que imprima lo indicado
musica = ['rock', 'pop', 'jazz', 'blues', 'metal']

print(musica[0])        # ¿Qué imprime?
print(musica[-1])       # ¿Qué imprime?
print(musica[2])        # ¿Qué imprime?
print(musica[1:4])      # ¿Qué imprime?
```

**Respuesta esperada:**
```
rock
metal
jazz
['pop', 'jazz', 'blues']
```

---

### QA2: Modificar listas
```python
compra = ['leche', 'pan']

# Añade 'queso'
# Añade 'huevos'
# Elimina 'pan'

print(compra)  # Debe mostrar ['leche', 'queso', 'huevos']
```

**Solución:**
```python
compra.append('queso')
compra.append('huevos')
compra.remove('pan')
```

---

### QA3: Bucle simple
```python
# Escribe un bucle que imprima cada número multiplicado por 2
numeros = [1, 2, 3, 4, 5]

# Tu código aquí

# Salida esperada:
# 2
# 4
# 6
# 8
# 10
```

**Solución:**
```python
for numero in numeros:
    print(numero * 2)
```

---

### QA4: Contar elementos
```python
# ¿Cuántos elementos hay en la lista?
# ¿Cuál es el elemento más grande?
# ¿Cuál es el elemento más pequeño?

datos = [15, 3, 42, 7, 19, 2, 33]

print(len(datos))      # Respuesta: ?
print(max(datos))      # Respuesta: ?
print(min(datos))      # Respuesta: ?
```

**Respuesta:**
```
7
42
2
```

---

### QA5: Invertir
```python
# Invierte la lista de dos formas diferentes
palabra = ['h', 'o', 'l', 'a']

# Forma 1: Con slicing
print(palabra[::-1])

# Forma 2: Con el método reverse()
palabra.reverse()
print(palabra)
```

---

## 📝 EJERCICIOS DE PROGRAMACIÓN (15-30 minutos)

### PA1: Contador de caracteres
**Enunciado:**
Escribe un programa que cuente cuántas veces aparece cada letra en la palabra "programacion".

**Pista:** Transforma la palabra en lista usando `list(palabra)`

**Solución esperada:**
```python
palabra = "programacion"
letras = list(palabra)

# Opción 1: Con un diccionario (si lo conocen)
for letra in set(letras):
    print(f"{letra}: {letras.count(letra)}")

# Opción 2: Con listas simples
letras_unicas = []
for letra in letras:
    if letra not in letras_unicas:
        letras_unicas.append(letra)

for letra in letras_unicas:
    print(f"{letra}: {letras.count(letra)}")
```

---

### PA2: Calificaciones de un grupo
**Enunciado:**
Los alumnos de una clase obtuvieron estas notas: `[8, 6, 9, 7, 5, 8, 6, 9, 10, 7]`

Escribe un programa que:
- Cuente cuántos aprobaron (nota >= 6)
- Cuente cuántos suspendieron (nota < 6)
- Calcule la nota media del grupo

**Salida esperada:**
```
Aprobados: 8
Suspendidos: 2
Nota media: 7.5
```

**Solución esperada:**
```python
notas = [8, 6, 9, 7, 5, 8, 6, 9, 10, 7]

# Aprobados
aprobados = sum(1 for nota in notas if nota >= 6)

# Suspendidos  
suspendidos = sum(1 for nota in notas if nota < 6)

# Media
media = sum(notas) / len(notas)

print(f"Aprobados: {aprobados}")
print(f"Suspendidos: {suspendidos}")
print(f"Nota media: {media}")
```

---

### PA3: Ordenar una lista manualmente
**Enunciado:**
Sin usar `sort()` ni `sorted()`, ordena esta lista de menor a mayor usando solo bucles:
`[64, 34, 25, 12, 22, 11, 90]`

**Pista:** Compara cada número con los demás y coloca el más pequeño al principio.

**Solución (Algoritmo de selección):**
```python
numeros = [64, 34, 25, 12, 22, 11, 90]

# Algoritmo de selección
for i in range(len(numeros)):
    # Encuentra el índice del mínimo
    minimo_idx = i
    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[minimo_idx]:
            minimo_idx = j
    
    # Intercambia
    numeros[i], numeros[minimo_idx] = numeros[minimo_idx], numeros[i]

print(numeros)  # [11, 12, 22, 25, 34, 64, 90]
```

---

### PA4: Más alto y más bajo
**Enunciado:**
En un videoclub hay películas con estas duraciones (en minutos):
`[120, 95, 148, 102, 156, 110, 99, 140, 135, 118]`

Escribe un programa que:
- Encuentre la película más larga
- Encuentre la película más corta
- Calcule el tiempo medio

**Salida esperada:**
```
Película más larga: 156 minutos
Película más corta: 95 minutos
Duración media: 124.3 minutos
```

---

### PA5: Palabras de un texto
**Enunciado:**
Escribe un programa que:
1. Pida al usuario que escriba una frase
2. Divida la frase en palabras
3. Muestre:
   - Cuántas palabras hay
   - La palabra más larga
   - La palabra más corta

**Ejemplo:**
```
Escribe una frase: La programación es muy divertida
Número de palabras: 6
Palabra más larga: programación
Palabra más corta: es
```

**Solución esperada:**
```python
frase = input("Escribe una frase: ")
palabras = frase.split()  # Divide por espacios

print(f"Número de palabras: {len(palabras)}")

# Palabra más larga
mas_larga = palabras[0]
for palabra in palabras:
    if len(palabra) > len(mas_larga):
        mas_larga = palabra
print(f"Palabra más larga: {mas_larga}")

# Palabra más corta
mas_corta = palabras[0]
for palabra in palabras:
    if len(palabra) < len(mas_corta):
        mas_corta = palabra
print(f"Palabra más corta: {mas_corta}")
```

---

## 🏆 EJERCICIOS DE DESAFÍO (30-45 minutos)

Para alumnos avanzados o como tarea de ampliación.

### DA1: Simulador de tienda
**Enunciado:**
Simula una tienda con estos artículos y precios:

```python
articulos = ['manzana', 'pan', 'leche', 'queso', 'huevo']
precios = [0.50, 1.20, 1.50, 2.00, 0.30]
```

Escribe un programa que:
1. Muestre los artículos con su número
2. Permita al usuario comprar artículos
3. Calcule el total de la compra
4. Permita comprar más o terminar

**Estructura sugerida:**
```python
articulos = ['manzana', 'pan', 'leche', 'queso', 'huevo']
precios = [0.50, 1.20, 1.50, 2.00, 0.30]

carrito = []
total = 0

while True:
    # Mostrar menú
    for i in range(len(articulos)):
        print(f"{i}: {articulos[i]} - ${precios[i]}")
    
    # Pedir selección
    seleccion = int(input("¿Qué deseas comprar? (o -1 para terminar): "))
    
    if seleccion == -1:
        break
    
    # Agregar al carrito
    carrito.append(articulos[seleccion])
    total += precios[seleccion]

print(f"Total: ${total:.2f}")
```

---

### DA2: Análisis de temperaturas
**Enunciado:**
Tienes las temperaturas diarias de una semana:
`[22, 25, 23, 28, 26, 24, 27]`

Escribe un programa que:
1. Encuentre el día más caluroso
2. Encuentre el día más frío
3. Calcule la temperatura media
4. Muestre cuántos días tuvieron temperatura >= 25°C
5. Cree dos listas: una con días "fríos" (< 24°C) y otra con "cálidos" (>= 25°C)

---

### DA3: Palabras duplicadas
**Enunciado:**
Escribe un programa que:
1. Pida al usuario una frase
2. Encuentre todas las palabras que se repiten
3. Muestre cuántas veces aparece cada palabra duplicada

**Ejemplo:**
```
Frase: hola mundo hola python mundo hola
Palabras duplicadas:
- hola: 3 veces
- mundo: 2 veces
```

---

### DA4: Ordenar estudiantes
**Enunciado:**
Tienes datos de estudiantes:
```python
estudiantes = [
    ['Juan', 8, 7, 9],
    ['María', 9, 9, 8],
    ['Pedro', 6, 7, 6],
    ['Ana', 9, 10, 9]
]
```

Escribe un programa que:
1. Calcule el promedio de cada estudiante
2. Ordene los estudiantes por promedio (mayor a menor)
3. Muestre el ranking con posición, nombre y promedio

**Salida esperada:**
```
1. Ana - 9.33
2. María - 8.67
3. Juan - 8.0
4. Pedro - 6.33
```

---

### DA5: Juego de adivinanza
**Enunciado:**
Crea un juego donde:
1. La computadora elige un número al azar (1-100)
2. El usuario intenta adivinarlo
3. Cada intento se guarda en una lista
4. Al final se muestra:
   - Cuántos intentos hizo
   - La lista de intentos
   - Si fue mejor o peor que la última vez (compara con el juego anterior)

**Pista:** Guarda los resultados en un archivo o variable global

---

## 📊 RÚBRICA DE EVALUACIÓN

### Criterios básicos (0-10 puntos):
- ✓ El código funciona sin errores (4 puntos)
- ✓ Usa listas correctamente (3 puntos)
- ✓ El código está limpio y legible (2 puntos)
- ✓ Hay comentarios explicativos (1 punto)

### Criterios intermedios (extra):
- ✓ Usa list comprehension (+1 punto)
- ✓ Maneja excepciones (+1 punto)
- ✓ Código eficiente (+1 punto)

---

## 💡 ACTIVIDADES PARA CLASE

### Actividad 1: Debate - ¿Qué es más Pythónico?

Presenta dos formas de hacer lo mismo y pregunta cuál prefieren y por qué:

**Opción A:**
```python
numeros = [1, 2, 3, 4, 5]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
```

**Opción B:**
```python
numeros = [1, 2, 3, 4, 5]
pares = [n for n in numeros if n % 2 == 0]
```

**Discusión:** ¿Cuál es más legible? ¿Cuál es más rápido? ¿Cuál prefieres y por qué?

---

### Actividad 2: Ejercicio en parejas
Los alumnos trabajan en parejas:
- Uno explica qué hace una línea de código
- El otro la ejecuta mentalmente
- Intercambian roles

---

### Actividad 3: Detección de errores
Muestra código con errores y pide que los identifiquen:

```python
# Error 1
lista = [1, 2, 3]
print(lista[3])  # ¿Qué pasará?

# Error 2
lista = [1, 2, 3]
lista.remove(4)  # ¿Qué pasará?

# Error 3
lista = [1, 2, 3]
lista[0] = [4, 5]  # ¿Resultado?
```

---

