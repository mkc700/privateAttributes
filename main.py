from classVenta import Venta

venta  = Venta()


productos = {
    "producto1": {"nombre": "Laptop", "precio": 1500},
    "producto2": {"nombre": "Smartphone", "precio": 800},
    "producto3": {"nombre": "Tablet", "precio": 300}
}


venta.set_cliente('Ricardo')
venta.set_id_venta(1)

venta.set_productos(productos)

venta.set_fecha("07/28/13")
venta.set_total(400)

id_ventaa = venta.get_id_venta()
total = venta.get_total()

'''
print(venta.get_id_venta())
print("el id de la venta: "+str(id_ventaa)+"\n el nombre del cliente: "+venta.get_cliente())
print("\n productos"+venta.get_productos()+"\n total: "+str(total)+"\n fecha: "+venta.set_fecha())
'''

print(venta.get_productos())