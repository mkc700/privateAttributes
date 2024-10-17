from classVenta import Venta

venta  = Venta()

productos = {
    "producto1": {"nombre": "manzana", "precio": 4, "cantidad": 17},
    "producto2": {"nombre": "uvas", "precio": 20, "cantidad": 2},
    "producto3": {"nombre": "melones", "precio": 17,"cantidad": 4}
}
venta.set_cliente('Martin')
venta.set_id_venta(450)
venta.set_productos(productos)
venta.set_fecha("15/11/20")
venta.set_total(productos)


venta.mostrar_detalle()

