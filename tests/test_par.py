# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import es_par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_par(self):
        assert es_par(4) == "par"
        assert es_par(5) == "impar"
        assert es_par(6) == "par"
