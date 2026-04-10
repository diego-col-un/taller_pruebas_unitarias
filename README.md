
## ✅ RESULTADOS OBTENIDOS

| Métrica | Resultado |
|---|---|
| Tests en estado PASSED | ✅ 40 / 40 |
| Bugs encontrados y corregidos | ✅ 14 / 14 |
| Cobertura de código | ✅ 100% |

### Cobertura por módulo

| Módulo | Cobertura inicial | Cobertura final |
|---|---|---|
| `calculadora.py` | 98% | ✅ 100% |
| `conversor.py` | 62% | ✅ 100% |
| `csv_parser.py` | 76% | ✅ 100% |
| `descuentos.py` | 78% | ✅ 100% |
| `fibonacci.py` | 84% | ✅ 100% |
| `manipulador_texto.py` | 73% | ✅ 100% |
| `procesador_texto.py` | 56% | ✅ 100% |
| `utils.py` | 60% | ✅ 100% |
| `validador.py` | 78% | ✅ 100% |
| `autenticacion.py` | 100% | ✅ 100% |
| **TOTAL** | **83%** | **✅ 100%** |

## 🚀 INSTRUCCIONES DE USO

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/pruebas_unitarias_devops.git
cd pruebas_unitarias_devops
```

### Paso 2: Crear entorno virtual
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar los tests
```bash
pytest
```

### Paso 5: Ver reporte de cobertura
```bash
pytest --cov=src --cov-report=term-missing
```

### Paso 6: Ver reporte de cobertura html 
```bash
pytest --cov=src --cov-report=html
```

---

## 🧠 EJEMPLO DE TEST (patrón AAA)

```python
def test_minimo_lista_positivos():
    """Verifica que minimo() retorna el valor correcto, no 0."""
    # Arrange
    lista = [5, 10, 15]

    # Act
    resultado = minimo(lista)

    # Assert
    assert resultado == 5  # Bug: antes retornaba 0
```

---

## 📦 REPOSITORIO BASE

Este proyecto es la solución al taller propuesto por el profesor.
El repositorio original del enunciado se encuentra en:
[github.com/cesarpalacios/pruebas_unitarias_devops](https://github.com/cesarpalacios/pruebas_unitarias_devops)