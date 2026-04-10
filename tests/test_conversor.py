import pytest
from src.conversor import (
    celsius_a_fahrenheit, fahrenheit_a_celsius,
    celsius_a_kelvin, kelvin_a_celsius,
    metros_a_kilometros, kilometros_a_metros,
    libras_a_kilogramos, kilogramos_a_libras,
    galones_a_litros, litros_a_galones,
    millas_a_kilometros, kilometros_a_millas,
    pies_a_metros, metros_a_pies,
    onzas_a_gramos, gramos_a_onzas
)

def test_temperaturas():
    assert celsius_a_fahrenheit(0) == 32
    assert fahrenheit_a_celsius(32) == 0
    assert celsius_a_kelvin(0) == 273.15
    assert kelvin_a_celsius(273.15) == 0
    with pytest.raises(ValueError, match="cero absoluto"):
        kelvin_a_celsius(-1)

def test_distancias():
    assert metros_a_kilometros(1000) == 1
    assert kilometros_a_metros(1) == 1000
    assert millas_a_kilometros(1) == 1.60934
    assert pytest.approx(kilometros_a_millas(1.60934), 0.0001) == 1
    assert pies_a_metros(1) == 0.3048
    assert metros_a_pies(0.3048) == pytest.approx(1, 0.0001)

def test_distancias_errores():
    with pytest.raises(ValueError):
        metros_a_kilometros(-1)
    with pytest.raises(ValueError):
        kilometros_a_metros(-1)
    with pytest.raises(ValueError):
        millas_a_kilometros(-5)
    with pytest.raises(ValueError):
        kilometros_a_millas(-1)
    with pytest.raises(ValueError):
        pies_a_metros(-1)
    with pytest.raises(ValueError):
        metros_a_pies(-1)

def test_pesos():
    assert libras_a_kilogramos(1) == 0.453592
    assert kilogramos_a_libras(0.453592) == pytest.approx(1, 0.0001)
    assert onzas_a_gramos(1) == 28.3495
    assert gramos_a_onzas(28.3495) == pytest.approx(1, 0.0001)

def test_pesos_errores():
    with pytest.raises(ValueError):
        libras_a_kilogramos(-1)
    with pytest.raises(ValueError):
        kilogramos_a_libras(-1)
    with pytest.raises(ValueError):
        onzas_a_gramos(-1)
    with pytest.raises(ValueError):
        gramos_a_onzas(-1)

def test_volumen():
    assert galones_a_litros(1) == 3.78541
    assert litros_a_galones(3.78541) == pytest.approx(1, 0.0001)

def test_volumen_errores():
    with pytest.raises(ValueError):
        galones_a_litros(-1)
    with pytest.raises(ValueError):
        litros_a_galones(-1)