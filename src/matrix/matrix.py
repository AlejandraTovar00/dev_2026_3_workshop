class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    Incluye operaciones aritméticas, propiedades y transformaciones matriciales.
    """

    def suma_matrices(self, A, B):
        """
        Suma dos matrices elemento a elemento.
        """
        if len(A) != len(B) or any(len(fA) != len(fB) for fA, fB in zip(A, B)):
            raise ValueError("Las matrices tienen dimensiones incompatibles")
        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[i])):
                fila.append(A[i][j] + B[i][j])
            resultado.append(fila)
        return resultado

    def resta_matrices(self, A, B):
        """
        Resta dos matrices elemento a elemento (A - B).
        """
        if len(A) != len(B) or any(len(fA) != len(fB) for fA, fB in zip(A, B)):
            raise ValueError("Las matrices tienen dimensiones incompatibles")
        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[i])):
                fila.append(A[i][j] - B[i][j])
            resultado.append(fila)
        return resultado

    def multiplicar_matrices(self, A, B):
        """
        Multiplica dos matrices usando la multiplicación matricial estándar.
        """
        filas_A, columnas_A = len(A), len(A[0])
        filas_B, columnas_B = len(B), len(B[0])
        if columnas_A != filas_B:
            raise ValueError("Dimensiones incompatibles para multiplicación")
        
        resultado = [[0] * columnas_B for _ in range(filas_A)]
        for i in range(filas_A):
            for j in range(columnas_B):
                suma = 0
                for k in range(columnas_A):
                    suma += A[i][k] * B[k][j]
                resultado[i][j] = suma
        return resultado

    def multiplicar_escalar(self, matriz, escalar):
        """
        Multiplica cada elemento de la matriz por un escalar.
        """
        resultado = []
        for fila in matriz:
            nueva_fila = [elemento * escalar for elemento in fila]
            resultado.append(nueva_fila)
        return resultado

    def transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        """
        if len(matriz) == 0:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            resultado.append(nueva_fila)
        return resultado

    def es_cuadrada(self, matriz):
        """
        Verifica si una matriz es cuadrada.
        """
        if len(matriz) == 0:
            return False
        for fila in matriz:
            if len(fila) != len(matriz):
                return False
        return True

    def es_simetrica(self, matriz):
        """
        Verifica si una matriz es simétrica.
        """
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if matriz[i][j] != matriz[j][i]:
                    return False
        return True

    def traza(self, matriz):
        """
        Calcula la traza de una matriz cuadrada.
        """
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][i]
        return suma

    def determinante_2x2(self, matriz):
        """
        Calcula el determinante de una matriz 2x2.
        """
        if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
            raise ValueError("La matriz no es 2x2")
        a, b = matriz[0]
        c, d = matriz[1]
        return a * d - b * c

    def determinante_3x3(self, matriz):
        """
        Calcula el determinante de una matriz 3x3 usando la regla de Sarrus.
        """
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz no es 3x3")
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        return (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)

    def identidad(self, n):
        """
        Genera una matriz identidad de tamaño n x n.
        """
        resultado = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(1 if i == j else 0)
            resultado.append(fila)
        return resultado

    def diagonal(self, matriz):
        """
        Extrae los elementos de la diagonal principal de una matriz cuadrada.
        """
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")
        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
        """
        Verifica si una matriz cuadrada es diagonal.
        """
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if i != j and matriz[i][j] != 0:
                    return False
        return True

    def rotar_90(self, matriz):
        """
        Rota una matriz 90 grados en sentido horario.
        """
        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = [[0] * filas for _ in range(columnas)]
        for i in range(filas):
            for j in range(columnas):
                resultado[j][filas - 1 - i] = matriz[i][j]
        return resultado

    def buscar_en_matriz(self, matriz, valor):
        """
        Busca un valor en la matriz y retorna todas las posiciones donde se encuentra.
        """
        posiciones = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))
        return posiciones
# Ejercicio de matrix completado
