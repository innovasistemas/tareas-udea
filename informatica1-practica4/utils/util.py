from datetime import date, datetime
import utils.colors as color

def system_message(message = "", type = "information") -> None:
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
    text_est = ""
    text_est += "-" * 20 + "Triqui" + "-" * 20 + "\n"

    now = datetime.now()
    text_est += now.strftime("%A, %B %d, %Y - %H:%M:%S")
    
    text_est += "\n\nNombre del jugador: " + stat[0] 

    text_est += "\n\nJuegos ganados por el usuario: " + str(stat[1])
    text_est += "\nJuegos ganados por el computador: " + str(stat[2]) 
    text_est += "\nJuegos empatados: " + str(stat[3]) 
    text_est += "\n" 
    text_est += "-" * 46
    text_est += "\n\n" 

    file = open("assets/files/statistics.log", "a", encoding="utf-8")
    file.write(text_est)
    file.close()