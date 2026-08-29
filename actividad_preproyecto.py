import json

def carga_y_agrupacion(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        ventas = json.load(archivo)

    monto_por_vendedor={}
    cantidades_total_por_producto={}

    for venta in ventas:
        tienda = venta["tienda"]
        vendedor = venta["vendedor"]
        precio_unitario = venta["precio_unitario"]
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        monto= venta['cantidad'] * venta['precio_unitario']
        if monto > 700000:
            with open("alerta ventas.txt", "a",encoding="utf-8") as archivo_alerta:
                archivo_alerta.write(
                    f"\nVendedor: {vendedor}"
                    f"\nTienda: {tienda}"
                    f"\nProducto: {producto}"
                    f"\nMonto: {monto:,.2f}"
                )
        
        print(f"Producto: {venta['producto']}, Monto: {monto}")
        
        if vendedor in monto_por_vendedor:
            monto_por_vendedor[vendedor].append(monto)
        else:
            monto_por_vendedor[vendedor] = [monto]
        if producto in cantidades_total_por_producto:
            cantidades_total_por_producto[producto] += cantidad
        else:
            cantidades_total_por_producto[producto] = cantidad
    return monto_por_vendedor, cantidades_total_por_producto

def calculo_de_cada_vendedor(monto_por_vendedor):
    estadistica_vendedores = {}
    for vendedor, montos in monto_por_vendedor.items():
        estadistica_vendedores[vendedor]={
            "Total": sum(montos),
            "Promedio": sum(montos) / len(montos),
            "Maximo": max(montos),
            "Minimo": min(montos)
        }
    vendedor_del_mes = max(estadistica_vendedores, key=lambda x: estadistica_vendedores[x]["Total"])
    return estadistica_vendedores, vendedor_del_mes

def calculos_globales(monto_por_vendedor,cantidades_total_por_producto):
    producto_estrella=max(cantidades_total_por_producto, key=cantidades_total_por_producto.get)
    producto_menos_vendido=min(cantidades_total_por_producto, key=cantidades_total_por_producto.get)
    Total_general=sum(sum(montos) for montos in monto_por_vendedor.values())
    total_ventas_regs= sum(len(montos) for montos in monto_por_vendedor.values())
    promedio_general= Total_general / total_ventas_regs
    return producto_estrella, producto_menos_vendido,Total_general,promedio_general
    
monto_vendedor, cant_producto = carga_y_agrupacion("ventas.json")
stats_vendedores, vendedor_estrella = calculo_de_cada_vendedor(monto_vendedor)
Prod_Estrella, Prod_menor, Total_General, Prom_General = calculos_globales(monto_vendedor, cant_producto)
print("🌟Bienvenido, este es el reporte de ventas del mes🌟")
print("Estadisticas personales de cada vendedor 📅")

for vendedor, datos in stats_vendedores.items():
    print(f"\n🤓Estadísticas de {vendedor}:")
    print(f"   \n🧐vendio un total de: ${datos['Total']:,.2f}")
    print(f"   💰en promedio vendio: ${datos['Promedio']:,.2f}")
    print(f"   🤑su mayor venta fue de: ${datos['Maximo']:,.2f}")
    print(f"   📉su menor venta fue de: ${datos['Minimo']:,.2f}")

print("\n DESTACADOS Y MEJORES ESTADISTICAS GLOBALES")
print(f"    \n🤑El vendedor del mes fue: {vendedor_estrella}")
print(f"    🌟El producto estrella fue: {Prod_Estrella} con un total de {cant_producto[Prod_Estrella]} unidades")
print(f"    💸El total vendido fue de: ${Total_General:,.2f}")
print(f"    💹Promedio de ventas general: ${Prom_General:,.2f}")

ranking_lista = [(vendedor, sum(montos)) for vendedor, montos in monto_vendedor.items()]
ranking_lista.sort(key=lambda item: item[1],reverse=True)
podio=ranking_lista[:3]

print(f"\n🏆🥇 El mejor vendedor fue {podio[0][0]}")
print(f"🏆🥈 El segundo mejor vendedor fue {podio[1][0]}")
print(f"🏆🥉 El tercer mejor vendedor fue {podio[2][0]}")

with open("resumen ventas.txt","w",encoding="utf-8") as archivo_resumen:
    archivo_resumen.write( 
        f"\nTotal General Vendido {Total_General}"
        f"\nProducto estrella: {Prod_Estrella}"
        f"\nCantidad vendida: {cant_producto}"
        f"\nProducto menos vendido: {Prod_menor}"
        f"\n\nEl top 3 de nuestros vendedores fue: \n\nPrimer puesto {podio[0][0]}\nSegundo puesto {podio[1][0]}\nTercer puesto {podio[2][0]}"
    )
