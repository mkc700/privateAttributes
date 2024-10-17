
class Venta:
# el __ hace los atributos privados
    __id_venta = None
    __fecha = None
    __cliente = None
    __productos = {}  # Lista de productos vendidos
    __total = None


    # Setters para modificar los atributos privados

    def set_id_venta(self, id_venta):

        self.__id_venta = id_venta


    def set_fecha(self, fecha):

        self.__fecha = fecha


    def set_cliente(self, cliente):

        self.__cliente = cliente


    def set_productos(self, productos):

      self.__productos = productos


    def set_total(self,productos):
        # accedo al producto y despues uso el get para tomar las propiedades
        precio_prod1 = productos["producto1"].get("precio")
        cantidad_prod1 = productos["producto1"].get("cantidad")

        precio_prod2 = productos["producto2"].get("precio")
        cantidad_prod2 = productos["producto2"].get("cantidad")

        precio_prod3 = productos["producto3"].get("precio")
        cantidad_prod3 = productos["producto3"].get("cantidad")

        # definir los valores de diccionarios en variables y multiplicarlos despues
        __nomprod1 = precio_prod1 * cantidad_prod1
        __nomprod2 = precio_prod2 * cantidad_prod2
        __nomprod3 = precio_prod3 * cantidad_prod3

        total = __nomprod1 + __nomprod2 + __nomprod3

        self.__total = total


    # Método para mostrar los detalles de la venta

    def mostrar_detalle(self):
        # metodo para mostrar de manera mas adecuada los productos

        print(f"ID Venta: {self.__id_venta}")

        print(f"Fecha: {self.__fecha}")

        print(f"Cliente: {self.__cliente}")

        #print(f"Productos: {self.__productos}")
        print("____________________________________________________________")
        print("Nombre del producto:", self.__productos["producto1"].get("nombre"))
        print("precio:", self.__productos["producto1"].get("precio"))
        print("Cantidad:", self.__productos["producto1"].get("cantidad"))
        print("____________________________________________________________")
        print("Nombre del producto:", self.__productos["producto2"].get("nombre"))
        print("precio:", self.__productos["producto2"].get("precio"))
        print("Cantidad:", self.__productos["producto3"].get("cantidad"))
        print("____________________________________________________________")
        print("Nombre del producto:", self.__productos["producto3"].get("nombre"))
        print("precio:", self.__productos["producto3"].get("precio"))
        print("Cantidad:", self.__productos["producto3"].get("cantidad"))

        print(f"\n Total: ${self.__total:.2f}")

        # Getters para acceder a los atributos privados

    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):

        return self.__total
