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
    "pedidos_por_canal": lp.new_map(3, 0.5),
    "pedidos_por_fecha": lp.new_map(730, 0.5),
    "promedio_producto_pais": lp.new_map(60, 0.5),
    "pedidos_por_pais": lp.new_map(5,0.5)
    }
    return catalog


# Funciones para la carga de datos

def criterio_amount_desc(pedido_1, pedido_2):
    if pedido_1["Amount"] > pedido_2["Amount"]:
        return True
    if pedido_1["Amount"] == pedido_2["Amount"]:
        return pedido_1["Order_ID"] < pedido_2["Order_ID"]
    return False

def criterio_req_3(pedido_1, pedido_2):
    if pedido_1["Amount"] > pedido_2["Amount"]:
        return True
    if pedido_1["Amount"] == pedido_2["Amount"]:
        if pedido_1["Aporte_Comercial"] > pedido_2["Aporte_Comercial"]:
            return True
        if pedido_1["Aporte_Comercial"] == pedido_2["Aporte_Comercial"]:
            return pedido_1["Order_ID"] < pedido_2["Order_ID"]
    return False

def criterio_req_4(pedido_1, pedido_2):
    if pedido_1["Amount"] > pedido_2["Amount"]:
        return True
    if pedido_1["Amount"] == pedido_2["Amount"]:
        if pedido_1["Marketing_Spend"] < pedido_2["Marketing_Spend"]:
            return True
        if pedido_1["Marketing_Spend"] == pedido_2["Marketing_Spend"]:
            return pedido_1["Order_ID"] < pedido_2["Order_ID"]
    return False

def criterio_req_5(registro_1, registro_2):
    if registro_1["recaudo"] > registro_2["recaudo"]:
        return True
    if registro_1["recaudo"] == registro_2["recaudo"]:
        if registro_1["cajas"] > registro_2["cajas"]:
            return True
        if registro_1["cajas"] == registro_2["cajas"]:
            return registro_1["Product"] < registro_2["Product"]
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
        
        fecha = pedido["Order_Date"]
        mapa_fecha = catalog["pedidos_por_fecha"]
        if lp.contains(mapa_fecha, fecha):
            lista = lp.get(mapa_fecha, fecha)
            al.add_last(lista, pedido)
        else:
            lista = al.new_list()
            al.add_last(lista, pedido)
            lp.put(mapa_fecha, fecha, lista)
        
        producto = pedido["Product"]
        pais = pedido["Country"]
        llave = (producto, pais)
        mapa_producto_pais = catalog["promedio_producto_pais"]
        if lp.contains(mapa_producto_pais, llave):
            lista = lp.get(mapa_producto_pais, llave)
            al.add_last(lista, pedido)
        else:
            lista= al.new_list()
            al.add_last(lista, pedido)
            lp.put(mapa_producto_pais, llave, lista)
        
        mapa_pedidos_pais = catalog["pedidos_por_pais"]
        if lp.contains(mapa_pedidos_pais, pais):
            lista = lp.get(mapa_pedidos_pais, pais)
            al.add_last(lista, pedido)
        
        else:
            lista = al.new_list()
            al.add_last(lista, pedido)
            lp.put(mapa_pedidos_pais, pais, lista)
        
    
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


def req_3(catalog, fecha_pedido, amount_min, amount_max):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    tiempo_inicial = get_time()
    mapa_fecha = catalog["pedidos_por_fecha"]
    pedidos_fecha = lp.get(mapa_fecha, fecha_pedido)
    lista_filtrada = al.new_list()
    total_amount = 0
    total_marketing = 0
    total_aporte = 0
    
    if pedidos_fecha != None:
        for i in range(al.size(pedidos_fecha)):
            pedido = al.get_element(pedidos_fecha,i)
            if pedido["Amount"] >= amount_min and pedido["Amount"] <= amount_max:
                al.add_last(lista_filtrada, pedido)
                total_amount += pedido["Amount"]
                total_marketing += pedido["Marketing_Spend"]
                aporte = pedido["Amount"] - pedido["Marketing_Spend"]
                pedido["Aporte_Comercial"] = aporte
                total_aporte += aporte
                
        al.merge_sort(lista_filtrada, criterio_req_3)
    if al.size(lista_filtrada) > 20:
        primeros = al.sub_list(lista_filtrada, 0, 10)
        ultimos = al.sub_list(lista_filtrada, al.size(lista_filtrada)-10, 10)
    else:
        primeros = lista_filtrada
        ultimos = al.new_list()

    tiempo_final = get_time()
    diferencia_tiempo = delta_time(tiempo_inicial, tiempo_final)
    
    return {
        "tiempo":          diferencia_tiempo,
        "total_pedidos":   al.size(lista_filtrada),
        "total_amount":    total_amount,
        "total_marketing": total_marketing,
        "total_aporte":    total_aporte,
        "primeros":        primeros,
        "ultimos":         ultimos,
    }

        
    
        
    
    


