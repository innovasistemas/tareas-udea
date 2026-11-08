users_data = {}
stations_data = {}

def load_data_csv():
    '''
    Función para cargar los archivos csv en memoria
    '''

    global users_data, stations_data
    
    aux_data = []
    file = open("assets/data_base/usuarios.csv", "r", encoding="utf-8")
    l = 0
    for line in file:
        if l != 0:
            aux_data = line.split(",")
            # Quitar el \n del final de la línea en el archivo csv
            aux_data[3] = aux_data[3][:len(aux_data[3]) - 1]
            users_data.update({
                aux_data[0]: 
                    {"nombre": aux_data[1], "clave": aux_data[2], "rol": aux_data[3]}
            })
        aux_data.clear()
        l += 1
    file.close()

    file = open("assets/data_base/estaciones.csv", "r")
    l = 0
    for line in file:
        if l != 0:
            aux_data = line.split(",")
            stations_data.update({
                aux_data[0]: 
                    {"nombre": aux_data[1]}
            })
        aux_data.clear()
        l += 1
    file.close()

load_data_csv()
