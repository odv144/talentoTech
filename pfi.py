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
    

#------------funcion para rellono de grilla-------------
def rellenoGrilla(cadena,anchoColumna):        
    return f"{cadena}{' ' * (anchoColumna - len(cadena))}"
        
#-----------------------ALTA PRODUCTO-------------------    
def alta(productos):
    id=len(productos)+1
    nombre=input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio unitario:"))
    stock = int(input("Ingrese la cantidad: "))
    minimo = int(input("Ingrese Stock mínimo: "))
    
    producto ={
    "id":id,
    "nombre":nombre,
    "precio":precio,
    "stock":stock,
    "minimo":minimo,
    "activo":True
    
        }
    productos.append(producto)

#---------------------CONSULTAR PRODUCTO----------------    
def consulta():
    pass

#--------------------MODIFICACION DE PRODUCTO------------    
def modificacion(productos):
    #esta lista debe ser la general la modificacion debe ser ingresada luego de seleccionar
    #el item por cual se realiza la busqueda
    valor=input("Valor para buscar el nombre: ")
    response=buscarProducto(productos,valor)
    print(producto)
    flag=True
    while flag:
        for key,values in enumerate(producto):
            print(f"{key}:para {values}")
      
        print(f"99 : para Salir")
        opc = int(input("Ingrese el número del campo a cambiar: "))
            
        match opc:
                case 0:
                    producto[0]=int(input("Ingrese el nuevo id: "))
                case 1:
                    producto[1]=input("Ingrese el nuevo nombre: ")
                case 2:
                    producto[2]=float(input("Ingrese el nuevo precio: "))
                case 3:
                    producto[3]=int(input("Ingrese el nuevo stock: "))
                case 4:
                    producto[4]=int(input("Ingrese el nuevo minimo: "))
                case 5:
                    producto[5]=input("Activar producto 'S' o 'N': ")
                    estado = producto[5].upper()=='S'
                    producto[5]=estado
                case 99:
                    flag=False
                case _:
                    print("Opción no válida")
                    
                    
    else:
        print(f"El producto con nombre: {valor} no fue encontrado")
    #if producto['nombre']==search:

#-------------------BUSCAR PRODUCTO POR CAMPO-------------    
def buscarProducto(lista,valor):
    resultado = []
    #Busca los productos que coinciden con el valor
    for producto in lista:
        if(re.search(valor,producto['nombre'],re.IGNORECASE)):
            resultado.append(producto)
    for indice,elemento in enumerate(resultado):
        print(f"{indice}-{elemento}")
    opc = int(input("Ingrese el indice del producto que desea modificar: "))
    if opc!="salir":
        return resultado[opc]
    else:
        return 0
    
#-------------------ELIMINICION DE PRODUCTO---------------    
def baja():
    pass

#------------------LISTAR PRODUCTOS-----------------------    
def listarProductos(productos):
    for producto in productos:
        print("-"*75)
        print((f"{producto['id']}\t"
              f"{rellenoGrilla(producto['nombre'],40)}\t"
              f"{rellenoGrilla(str(producto['precio']),10)}\t"
              f"{producto['stock']}\t"
              ))    
    print("-"*75)

#--------------------LISTAR STOCK MINIMO------------------    
def listarStockMinimo():
    pass
   
###############CURPO PRINCIPAL DEL PROGRAMA###################
productos = [{"id":1,"nombre":"SSD de 480GB","precio":52600,"stock":4,"minimo":1,"activo":False},{"id":3,"nombre":"SSD de 240GB","precio":25600,"stock":5},{"id":2,"nombre":"MOTHER A320H-M","precio":35600,"stock":2,"minimo":2,"activo":False}]

producto ={
    "id":1,
    "nombre":"Pantalones",
    "precio":1000,
    "stock":10,
    "minimo":2,
    "activo":True
    
}
productos.append(producto)

print(productos)
fin = True
while fin:
    menu()
    opcion = int(input("Ingrese la opción deseada: "))
    match opcion:
        case 1:
            alta(productos)
        case 2:
            consulta()
        case 3:
            modificacion(productos)
        case 4:
            baja()
        case 5:
            listarProductos(productos)
        case 6:
            listarStockMinimo()
        case 7:
            fin=False
        case _:
            print("Opción no válida. Por favor, vuelva a intentarlo.")
            
        