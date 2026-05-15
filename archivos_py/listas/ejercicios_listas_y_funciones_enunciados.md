# Ejercicios sobre Listas en Python
## Nivel Básico e Intermedio

---

## NIVEL BÁSICO

### 1️⃣ Crear y acceder a elementos
**Enunciado:**
Crea una lista con los nombres de 5 frutas. Luego:
- Imprime la primera fruta
- Imprime la última fruta  
- Imprime la fruta que está en el medio

**Ejemplo:**
```
frutas = ['manzana', 'plátano', 'naranja', 'fresa', 'sandía']
```

**Salida esperada:**
```
Primera fruta: manzana
Última fruta: sandía
Fruta del medio: naranja
```

---

### 2️⃣ Contar elementos y longitud
**Enunciado:**
Escribe un programa que:
- Pida al usuario que introduzca números uno por uno
- Se detenga cuando escriba "fin"
- Muestre cuántos números ha introducido

**Ejemplo de ejecución:**
```
Introduce un número (o "fin" para terminar): 5
Introduce un número (o "fin" para terminar): 12
Introduce un número (o "fin" para terminar): 8
Introduce un número (o "fin" para terminar): fin

Has introducido 3 números.
```

---

### 3️⃣ Agregar elementos con append()
**Enunciado:**
Crea una lista vacía. Luego:
- Añade tres colores usando `append()`
- Imprime la lista después de cada adición

**Ejemplo:**
```
Lista inicial: []
Tras añadir rojo: ['rojo']
Tras añadir azul: ['rojo', 'azul']
Tras añadir verde: ['rojo', 'azul', 'verde']
```

---

### 4️⃣ Eliminar elementos
**Enunciado:**
Dada la lista `[10, 20, 30, 40, 50]`:
- Elimina el número 30
- Imprime la lista resultante

**Pista:** Usa el método `remove()`

---

### 5️⃣ Suma de elementos
**Enunciado:**
Escribe una función `sumar_lista(lista)` que reciba una lista de números y devuelva la suma de todos ellos. **No puedes usar la función `sum()` de Python.**

**Ejemplo:**
```
>>> sumar_lista([1, 2, 3, 4, 5])
15

>>> sumar_lista([10, 20, 30])
60
```

---

### 6️⃣ Buscar un elemento
**Enunciado:**
Escribe una función `esta_en_lista(elemento, lista)` que devuelva `True` si el elemento está en la lista, y `False` en caso contrario. **No puedes usar el operador `in`.**

**Ejemplo:**
```
>>> esta_en_lista('gato', ['perro', 'gato', 'pájaro'])
True

>>> esta_en_lista('pez', ['perro', 'gato', 'pájaro'])
False
```

---

### 7️⃣ Invertir una lista
**Enunciado:**
Crea una función `invertir_lista(lista)` que devuelva los elementos de la lista en orden inverso.

**Ejemplo:**
```
>>> invertir_lista([1, 2, 3, 4, 5])
[5, 4, 3, 2, 1]

>>> invertir_lista(['a', 'b', 'c'])
['c', 'b', 'a']
```

**Pista:** Puedes usar un bucle `for` y una lista nueva, o usar *slicing* con `[::-1]`

---

### 8️⃣ Contar veces que aparece un elemento
**Enunciado:**
Escribe una función `contar_elemento(lista, elemento)` que cuente cuántas veces aparece un elemento en la lista. **No puedes usar el método `.count()`**

**Ejemplo:**
```
>>> contar_elemento([1, 2, 2, 3, 2, 4], 2)
3

>>> contar_elemento(['a', 'b', 'a', 'a', 'c'], 'a')
3
```

---

## NIVEL INTERMEDIO

### 9️⃣ Números pares e impares
**Enunciado:**
Dada una lista de números `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, crea dos listas nuevas:
- Una con los números pares
- Otra con los números impares

**Salida esperada:**
```
Pares: [2, 4, 6, 8, 10]
Impares: [1, 3, 5, 7, 9]
```

**Pista:** Usa un bucle y `append()`, o mejor aún, intenta con **list comprehension** (comprensión de listas)

---

### 🔟 Ordenar una lista
**Enunciado:**
Escribe una función `ordenar_numeros(lista)` que ordene una lista de números de menor a mayor. **No puedes usar el método `.sort()` ni la función `sorted()`**

**Ejemplo:**
```
>>> ordenar_numeros([5, 2, 8, 1, 9])
[1, 2, 5, 8, 9]

>>> ordenar_numeros([15, 3, 42, 7])
[3, 7, 15, 42]
```

**Pista:** Piensa en el algoritmo de ordenamiento más simple que conozcas (burbuja, por ejemplo)

---

### 1️⃣1️⃣ Máximo y mínimo
**Enunciado:**
Escribe dos funciones:
- `encontrar_maximo(lista)` - devuelve el número más grande
- `encontrar_minimo(lista)` - devuelve el número más pequeño

**No puedes usar `max()` ni `min()`**

**Ejemplo:**
```
>>> encontrar_maximo([3, 1, 4, 1, 5, 9, 2, 6])
9

