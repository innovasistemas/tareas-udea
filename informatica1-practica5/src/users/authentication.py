import src.config.load_data as ld_data

user_id = ""
user_password = ""

def data_authentication() -> str:
    '''
    Función para autenticar usuarios registrados
    Pide los datos al usuario
    '''

    global user_id, user_password
    user_id = input("Documento: ")
    user_password = input("Contraseña: ")
    
    def validate_credentials(user, password) -> str:
        '''
        Valida que las credenciales ingresadas por el usuario sean válidas
        Argumentos:
        user: documento del usuario
        password: contraseña del usuario
        '''

        if user in ld_data.users_data and password in ld_data.users_data[user]["clave"]:
            return ld_data.users_data[user]["rol"]
        else:
            return "Usuario/contraseña no válidos"
    print(ld_data.stations_data)    
    return validate_credentials(user_id, user_password)