import random
import src.utils.colors_symbols as col_sym
import src.utils.util as utl

symbol = []

def printIntro(introFile = "") -> None:
    '''
        Firma:
            (string) -> ()

        Sinopsis:
            Función que imprime el contenido de un archivo en pantalla, en este
    		caso, el mensaje de bienvenida al juego

        Entradas y salidas:
            - introFile: Nombre del archivo que contiene la presentación del juego
            - returns: None, solo imprime el archivo leído en pantalla

        Ejemplos de uso:

            >>> printIntro("intro.txt")

            ████████╗██████╗ ██╗ ██████╗ ██╗   ██╗██╗
            ╚══██╔══╝██╔══██╗██║██╔═══██╗██║   ██║██║
               ██║   ██████╔╝██║██║   ██║██║   ██║██║
               ██║   ██╔══██╗██║██║▄▄ ██║██║   ██║██║
               ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║
               ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝
    '''

    # Desarrolle el cuerpo de la función aquí...
    try:
        file = open(introFile, "r", encoding="utf-8")
        content = file.read()
        file.close()
        print(col_sym.YELLOW)
        print("=" * 50)
        print("=" * 50)
        print(col_sym.GREEN)
        print(content)
        print(col_sym.YELLOW, end="")
        print("=" * 50)
        print("=" * 50)
        print(col_sym.WHITE)
        utl.systemMessage("Desarrollado por: Mayker Escudero - Jaime Montoya")
    except FileNotFoundError as e:
        print("Error al abrir el archivo:", e)
    

def drawBoard(board) -> None:
    # Esta función imprime el tablero en la consola
    # Argumentos:
    # Board: Lista de strings que representa el estado del tablero

    # Desarrolle el cuerpo de la función aquí...
    print("-" * 20)
    print("Tablero")
    print("-" * 20)

    print(board[6] + "|" + board[7] + "|" + board[8])
    print("-+-+--+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+--+-+-")
    print(board[0] + "|" + board[1] + "|" + board[2])

    print("-" * 20)


def inputPlayerLetter() -> list:
    # Esta función le permite escoger al usuario entre la letra "X" y la letra "O".

    # retorna una lista de strings donde la letra escogida por el usuario
    # ocupa la primera posición y la letra que le corresponde a la computadora
    # ocupa la segunda posición.

    # Desarrolle el cuerpo de la función aquí...
    char = ""
    while char != "X" and char != "O":
        print(col_sym.GREEN + "-" * 20 + "\n" + "Seleccionar símbolo" + 
              "\n" + "-" * 20 + col_sym.WHITE)
        char = input("Símbolo a usar [X | O]: ").upper()
        if char != "X" and char != "O":
            utl.systemMessage("Debe usar uno de los símbolos 'X' u 'O' para jugar. " \
                "Intente de nuevo ", "error")
        else:
            if char == "X":
                symbol.append("X")
                symbol.append("O")
            else: 
                symbol.append("O")
                symbol.append("X")
    return symbol
    

def whoGoesFirst() -> str:
    # Esta función escoge de forma aleatoria quien inicial el juego.

    # Retorna el string "Usuario" si el usuario inicia el juego o
    # el string "Computadora" si la computadora inicia el juego.

    # Desarrolle el cuerpo de la función aquí...
    # Se genera un número aleatorio entero: 1 (Usuario) o 2 (Computadora) 
    rand = random.randint(1, 2)
    return "Usuario" if rand == 1 else "Computadora"


def makeMove(board, letter, move) -> None:
    # Esta función actualiza el estado del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: Es la marca que se desea poner en el tablero ("X" o "O").
    # move: Es el número de la casilla donde se desea poner la marca.

    # Desarrolle el cuerpo de la función aquí...
    board[move] = f' {letter} '
    

def isWinner(board, letter) -> bool:
    # Esta función debe verificar si hay una jugada ganadora en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: La marca que se desea verificar ("X" o "O").

    # Esta función debe retornar el valor lógico True, si hay una jugada ganadora o
    # debe retornar el valor lógico False, si no hay una jugada ganadora.

    # Desarrolle el cuerpo de la función aquí...
    # Verificar filas
    if f" {letter} " == board[0] == board[1] == board[2]:
        return True
    elif f" {letter} " == board[3] == board[4] == board[5]:
        return True
    elif f" {letter} " == board[6] == board[7] == board[8]:
        return True
    
    # Verificar columnas
    elif f" {letter} " == board[0] == board[3] == board[6]:
        return True
    elif f" {letter} " == board[1] == board[4] == board[7]:
        return True
    elif f" {letter} " == board[2] == board[5] == board[8]:
        return True
    
    # Verificar diagonales
    elif f" {letter} " == board[2] == board[4] == board[6]:
        return True
    elif f" {letter} " == board[0] == board[4] == board[8]:
        return True
    
    else:
        return False


