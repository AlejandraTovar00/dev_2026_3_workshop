import math

class Formulas:
    """
    Clase con ejercicios de fórmulas de física, finanzas y álgebra.
    """

    def velocidad_media(self, distancia, tiempo):
        """
        Calcula la velocidad media de un recorrido.
        Fórmula: v = d / t
        """
        return distancia / tiempo

    def mruv_posicion(self, posicion_inicial, velocidad_inicial, aceleracion, tiempo):
        """
        Calcula la posición de un móvil con aceleración constante (MRUV).
        Fórmula: x = x0 + v0*t + (1/2)*a*t^2
        """
        return posicion_inicial + velocidad_inicial * tiempo + 0.5 * aceleracion * tiempo ** 2

    def mruv_velocidad(self, velocidad_inicial, aceleracion, tiempo):
        """
        Calcula la velocidad final de un móvil con aceleración constante (MRUV).
        Fórmula: v = v0 + a*t
        """
        return velocidad_inicial + aceleracion * tiempo

    def fuerza_newton(self, masa, aceleracion):
        """
        Calcula la fuerza según la segunda ley de Newton.
        Fórmula: F = m * a
        """
        return masa * aceleracion

    def energia_cinetica(self, masa, velocidad):
        """
        Calcula la energía cinética de un objeto en movimiento.
        Fórmula: Ec = (1/2) * m * v^2
        """
        return 0.5 * masa * velocidad ** 2

    def energia_potencial(self, masa, altura, gravedad=9.8):
        """
        Calcula la energía potencial gravitatoria de un objeto.
        Fórmula: Ep = m * g * h
        """
        return masa * gravedad * altura

    def ley_ohm_voltaje(self, corriente, resistencia):
        """
        Calcula el voltaje usando la ley de Ohm.
        Fórmula: V = I * R
        """
        return corriente * resistencia

    def ley_ohm_corriente(self, voltaje, resistencia):
        """
        Calcula la corriente usando la ley de Ohm.
        Fórmula: I = V / R
        """
        return voltaje / resistencia

    def interes_simple(self, capital, tasa, tiempo):
        """
        Calcula el interés generado por un capital a interés simple.
        Fórmula: I = C * r * t
        """
        return capital * tasa * tiempo

    def interes_compuesto(self, capital, tasa, tiempo, n=1):
        """
        Calcula el monto final de un capital a interés compuesto.
        Fórmula: M = C * (1 + r/n)^(n*t)
        """
        return capital * (1 + tasa / n) ** (n * tiempo)

    def discriminante(self, a, b, c):
        """
        Calcula el discriminante de una ecuación cuadrática ax^2 + bx + c = 0.
        Fórmula: D = b^2 - 4*a*c
        """
        return b ** 2 - 4 * a * c

    def raices_cuadraticas(self, a, b, c):
        """
        Calcula las raíces reales de una ecuación cuadrática ax^2 + bx + c = 0.
        Fórmula: x = (-b ± sqrt(b^2 - 4ac)) / (2a)
        """
        d = b ** 2 - 4 * a * c
        if d < 0:
            raise ValueError("El discriminante es negativo, no hay raíces reales")
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        raiz2 = (-b - math.sqrt(d)) / (2 * a)
        return (raiz1, raiz2)

    def imc(self, peso, altura):
        """
        Calcula el Índice de Masa Corporal (IMC).
        Fórmula: IMC = peso / altura^2
        """
        return peso / altura ** 2

    def hipotenusa_pitagoras(self, cateto1, cateto2):
        """
        Calcula la longitud de la hipotenusa de un triángulo rectángulo.
        Fórmula: h = sqrt(cateto1^2 + cateto2^2)
        """
        return math.sqrt(cateto1 ** 2 + cateto2 ** 2)
# Ejercicio de formulas completado