import pytest
from pages.page_carrito_eliminado import ProductosCarrito
from selenium import webdriver


class TestCarrito:
    def test_carrito_producto(self, driver:webdriver.Remote):
        productos_carrito = ProductosCarrito(driver)
        driver.get("https://pruebasautomation.mitiendanube.com/productos/guante-wilson/")
        driver.maximize_window()
        productos_carrito.btn_cookies()
        productos_carrito.btn_agregar_producto()
        productos_carrito.click_ir_a_carrito()
        productos_carrito.eliminar_producto_del_carrito()
        productos_carrito.visualizar_carrito()