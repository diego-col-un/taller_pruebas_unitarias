import pytest
from src.validador import validar_fecha, validar_email, validar_password

def test_validar_fecha_borde_febrero():
    """Prueba el BUG de la fecha con estructura AAA."""
    # Arrange
    dia, mes, anio = 31, 2, 2024
    
    # Act
    resultado = validar_fecha(dia, mes, anio)
    
    # Assert
    assert resultado is False, "Febrero no puede tener 31 días"

def test_validar_email_formato():
    """Valida emails correctos e incorrectos (AAA)."""
    # Arrange
    email_valido = "diego@devops.com"
    email_invalido = "diego.com"
    
    # Act & Assert
    assert validar_email(email_valido) is True
    assert validar_email(email_invalido) is False

def test_validar_password_seguridad():
    """Valida requisitos de contraseña (AAA)."""
    # Arrange
    pass_debil = "12345"
    pass_fuerte = "DevOps2026"
    
    # Act & Assert
    assert validar_password(pass_debil) is False
    assert validar_password(pass_fuerte) is True

def test_cobertura_validador():
    # Arrange / Act / Assert
    from src.validador import validar_cedula, validar_url, validar_edad
    
    # Probamos ramas de éxito y error para validar_edad
    assert validar_edad(25) is True
    assert validar_edad("veinte") is False  # Cubre el isinstance
    assert validar_edad(-1) is False        # Cubre el < 0
    assert validar_edad(150) is False       # Cubre el > 120
    
    # Probamos validar_url
    assert validar_url("https://google.com") is True
    assert validar_url(None) is False
    
    # Probamos validar_cedula
    assert validar_cedula(1234567) is True
    assert validar_cedula("abc") is False

def test_validador_casos_vacios():
    from src.validador import validar_email, validar_telefono, validar_password
    assert validar_email("") is False      # Línea 12
    assert validar_telefono(None) is False # Línea 19
    assert validar_password("") is False   # Línea 24

def test_validar_telefono_valido():
    from src.validador import validar_telefono
    assert validar_telefono("3001234567") is True
    assert validar_telefono("300-123-4567") is True
    assert validar_telefono("123") is False     # muy corto
    assert validar_telefono("abc123") is False  # letras

def test_validar_fecha_valida_e_invalida():
    assert validar_fecha(15, 6, 2023) is True
    assert validar_fecha(31, 4, 2023) is False   # abril no tiene 31
    assert validar_fecha(29, 2, 2023) is False   # 2023 no es bisiesto
    assert validar_fecha(29, 2, 2024) is True    # 2024 sí es bisiesto
    assert validar_fecha(1, 1, 1800) is False    # fuera del rango (< 1900)
    assert validar_fecha(1, 1, 2200) is False    # fuera del rango (> 2100)

def test_validar_fecha_tipos_invalidos():
    assert validar_fecha("01", 1, 2023) is False  # cubre el isinstance

def test_validar_email_sin_punto_en_dominio():
    from src.validador import validar_email
    assert validar_email("user@dominio") is False  # sin punto en dominio
    assert validar_email("@dominio.com") is False  # sin usuario
    assert validar_email("user@") is False          # sin dominio    