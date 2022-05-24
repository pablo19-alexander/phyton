#### listas paralelas ####

# nombre = ['joel', 'mateo', 'ricardo', 'luis', 'marcela']
# edad = [35,18,24,32,19]

# for i in range(5):
#     print(f'{nombre[i]} tiene {edad[i]} años de edad')

#otro caso 

# nombre = list()
# edad = list()
# for i in range(5):
#     nombre = input('digite el nombre')
#     edad = input('digite la edad')
#     nombre.append(nombre)
#     edad.append(edad)

# print(nombre)
# print(edad)

#### listas compuestas #####

# posicion = [
#     [1,2,3,4],
#     [5,6,7,8]
#     ]

# for i in posicion:
#     for j in i:
#         print(j)

# posicion = [
#     [1,2,[1,2,3]3,4],
#     [5,6,[4,5,6]7,8]
#     ]

# suma = 0
# for i in posicion:
#    for j in i:
#         if type(i) = list:
#             valor = sum(j)
#             suma += valor
# print(suma)

# posicion = [
#     [1,2,[1,2,3],3,4],
#     [5,6,[4,5,6],7,8]
#     ]

# suma = 0
# for i in posicion:
#    for j in i:
#         if type(j) == list:
#             j.append(2)
# print(suma)


# def conversion(x:list):
#     diccionario = dict(x)
#     return diccionario

# print(conversion([1,2,3,4,5]))

def conversion(x:list):
    dicc2 = dict(zip(["carro", "motor", "avion", "barco"],[1,2,3,4]))
    return dicc2

lista = [[1,2,3,4],[5,6,7,8]]
print(conversion(lista))