def isSpaceFree(board, move) -> bool:
    # Esta función verifica si hay una casilla vacía en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # move: Es el número de la casilla que se desea verificar.

    # Esta función debe retornar el valor lógico True, si la casilla está vacía
    # en caso contrario, debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    
    # Validaciones para pruebas de caja negra
    if not isinstance(move, int):
        raise TypeError("El movimiento debe ser un número entero")
    
    if move < 0 or move > 8:
        raise ValueError("El movimiento debe estar entre 1 y 9")
    
    return board[move] == '   '
        

def getPlayerMove(board) -> int:
    # Esta función le pide al usuario que ingrese el número de la casilla
    # que quiere marcar.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función retorna el número de la casilla seleccionada por el usuario.

    # Desarrolle el cuerpo de la función aquí...
    move = 0
    while move < 1 or not isSpaceFree(board, move - 1):
        flag = False
        while not flag:
            value = input("Casilla (celda 1-9): ").strip()
            flag = utl.validateInput(value)
            if not flag:
                utl.systemMessage("Casilla no válida, Intente de nuevo", "error")
            
        move = int(value)
        if not isSpaceFree(board, move - 1):
            utl.systemMessage("Casilla no válida, Intente de nuevo", "error")
    return move
   
    
def chooseRandomMoveFromList(board, movesList) -> int:
    # Esta función escoge de forma aleatoria una casilla vacía del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # moveList: Lista que contiene los números de las casillas a verificar (ver documento de la práctica).

    # Esta función debe retornar alguno de los números de casillas en moveList
    # desde que dicha casilla esté vacía. Si ninguna de las casillas está vacía,
    # esta función debe retornar el valor None.

    # Desarrolle el cuerpo de la función aquí...
    i = 0
    cellRand = -1
    while i < len(board):
        j = 0
        while j < len(movesList):
            if not isSpaceFree(board, movesList[j]):
                movesList.pop(j)
            else:
                j += 1
        i += 1
    if len(movesList) > 0:
        cellRand = random.choice(movesList)
    return cellRand


