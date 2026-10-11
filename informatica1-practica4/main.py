import functions.triqui as tr
import utils.colors as color
import utils.validations as valid

# 1. Mostrar mensaje de bienvenida
tr.printIntro("assets/files/intro.txt")
# board_fill = [' X ', ' X ', ' O ', ' O ', ' X ', ' O ', ' O ', ' X ', ' O ']
board = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
board_help = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']

valid.message_system("Ayuda. Ingrese valores en celdas vacías siguiendo el teclado numérico")
tr.drawBoard(board_help)

resp = "S" 
while resp == "S":

    # 2. Crear el tablero


    # 3. El usuario debe seleccionar la marca
    symbol = tr.inputPlayerLetter()

    # 4. Quién va primero el usuario o la computadora?
    # Indica quién tiene el turno para jugar, el usuario o la computadora.
    turn = tr.whoGoesFirst()
    valid.message_system(turn + " inicia el juego [Usuario: " + symbol[0] + 
                         " | Computador: " + symbol[1] + "] ", "information")
    

    playing = True # El juego ha iniciado

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

            # e. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno

            turn = 'Computadora'

        else: # 6. Turno de la computadora.

            # a. Computadora hace jugada.
            # b. Actualizar el tablero.

            # c. Verificar si la computadora ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.

            # d. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.

            turn = 'Usuario'
        
        playing = False

    # 7. Preguntar si el usuario quiere jugar una vez mas
    #    Si no, finalizar el programa.
    print(color.YELLOW)
    resp = input("¿Desea continuar jugando? [S/?]: ").upper()
    print(color.WHITE)

print("")
print("=" * 20)
print("| Juego finalizado |")
print("=" * 20)
print("")
