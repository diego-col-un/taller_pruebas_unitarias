import pytest
from src.descuentos import (
    aplicar_descuento, calcular_descuento, 
    calcular_precio_final, descuento_por_volumen, 
    descuento_cumulativo, descuento_apilado
)

def test_precio_final_impuesto_correcto():
    """Confirma arreglo del BUG 1."""
    # Precio 100, Descuento 50% = 50. Impuesto 10% de 50 = 5. Total = 55.
    assert calcular_precio_final(100, 10, 50) == 55

def test_descuento_apilado_limite():
    """Confirma arreglo del BUG 2."""
    # Descuentos sumados dan 120%, debe topar en 100% (precio final 0).
    assert descuento_apilado(100, [60, 60]) == 0

def test_descuento_por_volumen_escalas():
    """Prueba todas las ramas (if/elif) para cobertura 100%."""
    assert descuento_por_volumen(100, 10) == 800  # 20% desc
    assert descuento_por_volumen(50, 10) == 425   # 15% desc
    assert descuento_por_volumen(20, 10) == 180   # 10% desc
    assert descuento_por_volumen(10, 10) == 95    # 5% desc
    assert descuento_por_volumen(5, 10) == 50     # 0% desc

def test_descuento_cumulativo():
    # 100 - 10% = 90. 90 - 10% = 81.
    assert descuento_cumulativo(100, [10, 10]) == 81
    assert descuento_cumulativo(100, []) == 100

def test_excepciones_descuentos():
    with pytest.raises(ValueError):
        aplicar_descuento(-1, 10)
    with pytest.raises(ValueError):
        descuento_cumulativo(100, [110])

def test_calcular_precio_final_errores():
    with pytest.raises(ValueError):
        calcular_precio_final(-1, 10, 0)   # precio negativo
    with pytest.raises(ValueError):
        calcular_precio_final(100, -5, 0)  # impuesto negativo
    with pytest.raises(ValueError):
        calcular_precio_final(100, 10, -1) # descuento negativo

def test_descuento_por_volumen_negativos():
    with pytest.raises(ValueError):
        descuento_por_volumen(-1, 10)
    with pytest.raises(ValueError):
        descuento_por_volumen(10, -1)

def test_descuento_apilado_sin_descuentos():
    assert descuento_apilado(100, []) == 100

def test_descuento_apilado_precio_negativo():
    with pytest.raises(ValueError):
        descuento_apilado(-100, [10])

def test_calcular_descuento_errores():
    with pytest.raises(ValueError):
        calcular_descuento(-1, 10)
    with pytest.raises(ValueError):
        calcular_descuento(100, 110)        