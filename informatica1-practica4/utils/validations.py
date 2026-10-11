import utils.colors as color

def message_system(message = "", type = "information") -> None:
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
    print(color.WHITE)
    input("Presione Enter \u23CE para continuar...")
    print()