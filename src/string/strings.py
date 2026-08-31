class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo.
        """
        limpio = texto.lower().replace(" ", "")
        return limpio == self.invertir_cadena(limpio)
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        """
        resultado = ""
        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]
        return resultado
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for char in texto:
            if char in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for char in texto:
            if char.isalpha() and char not in vocales:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas.
        """
        limpio1 = texto1.lower().replace(" ", "")
        limpio2 = texto2.lower().replace(" ", "")
        return sorted(limpio1) == sorted(limpio2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        """
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        """
        if texto == "":
            return ""
        resultado = []
        capitalizar_siguiente = True
        for char in texto:
            if char == " ":
                resultado.append(char)
                capitalizar_siguiente = True
            else:
                if capitalizar_siguiente:
                    resultado.append(char.upper())
                    capitalizar_siguiente = False
                else:
                    resultado.append(char.lower())
        return "".join(resultado)
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        """
        if texto == "":
            return ""
        resultado = []
        espacio_anterior = False
        for char in texto:
            if char == " ":
                if not espacio_anterior:
                    resultado.append(char)
                espacio_anterior = True
            else:
                resultado.append(char)
                espacio_anterior = False
        return "".join(resultado)
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        """
        if texto == "":
            return False
        inicio = 0
        if texto[0] == "-" or texto[0] == "+":
            inicio = 1
            if len(texto) == 1:
                return False
        for i in range(inicio, len(texto)):
            if texto[i] < "0" or texto[i] > "9":
                return False
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        """
        resultado = []
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                nuevo = (ord(char) - base + desplazamiento) % 26 + base
                resultado.append(chr(nuevo))
            else:
                resultado.append(char)
        return "".join(resultado)
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto.
        """
        if subcadena == "":
            return []
        posiciones = []
        n = len(texto)
        m = len(subcadena)
        for i in range(n - m + 1):
            if texto[i:i+m] == subcadena:
                posiciones.append(i)
        return posiciones