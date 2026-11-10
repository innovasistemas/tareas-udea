import getpass
import src.config.database as db
import src.utils.colors_symbols as col_sym

user_auth = {}

def authentication() -> None:
    '''
    Función para autenticar usuarios registrados
    Pide los datos al usuario
    '''  

    global user_auth

    user_id = input("Documento: ")
    user_password = getpass.getpass("Contraseña: ")
    
    validate_credentials(user_id, user_password)


def validate_credentials(user = "", password = "") -> None:
    '''
    Valida que las credenciales ingresadas por el usuario sean válidas
    Argumentos:
    user: documento del usuario
    password: contraseña del usuario
    '''
    
    global user_auth

    if user in db.users_data and password == db.users_data[user]["clave"]:
        user_auth = {"id": user} | db.users_data[user]
    else:
        user_auth = {"message": 
                        {"error": "Usuario/contraseña no válidos", 
                            "nombre": "Invitado", "rol": "Visitante"
                        }
                    }
        
            
def connected_user() -> None:
    '''
    Función para mostrar el usuario conectado
    '''

    if 'message' not in user_auth:
        print(f"Usuario conectado: {col_sym.BLUE}{user_auth['nombre']} " +
            f"[{user_auth['rol']}]{col_sym.WHITE}")
    else:
        print(f"Usuario conectado: {col_sym.BLUE}{user_auth['message']['nombre']} " +
            f"[{user_auth['message']['rol']}]{col_sym.WHITE}")