def req_4(catalog, producto, pais):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    tiempo_inicial = get_time()
    llave = (producto, pais)
    mapa_producto_pais = catalog["promedio_producto_pais"]
    pedidos_llave = lp.get(mapa_producto_pais, llave)
    suma_precio = 0
    suma_descuento = 0
    suma_marketing = 0
    suma_cajas = 0
    lista2 = al.new_list()
    n = 0
    if pedidos_llave != None:
        n = al.size(pedidos_llave)
        for i in range(al.size(pedidos_llave)):
            pedido = al.get_element(pedidos_llave, i)
            suma_precio += pedido["Price_per_Box"]
            suma_cajas += pedido["Boxes_Shipped"]
            suma_descuento += pedido["Discount_Pct"]
            suma_marketing += pedido["Marketing_Spend"]
        al.merge_sort(pedidos_llave, criterio_req_4)
        if al.size(pedidos_llave) >= 2:
            lista2 = al.sub_list(pedidos_llave, 0, 2)
        else:
            lista2 = pedidos_llave
    
    if n > 0:
    
        promedio_precio = suma_precio/n
        promedio_descuento = suma_descuento/n
        promedio_marketing = suma_marketing/n
        promedio_cajas = suma_cajas/n
    
    else:
        promedio_precio = suma_precio
        promedio_descuento = suma_descuento
        promedio_marketing = suma_marketing
        promedio_cajas = suma_cajas
    
    tiempo_final = get_time()
    diferencia_tiempo = delta_time(tiempo_inicial, tiempo_final)

    
    return {
        "tiempo":          diferencia_tiempo,
        "total_pedidos":   n,
        "promedio_precio": promedio_precio,
        "promedio_marketing": promedio_marketing,
        "promedio_descuento": promedio_descuento,
        "promedio_cajas": promedio_cajas,
        "lista2": lista2
    }




def req_5(catalog, n_productos, pais, fecha_inicial, fecha_final):
    
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    tiempo_inicial = get_time()
    
    mapa_pedidos_pais = catalog["pedidos_por_pais"]
    pedidos_pais = lp.get(mapa_pedidos_pais, pais)
    total_pedidos = 0
    total_recaudo = 0
    tabla_productos = lp.new_map(12,0.5)
    top_n = al.new_list()
    
    if pedidos_pais != None:
        for i in range(al.size(pedidos_pais)):
            pedido = al.get_element(pedidos_pais, i)
            if pedido["Order_Date"] >= fecha_inicial and pedido["Order_Date"] <= fecha_final:
                total_pedidos += 1
                total_recaudo += pedido["Amount"]
                producto = pedido["Product"]
                if lp.contains(tabla_productos, producto):
                    registro = lp.get(tabla_productos, producto)
                    registro["pedidos"] += 1
                    registro["cajas"] += pedido["Boxes_Shipped"]
                    registro["recaudo"] += pedido["Amount"]
                    registro["suma_precio"] += pedido["Price_per_Box"]
                    registro["suma_descuento"] += pedido["Discount_Pct"]
                    registro["marketing"] += pedido["Marketing_Spend"]
                
                else:
                    registro = {
                        "Product": producto,
                        "pedidos": 1,
                        "cajas": pedido["Boxes_Shipped"],
                        "recaudo": pedido["Amount"],
                        "suma_precio": pedido["Price_per_Box"],
                        "suma_descuento": pedido["Discount_Pct"],
                        "marketing": pedido["Marketing_Spend"]
                    }
                    lp.put(tabla_productos, producto, registro)
    
    lista_productos = lp.value_set(tabla_productos)
                    
    al.merge_sort(lista_productos, criterio_req_5)
    
    if al.size(lista_productos) >= n_productos:
        top_n = al.sub_list(lista_productos, 0, n_productos)
    else:
        top_n = lista_productos
        
    for i in range(al.size(top_n)):
        registro = al.get_element(top_n, i)
        registro["promedio_precio"] = registro["suma_precio"] / registro["pedidos"]
        registro["promedio_descuento"] = registro["suma_descuento"] / registro["pedidos"]
            
    tiempo_final = get_time()
    diferencia_tiempo = delta_time(tiempo_inicial, tiempo_final)

    return {
        "tiempo":            diferencia_tiempo,
        "total_pedidos":     total_pedidos,
        "total_productos":   al.size(lista_productos),
        "total_recaudo":     total_recaudo,
        "top_n":             top_n,
    }
    


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
