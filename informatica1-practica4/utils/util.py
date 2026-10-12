from datetime import date, datetime
import utils.colors as color

def systemMessage(message = "", type = "information") -> None:
    match type:
        case "information":
            col = color.BLUE
            title = "\u2139 Información del Sistema"
        case "success":
            col = color.GREEN
            title = "\u2714 Felicitaciones"
        case "error":
            title = "\u2716 ¡Error!"
            col = color.RED
        case "warning":
            title = "\u26A0 Advertencia"
            col = color.YELLOW
        case _:
            col = color.BLUE
            title = "\u2139 Información del Sistema"
    print(col)
    print("#" * len(message))
    print(f"{title} \n{message}")
    print("#" * len(message))
    print(color.WHITE, end="")
    input("Presione Enter \u23CE para continuar...")
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
