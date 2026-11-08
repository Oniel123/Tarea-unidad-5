class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, nombre, precio, cantidad):
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }
        self.productos.append(producto)

    def total(self):
        total = 0
        for producto in self.productos:
            total += producto["precio"] * producto["cantidad"]
        return total