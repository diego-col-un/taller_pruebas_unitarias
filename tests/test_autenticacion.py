import pytest
import time
from src.autenticacion import (
    hash_contraseña, verificar_contraseña, validar_usuario,
    generar_token, validar_token, generar_codigo_2fa,
    verificar_codigo_2fa, sanear_entrada
)

def test_autenticacion_completo():
    """Prueba todas las funciones para alcanzar el 100% de cobertura."""
    
    # --- ARRANGE ---
    usuario_valido = "diego_devops"
    pass_plana = "Segura123!"
    ahora = time.time()
    
    # --- ACT & ASSERT ---

    # 1. Test de Contraseñas
    h = hash_contraseña(pass_plana)
    assert verificar_contraseña(pass_plana, h) is True
    with pytest.raises(TypeError):
        hash_contraseña(None)

    # 2. Test de Usuarios (Cubre todas las ramas de longitud y regex)
    assert validar_usuario(usuario_valido) is True
    assert validar_usuario("") is False
    assert validar_usuario("ab") is False            # Muy corto
    assert validar_usuario("a" * 21) is False        # Muy largo
    assert validar_usuario("user!@#") is False       # Caracteres inválidos

    # 3. Test de Tokens
    token = generar_token(usuario_valido, ahora)
    assert validar_token(token) is True
    assert validar_token("") is False
    assert validar_token("short") is False
    assert validar_token("g" * 32) is False          # No hexadecimal (fuerza el except)

    # 4. Test de 2FA
    codigo = generar_codigo_2fa()
    assert len(codigo) == 6
    assert verificar_codigo_2fa(codigo, codigo) is True
    assert verificar_codigo_2fa("", codigo) is False

    # 5. Test de Saneamiento (El del error del espacio)
    entrada_sucia = "<script>; --"
    resultado = sanear_entrada(entrada_sucia)
    assert ";" not in resultado
    assert "--" not in resultado
    assert sanear_entrada(None) == ""