import pytest
from src.formulas.formulas import Formulas

class TestFormulas:
    def setup_method(self):
        self.formulas = Formulas()

    def test_velocidad_media(self):
        # Test con valores enteros
        assert self.formulas.velocidad_media(100, 10) == 10.0
        # Test con otro recorrido
        assert self.formulas.velocidad_media(60, 2) == 30.0
        # Test con distancia cero
        assert self.formulas.velocidad_media(0, 5) == 0.0

    def test_mruv_posicion(self):
        # Test con aceleración positiva
        assert self.formulas.mruv_posicion(0, 2, 1, 3) == 10.5
        # Test con velocidad inicial cero
        assert self.formulas.mruv_posicion(5, 0, 2, 2) == 9.0
        # Test con aceleración cero (movimiento uniforme)
        assert self.formulas.mruv_posicion(0, 10, 0, 5) == 50.0

    def test_mruv_velocidad(self):
        # Test con aceleración positiva
        assert self.formulas.mruv_velocidad(2, 1, 3) == 5.0
        # Test con velocidad inicial cero
        assert round(self.formulas.mruv_velocidad(0, 9.8, 2), 2) == 19.6
        # Test con aceleración negativa (frenado)
        assert self.formulas.mruv_velocidad(10, -2, 3) == 4.0

    def test_fuerza_newton(self):
        # Test con valores enteros
        assert self.formulas.fuerza_newton(10, 2) == 20.0
        # Test con aceleración cero (fuerza cero)
        assert self.formulas.fuerza_newton(5, 0) == 0.0
        # Test con valores decimales
        assert self.formulas.fuerza_newton(2.5, 4) == 10.0

    def test_energia_cinetica(self):
        # Test con valores enteros
        assert self.formulas.energia_cinetica(2, 3) == 9.0
        # Test con velocidad cero (energía cero)
        assert self.formulas.energia_cinetica(1, 0) == 0.0
        # Test con otros valores
        assert self.formulas.energia_cinetica(4, 5) == 50.0

    def test_energia_potencial(self):
        # Test con gravedad por defecto (9.8)
        assert self.formulas.energia_potencial(2, 5) == 98.0
        # Test con altura cero (energía cero)
        assert self.formulas.energia_potencial(10, 0) == 0.0
        # Test con gravedad personalizada
        assert self.formulas.energia_potencial(1, 10, 10) == 100.0

    def test_ley_ohm_voltaje(self):
        # Test con valores enteros
        assert self.formulas.ley_ohm_voltaje(2, 5) == 10.0
        # Test con corriente cero (voltaje cero)
        assert self.formulas.ley_ohm_voltaje(0, 5) == 0.0
        # Test con otros valores
        assert self.formulas.ley_ohm_voltaje(3, 3) == 9.0

    def test_ley_ohm_corriente(self):
        # Test con valores enteros
        assert self.formulas.ley_ohm_corriente(10, 5) == 2.0
        # Test con voltaje cero (corriente cero)
        assert self.formulas.ley_ohm_corriente(0, 5) == 0.0
        # Test con otros valores
        assert self.formulas.ley_ohm_corriente(9, 3) == 3.0

    def test_interes_simple(self):
        # Test con valores típicos
        assert self.formulas.interes_simple(1000, 0.05, 2) == 100.0
        # Test con otra tasa
        assert self.formulas.interes_simple(500, 0.1, 1) == 50.0
        # Test con tasa cero (interés cero)
        assert self.formulas.interes_simple(1000, 0, 5) == 0.0

    def test_interes_compuesto(self):
        # Test con capitalización anual (n=1 por defecto)
        assert self.formulas.interes_compuesto(1000, 0.05, 2) == 1102.5
        # Test con capitalización trimestral (n=4)
        assert round(self.formulas.interes_compuesto(1000, 0.05, 2, 4), 2) == 1104.49
        # Test con capitalización mensual (n=12)
        assert round(self.formulas.interes_compuesto(2000, 0.1, 3, 12), 2) == 2696.36

    def test_discriminante(self):
        # Test con discriminante positivo
        assert self.formulas.discriminante(1, -3, 2) == 1
        # Test con otro discriminante positivo
        assert self.formulas.discriminante(2, 4, -6) == 64
        # Test con discriminante negativo
        assert self.formulas.discriminante(1, 2, 5) == -16

    def test_raices_cuadraticas(self):
        # Test con raíces enteras distintas
        assert self.formulas.raices_cuadraticas(1, -3, 2) == (2.0, 1.0)
        # Test con raíces simétricas
        assert self.formulas.raices_cuadraticas(1, 0, -4) == (2.0, -2.0)
        # Test con otras raíces
        assert self.formulas.raices_cuadraticas(2, 4, -6) == (1.0, -3.0)
        # Test con discriminante negativo (no hay raíces reales)
        with pytest.raises(ValueError):
            self.formulas.raices_cuadraticas(1, 2, 5)

    def test_imc(self):
        # Test con valores típicos
        assert round(self.formulas.imc(70, 1.75), 2) == 22.86
        # Test con otros valores
        assert round(self.formulas.imc(60, 1.6), 2) == 23.44

    def test_hipotenusa_pitagoras(self):
        # Test con triángulo 3-4-5
        assert self.formulas.hipotenusa_pitagoras(3, 4) == 5.0
        # Test con triángulo 5-12-13
        assert self.formulas.hipotenusa_pitagoras(5, 12) == 13.0
        # Test con catetos iguales
        assert round(self.formulas.hipotenusa_pitagoras(1, 1), 2) == 1.41