>>> encontrar_minimo([3, 1, 4, 1, 5, 9, 2, 6])
1
```

---

### 1️⃣2️⃣ Listas de listas
**Enunciado:**
Dada una lista de calificaciones por alumno:
```python
calificaciones = [
    ['Ana', 7, 8, 9],
    ['Beto', 6, 7, 8],
    ['Clara', 9, 9, 10],
    ['Diego', 5, 6, 7]
]
```

Crea un programa que:
- Imprima el nombre y la nota media de cada alumno
- Indique quién tiene la nota media más alta

**Salida esperada:**
```
Ana: promedio 8.0
Beto: promedio 7.0
Clara: promedio 9.33
Diego: promedio 6.0

El alumno con mayor promedio es: Clara (9.33)
```

---

### 1️⃣3️⃣ Eliminar duplicados
**Enunciado:**
Escribe una función `eliminar_duplicados(lista)` que devuelva una nueva lista sin elementos repetidos, manteniendo el orden original.

**Ejemplo:**
```
>>> eliminar_duplicados([1, 2, 2, 3, 3, 3, 4])
[1, 2, 3, 4]

>>> eliminar_duplicados(['a', 'b', 'a', 'c', 'b'])
['a', 'b', 'c']
```

**Pista:** Recorre la lista y solo añade elementos que no hayas visto antes

---

### 1️⃣4️⃣ Intersección de listas
**Enunciado:**
Escribe una función `elementos_comunes(lista1, lista2)` que devuelva una lista con los elementos que aparecen en ambas listas (sin repetidos).

**Ejemplo:**
```
>>> elementos_comunes([1, 2, 3, 4], [3, 4, 5, 6])
[3, 4]

>>> elementos_comunes(['a', 'b', 'c'], ['c', 'd', 'e'])
['c']
```

---

### 1️⃣5️⃣ Transformar lista
**Enunciado:**
Escribe una función `elevar_al_cuadrado(lista)` que devuelva una nueva lista donde cada elemento sea el cuadrado del original.

**Ejemplo:**
```
>>> elevar_al_cuadrado([1, 2, 3, 4, 5])
[1, 4, 9, 16, 25]

>>> elevar_al_cuadrado([2, 5, 10])
[4, 25, 100]
```

**Intenta hacerlo de dos formas:**
- Con un bucle `for`
- Con **list comprehension**

---

### 1️⃣6️⃣ Filtrar lista
**Enunciado:**
Escribe una función `mayores_que(lista, numero)` que devuelva una nueva lista con solo los números mayores que el valor indicado.

**Ejemplo:**
```
>>> mayores_que([1, 2, 3, 4, 5, 6], 3)
[4, 5, 6]

>>> mayores_que([10, 20, 30, 40], 25)
[30, 40]
```

---

### 1️⃣7️⃣ Combinar listas
**Enunciado:**
Escribe una función `intercalar(lista1, lista2)` que combine dos listas alternando sus elementos.

**Ejemplo:**
```
>>> intercalar([1, 2, 3], ['a', 'b', 'c'])
[1, 'a', 2, 'b', 3, 'c']

>>> intercalar([10, 20], [100, 200])
[10, 100, 20, 200]
```

**Nota:** Asume que ambas listas tienen la misma longitud

---

### 1️⃣8️⃣ Palíndromos en lista
**Enunciado:**
Dada una lista de palabras, crea un programa que:
- Filtre solo las palabras que son palíndromos
- Las imprima con un mensaje especial

**Ejemplo:**
```
palabras = ['radar', 'hola', 'nivel', 'python', 'oso']

Salida:
radar es palíndromo ✓
nivel es palíndromo ✓
oso es palíndromo ✓
```

---

### 1️⃣9️⃣ Slicing avanzado
**Enunciado:**
Dada la lista `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, obtén:
- Los 3 primeros elementos
- Los 3 últimos elementos
- Todos los elementos de índice par
- Todos los elementos desde el índice 2 hasta el 7 (inclusive)
- La lista invertida

**Ejemplo:**
```
original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Primeros 3: [0, 1, 2]
Últimos 3: [7, 8, 9]
Índices pares: [0, 2, 4, 6, 8]
Del 2 al 7: [2, 3, 4, 5, 6, 7]
Invertida: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

### 2️⃣0️⃣ Desafío: Analizar notas
**Enunciado:**
Tienes una lista de notas de un alumno en diferentes asignaturas:
```python
notas = [7, 8, 6, 9, 7, 8, 10, 7]
```

Escribe un programa que:
- Calcule el promedio
- Encuentre la nota más alta y más baja
- Cuente cuántas notas son >= 8 (aprobadas con distinción)
- Cuente cuántas notas son < 7 (suspenso)
- Determine si el alumno aprobó (promedio >= 6)

**Salida esperada:**
```
Notas: [7, 8, 6, 9, 7, 8, 10, 7]
Promedio: 7.75
Nota máxima: 10
Nota mínima: 6
Notas >= 8: 3
Notas < 7: 1
¿Aprobado? Sí
```

---

