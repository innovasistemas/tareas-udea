import functions.triqui as tr
import utils.colors as color
import utils.util as utl

boarOrigin = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
boarHelp = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']
board = boarOrigin.copy()
resp = "S" 
stat = ['', 0, 0, 0]

# 1. Mostrar mensaje de bienvenida
tr.printIntro("assets/files/intro.txt")

stat[0] = input("Nombre usuario: ")

while resp == "S":
    # 2. Crear el tablero
    utl.systemMessage("Ayuda. Ingrese valores en celdas vacías siguiendo el teclado numérico")
    tr.drawBoard(boarHelp)

    # 3. El usuario debe seleccionar la marca
    symbol = tr.inputPlayerLetter()

    # 4. Quién va primero el usuario o la computadora?
    # Indica quién tiene el turno para jugar, el usuario o la computadora.
    turn = tr.whoGoesFirst()
    utl.systemMessage(f"Sorteo\n{turn} inicia el juego [ Usuario " +
                       f"{stat[0]}: {symbol[0]} | Computadora: {symbol[1]} ]\n" + 
                       f"Resultados: Usuario: {stat[1]}, Computadora: " + 
                       f"{stat[2]}, Empates: {stat[3]}", "information")
    
    playing = True # El juego ha iniciado
    win = False

    while playing:
        if turn == 'Usuario': # 5. Turno del usuario

            # a. Mostrar tablero
            tr.drawBoard(board)

            # b. Pedir jugada al usuario
            move = tr.getPlayerMove(board)
            
            # c. Actualizar el tablero
            tr.makeMove(board, symbol[0], move - 1)
            
            tr.drawBoard(board)

            # d. Verificar si el usuario ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.
            if tr.isWinner(board, symbol[0]):
                utl.systemMessage(f"¡Felicitaciones, {stat[0]}! Has ganado la partida", "success")
                stat[1] += 1
                tr.symbol.clear()
                board = boarOrigin.copy()
                win = True
                playing = False

            # e. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno
            turn = 'Computadora'

        else: # 6. Turno de la computadora.

            # a. Computadora hace jugada.
            move = tr.getComputerMove(board, f" {symbol[1]} ")

            # b. Actualizar el tablero.
            tr.makeMove(board, symbol[1], move)

            # c. Verificar si la computadora ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.
            if tr.isWinner(board, symbol[1]):
                tr.drawBoard(board)
                utl.systemMessage(f"Lo sentimos, {stat[0]}, has perdido la partida", "warning")
                stat[2] += 1
                tr.symbol.clear()
                board = boarOrigin.copy()
                win = True
                playing = False

            # d. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.
            turn = 'Usuario'
        
        if tr.isBoardFull(board) and not win:
            tr.drawBoard(board)
            utl.systemMessage(f"{stat[0]}, la partida quedó empatada", "information")
            stat[3] += 1
            tr.symbol.clear()
            board = boarOrigin.copy()
            playing = False

    # 7. Preguntar si el usuario quiere jugar una vez mas
    #    Si no, finalizar el programa.
    print(color.YELLOW)
    resp = input("¿Desea continuar jugando? [S/?]: ").upper()
    print(color.WHITE)

utl.statistics(stat)
print("")
textExit = "| Juego finalizado. Revise las estadísticas en el log del sistema |"
print("=" * len(textExit))
print(textExit)
print("=" * len(textExit))
print("")
