# 🎯 PROYECTO: PRUEBAS UNITARIAS - CÓDIGO PARA ESTUDIANTES
## Listo para subir a Git

---

## 📁 ESTRUCTURA DEL PROYECTO

```
proyecto-pruebas-unitarias/
├── src/
│   ├── __init__.py
│   ├── calculadora.py
│   ├── validador.py
│   ├── procesador_texto.py
│   ├── fibonacci.py
│   ├── descuentos.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_calculadora.py
│   ├── test_validador.py
│   ├── test_procesador_texto.py
│   ├── test_fibonacci.py
│   ├── test_descuentos.py
│   └── test_utils.py
├── README.md
├── requirements.txt
└── setup.sh
```

---

## 📋 INSTRUCCIONES PARA ESTUDIANTES

### Paso 1: Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto-pruebas-unitarias
```

### Paso 2: Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar pruebas
```bash
pytest
```

### Paso 5: Ver reporte de cobertura
```bash
pytest --cov=src --cov-report=html
```

### Paso 6: Enviar sus pruebas
```bash
git add tests/
git commit -m "Mis pruebas unitarias"
git push
```

---

## 🎮 DESAFÍOS PARA ESTUDIANTES

### Desafío 1: El Detective de Bugs
Hay **5 bugs ocultos** en los archivos de `src/`. Escriban pruebas para encontrarlos.

### Desafío 2: El Arquitecto de Pruebas
Cada prueba debe seguir la estructura AAA (Arrange, Act, Assert).

### Desafío 3: Casos Límite
Encuentren TODOS los casos límite posibles para cada función.

### Desafío 4: Cobertura Completa
Logren una cobertura del 100% en todos los archivos.

---

## 🏆 PUNTUACIÓN

- 1 punto por cada prueba válida
- 2 puntos por cada caso límite encontrado
- 3 puntos por cada bug encontrado
- 5 puntos por archivo con 100% de cobertura
- 10 puntos por nombre de prueba descriptivo

---

## 📝 EJEMPLO DE PRUEBA

```python
# test_calculadora.py
import pytest
from src.calculadora import sumar

def test_sumar_positivos():
    """Prueba suma de números positivos."""
    # Arrange
    a = 5
    b = 3
    resultado_esperado = 8

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == resultado_esperado
```

---

## 💡 CONSEJOS

1. Una prueba, un propósito
2. Nombres descriptivos
3. Casos normales, límites y errores
4. Organización clara
5. Comentarios cuando sea necesario

---

## 🚀 LISTO PARA EMPEZAR

¡Comiencen a escribir pruebas y encuentren los bugs ocultos!

---

**Buena suerte!** 🎯