def getComputerMove(board, computerLetter) -> int:
    # Esta función implementa la estrategia de juego de la computadora.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # computerLetter: La marca que está usando la computadora.

    # Desarrolle el cuerpo de la función aquí...

    freeSide = []

    # 1. Verificar si la computadora puede ganar...
    # Filas
    # Tercera fila
    if (computerLetter == board[0] == board[1]) and isSpaceFree(board, 2):
        cell = 2
    elif (computerLetter == board[0] == board[2]) and isSpaceFree(board, 1):
        cell = 1
    elif (computerLetter == board[1] == board[2]) and isSpaceFree(board, 0):
        cell = 0
    # Segunda fila
    elif (computerLetter == board[3] == board[4]) and isSpaceFree(board, 5):
        cell = 5
    elif (computerLetter == board[3] == board[5]) and isSpaceFree(board, 4):
        cell = 4
    elif (computerLetter == board[4] == board[5]) and isSpaceFree(board, 3):
        cell = 3
    # Primera fila
    elif (computerLetter == board[6] == board[7]) and isSpaceFree(board, 8):
        cell = 8
    elif (computerLetter == board[6] == board[8]) and isSpaceFree(board, 7):
        cell = 7
    elif (computerLetter == board[7] == board[8]) and isSpaceFree(board, 6):
        cell = 6

    # Columnas
    # Primera columna
    elif (computerLetter == board[0] == board[3]) and isSpaceFree(board, 6):
        cell = 6
    elif (computerLetter == board[0] == board[6]) and isSpaceFree(board, 3):
        cell = 3
    elif (computerLetter == board[3] == board[6]) and isSpaceFree(board, 0):
        cell = 0
    # Segunda columna
    elif (computerLetter == board[1] == board[4]) and isSpaceFree(board, 7):
        cell = 7
    elif (computerLetter == board[1] == board[7]) and isSpaceFree(board, 4):
        cell = 4
    elif (computerLetter == board[4] == board[7]) and isSpaceFree(board, 1):
        cell = 1
    # Tercera columna
    elif (computerLetter == board[2] == board[5]) and isSpaceFree(board, 8):
        cell = 8
    elif (computerLetter == board[2] == board[8]) and isSpaceFree(board, 5):
        cell = 5
    elif (computerLetter == board[5] == board[8]) and isSpaceFree(board, 2):
        cell = 2
        
    # Diagonales
    # Diagonal principal
    elif (computerLetter == board[2] == board[4]) and isSpaceFree(board, 6):
        cell = 6
    elif (computerLetter == board[2] == board[6]) and isSpaceFree(board, 4):
        cell = 4
    elif (computerLetter == board[4] == board[6]) and isSpaceFree(board, 2):
        cell = 2
    # Diagonal secundaria
    elif (computerLetter == board[0] == board[4]) and isSpaceFree(board, 8):
        cell = 8
    elif (computerLetter == board[0] == board[8]) and isSpaceFree(board, 4):
        cell = 4
    elif (computerLetter == board[4] == board[8]) and isSpaceFree(board, 0):
        cell = 0


    # 2. Si no, verificar si el usuario puede ganar en la siguiente jugada, si si, bloquear esta jugada...

    # Validación inicial para evitar el encierro desde el inicio
    elif board.count(f" {symbol[0]} ") == 1 and board.count(computerLetter) == 0 \
          and  f" {symbol[0]} " in [board[0], board[2], board[6], board[8]]:
        cell = 4

    elif (f" {symbol[0]} " == board[0] == board[8] or \
          f" {symbol[0]} " == board[2] == board[6]) and \
            board[4] == computerLetter and \
            board.count(f" {symbol[0]} ") == 2 and \
            board.count(computerLetter) == 1:
        if isSpaceFree(board, 1):
            freeSide.append(1)
        if isSpaceFree(board, 3):
            freeSide.append(3)
        if isSpaceFree(board, 5):
            freeSide.append(5)
        if isSpaceFree(board, 7):
            freeSide.append(7)
        cell = random.choice(freeSide)
    

    # Filas
    # Primera fila
    elif (f" {symbol[0]} " == board[0] == board[1]) and isSpaceFree(board, 2):
        cell = 2
    elif (f" {symbol[0]} " == board[0] == board[2]) and isSpaceFree(board, 1):
        cell = 1
    elif (f" {symbol[0]} " == board[1] == board[2]) and isSpaceFree(board, 0):
        cell = 0
    # Segunda fila
    elif (f" {symbol[0]} " == board[3] == board[4]) and isSpaceFree(board, 5):
        cell = 5
    elif (f" {symbol[0]} " == board[3] == board[5]) and isSpaceFree(board, 4):
        cell = 4
    elif (f" {symbol[0]} " == board[4] == board[5]) and isSpaceFree(board, 3):
        cell = 3
    # Tercera fila
    elif (f" {symbol[0]} " == board[6] == board[7]) and isSpaceFree(board, 8):
        cell = 8
    elif (f" {symbol[0]} " == board[6] == board[8]) and isSpaceFree(board, 7):
        cell = 7
    elif (f" {symbol[0]} " == board[7] == board[8]) and isSpaceFree(board, 6):
        cell = 6

    # Columnas
    # Primera columna
    elif (f" {symbol[0]} " == board[0] == board[3]) and isSpaceFree(board, 6):
        cell = 6
    elif (f" {symbol[0]} " == board[0] == board[6]) and isSpaceFree(board, 3):
        cell = 3
    elif (f" {symbol[0]} " == board[3] == board[6]) and isSpaceFree(board, 0):
        cell = 0
    # Segunda columna
    elif (f" {symbol[0]} " == board[1] == board[4]) and isSpaceFree(board, 7):
        cell = 7
    elif (f" {symbol[0]} " == board[1] == board[7]) and isSpaceFree(board, 4):
        cell = 4
    elif (f" {symbol[0]} " == board[4] == board[7]) and isSpaceFree(board, 1):
        cell = 1
    # Tercera columna
    elif (f" {symbol[0]} " == board[2] == board[5]) and isSpaceFree(board, 8):
        cell = 8
    elif (f" {symbol[0]} " == board[2] == board[8]) and isSpaceFree(board, 5):
        cell = 5
    elif (f" {symbol[0]} " == board[5] == board[8]) and isSpaceFree(board, 2):
        cell = 2
        
    # Diagonales
    # Diagonal principal
    elif (f" {symbol[0]} " == board[2] == board[4]) and isSpaceFree(board, 6):
        cell = 6
    elif (f" {symbol[0]} " == board[2] == board[6]) and isSpaceFree(board, 4):
        cell = 4
    elif (f" {symbol[0]} " == board[4] == board[6]) and isSpaceFree(board, 2):
        cell = 2
    # Diagonal secundaria
    elif (f" {symbol[0]} " == board[0] == board[4]) and isSpaceFree(board, 8):
        cell = 8
    elif (f" {symbol[0]} " == board[0] == board[8]) and isSpaceFree(board, 4):
        cell = 4
    elif (f" {symbol[0]} " == board[4] == board[8]) and isSpaceFree(board, 0):
        cell = 0


    # 3. Si no, tratar de poner una marca en alguna de las esquinas, si alguna está vacía...
    # 4. Si no, tratar de marcar la casilla del centro, si esta está vacía...
    # 5. Si no, tratar de poner una marca en alguna de las casillas de los lados...
    else:
        cell = chooseRandomMoveFromList(board, [0, 2, 6, 8])
        if cell == -1:
            cell = 4
            if not isSpaceFree(board, cell):
                cell = chooseRandomMoveFromList(board, [1, 3, 5, 7])            
    return cell
    

def isBoardFull(board) -> bool:
    # Esta función verifica si el tablero está lleno.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función debe retorna el valor lógico True, si el tablero está lleno.
    # En caso contrario debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    
    # Filtro de robustez (caja negra)
    if not isinstance(board, list):
        raise TypeError("El tablero debe ser una lista")
        
    return board.count(' X ') + board.count(' O ') == 9
    