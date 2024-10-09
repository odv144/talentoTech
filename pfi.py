import re
#-------------------------MENU--------------------------    
def menu():
    print("### Menú de Opciones ####")
    print("Menú de Gestión de Productos\n")
    print("1. Alta de productos nuevos")
    print("2. Consulta de datos de productos")
    print("3. Modificar la cantidad en stock de un producto")
    print("4. Dar de baja productos")
    print("5. Listado completo de los productos")
    print("6. Lista de productos con cantidad bajo minimo")
    print("7. Salir")
    
#-----------------------ALTA PRODUCTO-------------------    
def alta():
    pass

#---------------------CONSULTAR PRODUCTO----------------    
def consulta():
    pass

#--------------------MODIFICACION DE PRODUCTO------------    
def modificacion():
    #esta lista debe ser la general la modificacion debe ser ingresada luego de seleccionar
    #el item por cual se realiza la busqueda

    productos = [{"id":1,"nombre":"SSD de 240GB","precio":25600,"stock":5},{"id":3,"nombre":"SSD de 240GB","precio":25600,"stock":5},{"id":2,"nombre":"MOTHER A320H-M","precio":35600,"stock":2}]
    
    valor="SSD "
    response=buscarProducto(productos,valor)
    campo=0
    for producto in response:
        print(producto)
        for key,values in producto.items():
            print(f"{campo}:para {key}")
            campo+=1
        opc = int(input("Ingrese el número del campo a cambiar: "))
    else:
        print(f"El producto con nombre: {valor} no fue encontrado")
    #if producto['nombre']==search:

#-------------------BUSCAR PRODUCTO POR CAMPO-------------    
def buscarProducto(lista,valor):
    resultado = []
    for producto in lista:
        if(re.search(valor,producto['nombre'],re.IGNORECASE)):
            resultado.append(producto)
    return resultado
    
#-------------------ELIMINICION DE PRODUCTO---------------    
def baja():
    pass

#------------------LISTAR PRODUCTOS-----------------------    
def listarProductos():
    pass

#--------------------LISTAR STOCK MINIMO------------------    
def listarStockMinimo():
    pass
   
###############CURPO PRINCIPAL DEL PROGRAMA###################


fin = True
while fin:
    menu()
    opcion = int(input("Ingrese la opción deseada: "))
    match opcion:
        case 1:
            alta()
        case 2:
            consulta()
        case 3:
            modificacion()
        case 4:
            baja()
        case 5:
            listarProductos()
        case 6:
            listarStockMinimo()
        case 7:
            fin=False
        case _:
            print("Opción no válida. Por favor, vuelva a intentarlo.")
            
        