class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, nombre, precio, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad no puede ser 0 ni un valor negativo")
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }
        self.productos.append(producto)

    def total(self):
        return sum(
            producto["precio"] * producto["cantidad"]
            for producto in self.productos
        )
    