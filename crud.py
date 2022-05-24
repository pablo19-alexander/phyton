#create - crear
#read - leer
#update -actualizar
# delete - eliminar

#id
#nombre
#edad

bd = dict()

def crear(datos: list):
    id = datos[0]
    bd[id] = {
        'nomnbre': datos[1],
        'edad': datos[2]
    }
    return bd[id]

def leer(id: int):
    return bd[id]

def actualizar(datos: list):
    if datos[0] in bd.keys():
        bd[datos[0]] = {
            'nomnbre': datos[1],
            'edad': datos[2]
        }
    else:
        return 'registro no encotrado'
    
def eliminar(id):
    datos = bd[id]
    del bd[id]
    return datos

datos = [1234567890,'pablo salazar', 35]
crear(crear)