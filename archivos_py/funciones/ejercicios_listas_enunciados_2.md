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
Suma los números de una lista 

**Ejemplo:**
```
si tu lista contiene los números del 1 al 5, al ejecutar el programa debe darte 15
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
Invierte el orden de los elementos de la lista

**Ejemplo:**
```
si tu lista contiene los números del 1 al 5, al ejecutar el programa debe darte 
[5, 4, 3, 2, 1]
```
**Pista:** Puedes usar un bucle `for` y una lista nueva, o usar *slicing* con `[::-1]`

---

### 8️⃣ Contar veces que aparece un elemento
**Enunciado:**
Cuenta cuántas veces aparece un elemento en la lista. **No puedes usar el método `.count()`**

**Ejemplo:**
```
si tu lista tiene estos números: 1, 2, 2, 3, 2, 4
Deber darte 3

Si tu lista tiene estos elementos: a,b,a,c,a,d
Deber darte 3
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
Ordena una lista de números de menor a mayor. **No puedes usar el método `.sort()` ni la función `sorted()`**

**Ejemplo:**
```
Si tu lista tiene estos elementos: 5, 2, 8, 1, 9
Debe salir [1, 2, 5, 8, 9]

```
---

### 1️⃣1️⃣ Listas de listas
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

---

### 1️⃣2️⃣ Transformar lista
**Enunciado:**
Escribe un programa que eleve al cuadrado los elementos de una lista


**Ejemplo:**
```
Si tu lista tiene 1, 2, 3, 4, 5
Devuelve [1, 4, 9, 16, 25]

```

**Intenta hacerlo on un bucle `for`**

---

### 1️⃣3️⃣ Palíndromos en lista
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

### 1️⃣4️⃣ Slicing avanzado
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

### 1️⃣5️⃣ Desafío: Analizar notas
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

