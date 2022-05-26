def AutoPartes(ventas: list):
    # Inicializar diccionario
    venta = dict()
    # Ciclo para agregar un nuevo evento
    for idProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas:
        # Fuerza la entrada
        if venta.get(idProducto) is None:
            # Creacion de un nuevo evento
            venta[idProducto] = []
            # Registro de una nueva lista de tuplas en el dict agenda
        venta[idProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta))
    return venta

def consultaRegistro(ventas, idProducto):
    if idProducto in ventas.keys():
        for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print(
                f"Producto consultado : {idProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}"
            )
            
    else:
        print("No hay registro de venta de ese producto")
