class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        """
        if len(numeros) == 0:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        """
        if len(numeros) == 0:
            return 0
        ordenados = sorted(numeros)
        n = len(ordenados)
        mitad = n // 2
        if n % 2 == 0:
            return (ordenados[mitad - 1] + ordenados[mitad]) / 2
        else:
            return float(ordenados[mitad])
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        """
        if len(numeros) == 0:
            return None
        conteo = {}
        for numero in numeros:
            conteo[numero] = conteo.get(numero, 0) + 1
        
        max_frecuencia = 0
        moda_resultado = numeros[0]
        for numero in numeros:
            if conteo[numero] > max_frecuencia:
                max_frecuencia = conteo[numero]
                moda_resultado = numero
        return moda_resultado
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números (poblacional).
        """
        if len(numeros) == 0:
            return 0
        return self.varianza(numeros) ** 0.5
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números (poblacional).
        """
        if len(numeros) == 0:
            return 0
        media = self.promedio(numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        return suma_cuadrados / len(numeros)
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        """
        if len(numeros) == 0:
            return 0
        diferencia = max(numeros) - min(numeros)
        return round(diferencia, 10)
# Ejercicio de stats completado