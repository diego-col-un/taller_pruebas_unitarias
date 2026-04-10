import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir, potencia, 
    raiz_cuadrada, promedio, maximo, minimo,
    calcular_area_rectangulo, calcular_perimetro_rectangulo
)

def test_calculadora_todo():
    # Operaciones básicas
    assert sumar(2, 2) == 4
    assert restar(5, 2) == 3
    assert multiplicar(3, 3) == 9
    assert potencia(2, 3) == 8
    
    # División y su error (Líneas 20-22)
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

    # Raíz y su error (Líneas 43-49)
    assert raiz_cuadrada(25) == 5
    with pytest.raises(ValueError):
        raiz_cuadrada(-1)

    # Listas y sus errores (Promedio, Max, Min)
    lista = [1, 2, 3]
    assert promedio(lista) == 2
    assert maximo(lista) == 3
    assert minimo(lista) == 1
    with pytest.raises(ValueError):
        promedio([])
    with pytest.raises(ValueError):
        maximo([])
    with pytest.raises(ValueError):
        minimo([])

    # Geometría y sus errores
    assert calcular_area_rectangulo(5, 4) == 20
    assert calcular_perimetro_rectangulo(5, 4) == 18
    with pytest.raises(ValueError):
        calcular_area_rectangulo(-1, 5)
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(5, -1)

def test_perimetro_valores_negativos():
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(-1, 5)
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(5, -1)        