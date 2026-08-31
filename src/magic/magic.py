import math

class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        """
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        anterior, actual = 0, 1
        for _ in range(2, n + 1):
            anterior, actual = actual, anterior + actual
        return actual
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        """
        if n <= 0:
            return []
        secuencia = [0]
        if n == 1:
            return secuencia
        secuencia.append(1)
        while len(secuencia) < n:
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        """
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        """
        primos = []
        for numero in range(2, n + 1):
            if self.es_primo(numero):
                primos.append(numero)
        return primos
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        """
        if n <= 1:
            return False
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        """
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        """
        if n < 0:
            return None
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        """
        while b != 0:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        """
        n = abs(n)
        suma = 0
        for digito in str(n):
            suma += int(digito)
        return suma
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong.
        """
        digitos = str(n)
        num_digitos = len(digitos)
        suma = 0
        for digito in digitos:
            suma += int(digito) ** num_digitos
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico.
        """
        n = len(matriz)
        if n == 1:
            return True
        
        suma_esperada = sum(matriz[0])
        

        for fila in matriz:
            if sum(fila) != suma_esperada:
                return False
        

        for j in range(n):
            suma_columna = sum(matriz[i][j] for i in range(n))
            if suma_columna != suma_esperada:
                return False
        

        suma_diag1 = sum(matriz[i][i] for i in range(n))
        if suma_diag1 != suma_esperada:
            return False
        

        suma_diag2 = sum(matriz[i][n - 1 - i] for i in range(n))
        if suma_diag2 != suma_esperada:
            return False
        
        return True
# Ejercicio de magic completado