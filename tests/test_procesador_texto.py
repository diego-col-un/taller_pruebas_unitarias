import pytest
from src.procesador_texto import (
    contar_palabras, contar_vocales, invertir_texto,
    es_palindromo, eliminar_espacios_extra,
    convertir_mayusculas, convertir_minusculas,
    capitalizar_palabras, reemplazar_palabra,
    extraer_iniciales, limpiar_texto
)

def test_contar_palabras():
    assert contar_palabras("Tres tristes tigres") == 3
    assert contar_palabras("") == 0

def test_contar_vocales():
    assert contar_vocales("hola mundo") == 4
    assert contar_vocales("") == 0

def test_invertir_texto():
    assert invertir_texto("hola") == "aloh"
    assert invertir_texto("") == ""

def test_es_palindromo():
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("Reconocer") is True
    assert es_palindromo("Python") is False
    assert es_palindromo("") is False
    assert es_palindromo("   ") is False  # solo espacios

def test_eliminar_espacios_extra():
    assert eliminar_espacios_extra("  Muchos    espacios  ") == "Muchos espacios"
    assert eliminar_espacios_extra("") == ""

def test_convertir_mayusculas():
    assert convertir_mayusculas("hola") == "HOLA"
    assert convertir_mayusculas("") == ""

def test_convertir_minusculas():
    assert convertir_minusculas("HOLA") == "hola"
    assert convertir_minusculas("") == ""

def test_capitalizar_palabras():
    assert capitalizar_palabras("hola mundo") == "Hola Mundo"
    assert capitalizar_palabras("") == ""

def test_reemplazar_palabra():
    assert reemplazar_palabra("hola mundo", "hola", "adios") == "adios mundo"
    assert reemplazar_palabra("", "a", "b") == ""

def test_extraer_iniciales():
    assert extraer_iniciales("Diego Armando Maradona") == "DAM"
    assert extraer_iniciales("") == ""

def test_limpiar_texto():
    assert limpiar_texto("Hola@ Mundo!") == "Hola Mundo"
    assert limpiar_texto("") == ""