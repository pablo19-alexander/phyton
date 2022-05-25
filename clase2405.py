from asyncore import read


ruta = './archivo.txt'
# file = open(ruta)
# file = open(ruta, 'r') #leer
# file = open(ruta, 'w') #escritura
# file = open(ruta, 'a') #añadir
# file = open(ruta, 'b') #modo binario para maquinas


#METODO read()
# print(file.read())

######METODO readline()
# print(file.readline())# imprime la primera linea
# print(file.readline())# imprime la segunda linea

# para buscar un carecter o palabra
# if 'm' in file.readline():
#     print(True)
# print(file.readline())

#imprime las lineas
# lineas = file.readlines()
# print(lineas[2])

# #### o tambien se puede, busca caracter o palabra 
# for i in lineas:
#     if 'a' in i:
#         print('si')
#     else:
#         print('no')


# with open(ruta, 'r') as file:
#     linea = file.readline()
#     while linea != ' ':
#         print(linea, end='')
#         linea = file.readline()

