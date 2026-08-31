class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        Formula: F = (C x 9/5) + 32
        """
        return celsius * 9/5 +32
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Fórmula: C = (F - 32) × 5/9
        """
        return (fahrenheit - 32) * 5/9
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.  
        Factor: 1 metro = 3.28084 pies
        """
        return metros * 3.28084
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.   
        Factor: 1 pie = 0.3048 metros
        """
        return pies * 0.3048
    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        """
        return bin(decimal)[2:]
    
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        """
        return int(binario, 2)
    
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        """
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        resultado = ""
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        """
        valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M":1000}
        total = 0
        for i in range(len(romano)):
            actual = valores[romano[i]]
            if i + 1 < len(romano) and actual < valores[romano[i + 1]]:
                total -= actual
            else:
                total += actual
        return total
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        """
        morse = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }
        if texto == "":
            return ""
        texto = texto.upper()
        return " ".join(morse[caracter] for caracter in texto)
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        """
        morse_inverso = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
            '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
            '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
            '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
            '--..': 'Z',
            '-----': '0', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7',
            '---..': '8', '----.': '9'
        }
        if morse.strip() == "":
            return ""
        codigos = morse.split()
        return "".join(morse_inverso[codigo] for codigo in codigos)