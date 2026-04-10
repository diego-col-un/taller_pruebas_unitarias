import pytest
from src.utils import (
    celsius_a_fahrenheit, fahrenheit_a_celsius,
    celsius_a_kelvin, kelvin_a_celsius,
    calcular_imc, categorizar_imc,
    calcular_edad, es_bisiesto, dias_en_mes,
    es_primo, mcd, mcm
)

def test_conversiones_temperatura():
    assert celsius_a_fahrenheit(0) == 32
    assert fahrenheit_a_celsius(32) == 0
    assert celsius_a_kelvin(0) == 273.15
    assert kelvin_a_celsius(273.15) == 0

def test_calcular_imc():
    assert pytest.approx(calcular_imc(70, 1.75), 0.01) == 22.86
    with pytest.raises(ValueError):
        calcular_imc(0, 1.75)
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

def test_categorizar_imc_todas_ramas():
    assert categorizar_imc(17) == "Bajo peso"
    assert categorizar_imc(22) == "Normal"
    assert categorizar_imc(27) == "Sobrepeso"
    assert categorizar_imc(35) == "Obesidad"

def test_calcular_edad():
    assert calcular_edad(2000, 2025) == 25
    with pytest.raises(ValueError):
        calcular_edad(2030, 2025)

def test_es_bisiesto():
    assert es_bisiesto(2024) is True
    assert es_bisiesto(1900) is False  # divisible por 100 pero no por 400
    assert es_bisiesto(2000) is True   # divisible por 400
    assert es_bisiesto(2023) is False

def test_dias_en_mes():
    assert dias_en_mes(1, 2024) == 31   # enero
    assert dias_en_mes(4, 2024) == 30   # abril (30 días)
    assert dias_en_mes(2, 2024) == 29   # febrero bisiesto
    assert dias_en_mes(2, 2023) == 28   # febrero no bisiesto
    with pytest.raises(ValueError):
        dias_en_mes(13, 2024)

def test_es_primo():
    assert es_primo(7) is True
    assert es_primo(10) is False
    assert es_primo(1) is False
    assert es_primo(2) is True

def test_mcd():
    assert mcd(12, 8) == 4
    assert mcd(7, 3) == 1

def test_mcm():
    assert mcm(12, 18) == 36
    assert mcm(0, 5) == 0
    assert mcm(4, 6) == 12