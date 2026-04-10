import pytest
from src.csv_parser import (
    parse_csv_line, csv_a_diccionarios, validar_csv, 
    extraer_columna, contar_filas, contar_columnas
)

def test_parse_csv_comillas_complejas():
    """Confirma arreglo del BUG 1 (Comas dentro de comillas)."""
    linea = 'Diego,Caldas,"Ciudad, Manizales",2026'
    resultado = parse_csv_line(linea)
    
    assert len(resultado) == 4
    assert resultado[2] == "Ciudad, Manizales" # No debe romperse en la coma interna

def test_csv_a_diccionario_error_columnas():
    """Confirma arreglo del BUG 2 (Filas desiguales)."""
    csv_data = "nombre,edad\nDiego,30\nError,25,Extra"
    with pytest.raises(ValueError, match="Fila malformada"):
        csv_a_diccionarios(csv_data)

def test_validar_csv_basico():
    assert validar_csv("a,b\n1,2") is True
    assert validar_csv("a,b\n1,2,3") is False # Diferente número de comas

def test_utilidades_csv():
    data = "id,nombre\n1,Diego\n2,IA"
    assert contar_filas(data) == 3
    assert contar_columnas(data) == 2
    assert extraer_columna(data, 1) == ["nombre", "Diego", "IA"]

def test_casos_vacios():
    assert parse_csv_line("") == []
    assert contar_filas("") == 0
    assert csv_a_diccionarios("") == []

def test_csv_a_diccionarios_cobertura():
    from src.csv_parser import csv_a_diccionarios
    
    # Caso: CSV vacío
    assert csv_a_diccionarios("") == []
    
    # Caso: Una sola fila (sin datos)
    assert csv_a_diccionarios("nombre,edad", tiene_cabecera=True) == []   

def test_extraer_columna_indice_invalido():
    data = "a,b\n1,2"
    resultado = extraer_columna(data, 5)  # índice fuera de rango
    assert resultado == ["", ""]

def test_filtrar_por_columna():
    from src.csv_parser import filtrar_por_columna
    data = "nombre,ciudad\nDiego,Manizales\nAna,Bogota\nPedro,Manizales"
    resultado = filtrar_por_columna(data, 1, "Manizales")
    assert len(resultado) == 2
    assert ["Diego", "Manizales"] in resultado

def test_filtrar_csv_vacio():
    from src.csv_parser import filtrar_por_columna
    assert filtrar_por_columna("", 0, "x") == []

def test_leer_csv_como_lista():
    from src.csv_parser import leer_csv_como_lista
    assert leer_csv_como_lista("") == []
    resultado = leer_csv_como_lista("a,b\n1,2")
    assert resultado == [["a", "b"], ["1", "2"]]

def test_contar_columnas_vacio():
    assert contar_columnas("") == 0

def test_validar_csv_vacio():
    assert validar_csv("") is False

