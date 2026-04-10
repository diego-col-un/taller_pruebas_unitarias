import pytest
from src.manipulador_texto import (
    invertir_cadena, contar_vocales, es_palindromo, 
    dividir_en_palabras, extraer_dominio, enmascarar_email, truncar
)

def test_es_palindromo_complejo():
    """Confirma arreglo del BUG 1."""
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("No lemon, no melon") is True
    assert es_palindromo("hola") is False

def test_dividir_palabras_espacios_multiples():
    """Confirma arreglo del BUG 2."""
    texto = "Hola    mundo   desde Python"
    resultado = dividir_en_palabras(texto)
    assert resultado == ["Hola", "mundo", "desde", "Python"]
    assert "" not in resultado

def test_emails():
    email = "diego@gmail.com"
    assert extraer_dominio(email) == "gmail.com"
    assert enmascarar_email(email) == "d***o@gmail.com"
    assert enmascarar_email("ab@c.com") == "ab@c.com"

def test_utilidades_texto():
    assert invertir_cadena("abc") == "cba"
    assert contar_vocales("murcielago") == 5
    assert truncar("Hola Mundo", 7) == "Hola..."

def test_manipulador_cobertura_full():
    from src.manipulador_texto import (
        contar_consonantes, eliminar_duplicados, 
        capitalizar_palabras, convertir_a_titulo, reemplazar_subcadena
    )
    assert contar_consonantes("abc") == 2
    assert eliminar_duplicados("aaabbb") == "ab"
    assert capitalizar_palabras("hola mundo") == "Hola Mundo"
    assert convertir_a_titulo("hola") == "Hola"
    assert reemplazar_subcadena("hola", "h", "j") == "jola"

def test_palindromo_solo_simbolos():
    from src.manipulador_texto import es_palindromo
    assert es_palindromo("   ") is False   # solo espacios → cadena_limpia vacía
    assert es_palindromo("") is False

def test_extraer_dominio_invalido():
    assert extraer_dominio("") == ""
    assert extraer_dominio("sinArroba") == ""
    assert extraer_dominio("a@b@c") == ""  # más de un @

def test_enmascarar_email_invalido():
    assert enmascarar_email("") == ""
    assert enmascarar_email("sinArroba") == ""
    assert enmascarar_email("a@b@c") == ""

def test_normalizar_espacios():
    from src.manipulador_texto import normalizar_espacios
    assert normalizar_espacios("  hola   mundo  ") == "hola mundo"
    assert normalizar_espacios("") == ""

def test_es_anagrama():
    from src.manipulador_texto import es_anagrama
    assert es_anagrama("amor", "roma") is True
    assert es_anagrama("hola", "mundo") is False
    assert es_anagrama("", "algo") is False

def test_truncar_sin_truncar():
    assert truncar("Hola", 10) == "Hola"  # texto más corto que longitud
    assert truncar("", 5) == ""

def test_reemplazar_con_limite():
    from src.manipulador_texto import reemplazar_subcadena
    assert reemplazar_subcadena("aaa", "a", "b", 2) == "bba"
    assert reemplazar_subcadena("", "a", "b") == ""    