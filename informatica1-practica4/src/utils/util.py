from datetime import date, datetime
import src.utils.colors_symbols as col_sym

def systemMessage(message = "", type = "information") -> None:
    match type:
        case "information":
            col = col_sym.BLUE
            title = f"{col_sym.SYMBOL_INFORMATION} Información del Sistema"
        case "success":
            col = col_sym.GREEN
            title = f"{col_sym.SYMBOL_SUCCESS} Felicitaciones"
        case "error":
            title = f"{col_sym.SYMBOL_ERROR} ¡Error!"
            col = col_sym.RED
        case "warning":
            title = f"{col_sym.SYMBOL_WARNING} Advertencia"
            col = col_sym.YELLOW
        case _:
            col = col_sym.BLUE
            title = f"{col_sym.SYMBOL_INFORMATION} Información del Sistema"
    print(col)
    print("#" * len(message))
    print(f"{title} \n{message}")
    print("#" * len(message))
    print(col_sym.WHITE, end="")
    input(f"Presione Enter {col_sym.ENTER} para continuar...")
    print("")


def statistics(stat) -> None:
    textEstat = ""
    textEstat += "-" * 20 + "Triqui" + "-" * 20 + "\n"

    now = datetime.now()
    textEstat += now.strftime("%A, %B %d, %Y - %H:%M:%S")
    
    textEstat += "\n\nNombre del jugador: " + stat[0] 

    textEstat += "\n\nJuegos ganados por el usuario: " + str(stat[1])
    textEstat += "\nJuegos ganados por el computador: " + str(stat[2]) 
    textEstat += "\nJuegos empatados: " + str(stat[3]) 
    textEstat += "\n" 
    textEstat += "-" * 46
    textEstat += "\n\n" 

    file = open("assets/files/statistics.log", "a", encoding="utf-8")
    file.write(textEstat)
    file.close()


def validateInput(value) -> bool:
    if len(value) == 1:
        i = 0
        sw = True
        while sw and i < len(value):
            if value[i] not in "123456789":
                sw = False
            else:
                i += 1
    else:
        sw = False
    return sw
