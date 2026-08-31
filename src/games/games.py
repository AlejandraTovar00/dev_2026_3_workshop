import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        """
        opciones_validas = ["piedra", "papel", "tijera"]
        j1 = jugador1.lower()
        j2 = jugador2.lower()
        
        if j1 not in opciones_validas or j2 not in opciones_validas:
            return "invalid"
        
        if j1 == j2:
            return "empate"
        
        gana_jugador1 = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }
        
        if gana_jugador1[j1] == j2:
            return "jugador1"
        else:
            return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        """
        lineas = []
        

        for i in range(3):
            lineas.append(tablero[i])
        

        for j in range(3):
            lineas.append([tablero[0][j], tablero[1][j], tablero[2][j]])
        

        lineas.append([tablero[0][0], tablero[1][1], tablero[2][2]])
        lineas.append([tablero[0][2], tablero[1][1], tablero[2][0]])
        
        for linea in lineas:
            if linea[0] != " " and linea[0] == linea[1] == linea[2]:
                return linea[0]
        

        for fila in tablero:
            for celda in fila:
                if celda == " ":
                    return "continua"
        
        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        """
        combinacion = []
        for _ in range(longitud):
            combinacion.append(random.choice(colores_disponibles))
        return combinacion
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        """

        for valor in [desde_fila, desde_col, hasta_fila, hasta_col]:
            if valor < 0 or valor > 7:
                return False
        

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            col = desde_col + paso
            while col != hasta_col:
                if tablero[desde_fila][col] != " ":
                    return False
                col += paso
            return True
        

        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            fila = desde_fila + paso
            while fila != hasta_fila:
                if tablero[fila][desde_col] != " ":
                    return False
                fila += paso
            return True