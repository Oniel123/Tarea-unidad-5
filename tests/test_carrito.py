import pytest
from src.carrito import Carrito


def test_carrito_nuevo_tiene_total_cero():
    carrito = Carrito()
    assert carrito.total() == 0


def test_agregar_producto_actualiza_total():
    carrito = Carrito()
    carrito.agregar("Manzana", 10.0, 3)
    assert carrito.total() == pytest.approx(30.0)


    