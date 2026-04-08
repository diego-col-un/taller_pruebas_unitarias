# 🕵️ SOLUCIÓN DE BUGS OCULTOS
## SOLO PARA EL PROFESOR - NO COMPARTIR CON ESTUDIANTES

---

## 📋 LISTADO DE BUGS (5 en total)

### Módulo: calculadora.py

**BUG 1: Función `raiz_cuadrada(numero)`**
```python
def raiz_cuadrada(numero):
    return numero ** 0.5
```
**Problema:** No maneja números negativos (debe lanzar ValueError).

**Prueba para encontrarlo:**
```python
def test_raiz_cuadrada_negativo():
    with pytest.raises(ValueError):
        raiz_cuadrada(-4)
```

---

**BUG 2: Función `minimo(lista)`**
```python
def minimo(lista):
    min_val = 0  # BUG: Siempre comienza en 0
    for num in lista:
        if num < min_val:
            min_val = num
    return min_val
```
**Problema:** Comienza en 0, si todos los números son positivos, el mínimo incorrecto es 0.

**Prueba para encontrarlo:**
```python
def test_minimo_solo_positivos():
    assert minimo([1, 2, 3, 4, 5]) == 1  # Debe ser 1, pero devuelve 0
```

---

### Módulo: validador.py

**BUG 3: Función `validar_fecha(dia, mes, año)`**
```python
def validar_fecha(dia, mes, año):
    # BUG: No valida correctamente el mes y día
    if mes < 1 or mes > 12:
        return False

    if dia < 1 or dia > 31:  # BUG: Acepta 31 de febrero, 30 de noviembre, etc.
        return False
```
**Problema:** Acepta días que no existen en ciertos meses (ej: 31 de febrero).

**Prueba para encontrarlo:**
```python
def test_validar_fecha_febrero_31():
    assert not validar_fecha(31, 2, 2024)  # 31 de febrero no existe
```

---

### Módulo: procesador_texto.py

**BUG 4: Función `es_palindromo(texto)`**
```python
def es_palindromo(texto):
    # BUG: No maneja espacios ni mayúsculas
    return texto == texto[::-1]
```
**Problema:** No maneja espacios ni mayúsculas ("Ana" no es palíndromo).

**Prueba para encontrarlo:**
```python
def test_es_palindromo_con_espacios():
    assert es_palindromo("Ana")  # Debe ser True, pero devuelve False
    assert es_palindromo("A man a plan a canal Panama")  # Debe ser True
```

---

### Módulo: descuentos.py

**BUG 5: Función `calcular_precio_final(precio, impuesto, descuento)`**
```python
def calcular_precio_final(precio, impuesto, descuento):
    # Primero aplicar el descuento
    precio_con_descuento = aplicar_descuento(precio, descuento)

    # Luego aplicar el impuesto
    # BUG: El impuesto se aplica incorrectamente (al precio original, no al descontado)
    impuesto_monto = precio * (impuesto / 100)  # Debe ser: precio_con_descuento * (impuesto / 100)
    precio_final = precio_con_descuento + impuesto_monto

    return precio_final
```
**Problema:** El impuesto se calcula sobre el precio original, no sobre el precio con descuento.

**Prueba para encontrarlo:**
```python
def test_calcular_precio_final_impuesto_sobre_original():
    # Precio: 100, Descuento: 10%, Impuesto: 10%
    # Precio con descuento: 90
    # Impuesto correcto (sobre 90): 9
    # Impuesto incorrecto (sobre 100): 10
    # Precio final correcto: 90 + 9 = 99
    # Precio final incorrecto: 90 + 10 = 100
    resultado = calcular_precio_final(100, 10, 10)
    assert resultado == 99  # Debe ser 99, pero devuelve 100
```

---

**BUG 6: Función `descuento_apilado(precio, descuentos)`**
```python
def descuento_apilado(precio, descuentos):
    total_descuento = sum(descuentos)  # BUG: Puede exceder 100%
    return aplicar_descuento(precio, total_descuento)
```
**Problema:** Si los descuentos suman más de 100, la función `aplicar_descuento` lanza ValueError, pero esta función no valida eso.

**Prueba para encontrarlo:**
```python
def test_descuento_apilado_excede_100():
    # 50% + 60% = 110% (excede 100%)
    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        descuento_apilado(100, [50, 60])
```

---

### Módulo: utils.py

**BUG 7: Función `mcm(a, b)`**
```python
def mcm(a, b):
    # BUG: Error en el cálculo
    return a * b // mcd(a, b)
```
**Problema:** El cálculo es correcto en teoría, pero hay un bug sutil con números negativos.

**Prueba para encontrarlo:**
```python
def test_mcm_negativos():
    # MCM de -4 y 6 es 12
    # Pero la fórmula puede fallar con signos
    assert mcm(-4, 6) == 12  # Puede fallar
```

---

## 🎯 ESTRATEGIAS DE ENSEÑANZA

### 1. NO REVELAR LOS BUGS INMEDIATAMENTE
- Deja que los estudiantes los encuentren escribiendo pruebas
- Guíalos indirectamente: "¿Qué pasa si el precio es negativo?"

### 2. AYUDA CON PREGUNTAS
- En lugar de decir "hay un bug en la línea X", pregunta:
  - "¿Qué pasa si la lista está vacía?"
  - "¿Qué pasa si el número es negativo?"
  - "¿Qué pasa si hay múltiples espacios?"

### 3. PREMIA EL DESCUBRIMIENTO
- Celebra cuando encuentran un bug
- Escribe en el tablero: "¡BUG ENCONTRADO! [Nombre del estudiante]"

### 4. PROGRESIÓN DE DIFICULTAD
- Empieza con bugs obvios (dividir por cero)
- Luego bugs más sutiles (mínimo incorrecto)
- Finalmente bugs lógicos (impuesto calculado incorrectamente)

---

## 📊 PUNTUACIÓN SUGERIDA

| Actividad | Puntos |
|-----------|--------|
| Prueba válida escrita | 1 punto |
| Caso límite encontrado | 2 puntos |
| Bug encontrado | 3 puntos |
| Archivo con 100% cobertura | 5 puntos |
| Prueba con nombre descriptivo | 1 punto |
| Prueba con estructura AAA correcta | 2 puntos |
| Total máximo por estudiante | 50+ puntos |

---

**RECUERDA: La clave es que los estudiantes aprendan a pensar en casos de prueba, no solo a encontrar bugs.**