import pytest
from src.fibonacci import (
    fibonacci_iterativo, fibonacci_recursivo, fibonacci_serie,
    es_fibonacci, es_cuadrado_perfecto
)
def test_fibonacci_valores_correctos():
    # El 6to número (índice 6) es 8 (0, 1, 1, 2, 3, 5, 8)
    assert fibonacci_iterativo(6) == 8
    assert fibonacci_recursivo(6) == 8

def test_fibonacci_recursivo_rendimiento():
    """Prueba que el bug de rendimiento (memoización) esté arreglado."""
    # Si no tuviera memoización, fibonacci(35) tardaría segundos. 
    # Con memoización, es instantáneo.
    assert fibonacci_recursivo(35) == 9227465

def test_fibonacci_serie():
    assert fibonacci_serie(4) == [0, 1, 1, 2, 3]
    with pytest.raises(ValueError):
        fibonacci_serie(-1)

def test_es_fibonacci():
    assert es_fibonacci(13) is True
    assert es_fibonacci(7) is False
    assert es_fibonacci(0) is True

def test_es_fibonacci_negativo_cobertura():
    # Para llegar al 100% de cobertura en es_fibonacci
    assert es_fibonacci(-5) is False

def test_fibonacci_iterativo_casos_base():
    assert fibonacci_iterativo(0) == 0
    assert fibonacci_iterativo(1) == 1
    with pytest.raises(ValueError):
        fibonacci_iterativo(-1)

def test_fibonacci_recursivo_casos_base():
    assert fibonacci_recursivo(0) == 0
    assert fibonacci_recursivo(1) == 1
    with pytest.raises(ValueError):
        fibonacci_recursivo(-1)

def test_fibonacci_serie_casos_base():
    assert fibonacci_serie(0) == [0]
    assert fibonacci_serie(1) == [0, 1]

def test_es_fibonacci_uno():
    assert es_fibonacci(1) is True

def test_es_cuadrado_perfecto():
    assert es_cuadrado_perfecto(25) is True
    assert es_cuadrado_perfecto(7) is False
    assert es_cuadrado_perfecto(-4) is False