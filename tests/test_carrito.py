import pytest
from src.carrito import Carrito


def test_carrito_nuevo_tiene_total_cero():
    carrito = Carrito()
    assert carrito.total() == 0