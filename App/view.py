import sys
import App.logic as logic
from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_entry as me



def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return logic.new_logic()

def imprimir_pedido(pedido):                                  
    print(pedido["Order_ID"], pedido["Product"], pedido["Country"],
          pedido["Channel"], pedido["Order_Date"], pedido["Boxes_Shipped"],
          pedido["Price_per_Box"], pedido["Amount"])

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    archivo = input("Nombre del archivo: ")
    ruta = "Data/" + archivo
    resultado = logic.load_data(control, ruta)
    return resultado


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass

def imprimir_pedido_req_3(pedido):
    print(pedido["Order_ID"], pedido["Product"], pedido["Country"], pedido["Order_Date"],
          pedido["Marketing_Spend"], pedido["Boxes_Shipped"], pedido["Amount"], pedido["Aporte_Comercial"])


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    fecha = input("Ingrese una fecha: ")
    valor_max = float(input("Ingrese valor max: "))
    valor_min = float(input("Ingrese valor min: "))
    resultado = logic.req_3(control, fecha, valor_min, valor_max)
    print("Tiempo de ejecución: ", resultado["tiempo"], "ms")
    print("Total de pedidos: ", resultado["total_pedidos"])
    print("Monto total recaudado: ", resultado["total_amount"])
    print("Total inversión en mercadeo: ", resultado["total_marketing"])
    print("Aporte comercial total: ", resultado["total_aporte"])
    print("Pedidos:")
    for i in range(al.size(resultado["primeros"])):
        imprimir_pedido_req_3(al.get_element(resultado["primeros"], i))
    if al.size(resultado["ultimos"]) > 0:
        for i in range(al.size(resultado["ultimos"])):
            imprimir_pedido_req_3(al.get_element(resultado["ultimos"], i))
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print("Tiempo de carga: ", data["tiempo"], "ms")
            print("Total de pedidos: ", data["total"])
            print("Fecha más antigua: ", data["fecha_min"])
            print("Fecha más reciente: ", data["fecha_max"])
            print("Pedido con Amount mínimo:")
            imprimir_pedido(data["pedido_min"])
            print("Pedido con Amount máximo:")
            imprimir_pedido(data["pedido_max"])
            print("Primeros 5 pedidos:")
            for i in range(al.size(data["primeros_5"])):
                imprimir_pedido(al.get_element(data["primeros_5"], i))
            print("Ultimos 5 pedidos:")
            for i in range(al.size(data["ultimos_5"])):
                imprimir_pedido(al.get_element(data["ultimos_5"], i))
            mapa = control["pedidos_por_canal"]
            canales = lp.key_set(mapa)
            print("Pedidos por canal: ")
            for i in range(al.size(canales)):
                canal = al.get_element(canales, i)
                numero = lp.get(mapa,canal)
                print("En el canal", canal, "hay", numero)
                


            
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
