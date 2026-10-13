import time
import csv
from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as lp

csv.field_size_limit(2147483647) 

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
    "pedidos": al.new_list(),
    "pedidos_por_canal": lp.new_map(3,0.5) 
    }
    return catalog


# Funciones para la carga de datos

def criterio_amount_desc(pedido_1, pedido_2):
    if pedido_1["Amount"] > pedido_2["Amount"]:
        return True
    if pedido_1["Amount"] == pedido_2["Amount"]:
        return pedido_1["Order_ID"] < pedido_2["Order_ID"]
    return False


def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    tiempo_inicial = get_time()
    archivo = open(filename, encoding="utf-8-sig")
    lector = csv.DictReader(archivo)
    
    fecha_min = "9999-12-31"
    fecha_max = "0"
    
    pedido_min = None
    pedido_max = None
    
    for fila in lector:
        pedido = {
            "Order_ID":        fila["Order_ID"],
            "Product":         fila["Product"],
            "Country":         fila["Country"],
            "Channel":         fila["Channel"],
            "Order_Date":      fila["Order_Date"],
            "Discount_Pct":    float(fila["Discount_Pct"]),
            "Price_per_Box":   float(fila["Price_per_Box"]),
            "Marketing_Spend": float(fila["Marketing_Spend"]),
            "Boxes_Shipped":   int(fila["Boxes_Shipped"]),
            "Amount":          float(fila["Amount"]),
        }
        al.add_last(catalog["pedidos"],pedido)
        canal = pedido["Channel"]
        mapa_canales = catalog["pedidos_por_canal"]
        if lp.contains(mapa_canales, canal):
            conteo = lp.get(mapa_canales, canal)
            conteo += 1
            lp.put(mapa_canales, canal, conteo)
        else:
            lp.put(mapa_canales, canal, 1)
        
        fecha = pedido["Order_Date"]
        if fecha < fecha_min:
            fecha_min = fecha
        if fecha > fecha_max:
            fecha_max = fecha
        
        if pedido_min is None or pedido["Amount"] < pedido_min["Amount"]:
            pedido_min = pedido
        if pedido_max is None or pedido["Amount"] > pedido_max["Amount"]:
            pedido_max = pedido
    
    archivo.close()
    total = al.size(catalog["pedidos"])
    
    al.merge_sort(catalog["pedidos"], criterio_amount_desc)
    primeros_5 = al.sub_list(catalog["pedidos"], 0, 5)
    ultimos_5 = al.sub_list(catalog["pedidos"], total - 5, 5)
    
    tiempo_final = get_time()
    diferencia_tiempo = delta_time(tiempo_inicial, tiempo_final)

    return {
        "tiempo": diferencia_tiempo,
        "total": total,
        "fecha_min": fecha_min,
        "fecha_max": fecha_max,
        "pedido_min": pedido_min,
        "pedido_max": pedido_max,
        "primeros_5": primeros_5,
        "ultimos_5": ultimos_5,
    }

    
    

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
