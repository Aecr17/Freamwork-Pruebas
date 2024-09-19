import pytest
from pages.compraTN import CompraTiendaNube
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_method(self):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en modo headless
    chrome_options.add_argument("--no-sandbox")  # Necesario para entornos CI como GitHub Actions
    chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas de memoria compartida
    chrome_options.add_argument("--disable-gpu")  # Deshabilita la GPU (opcional en algunos casos)
    chrome_options.add_argument("--window-size=1920x1080")  # Configura el tamaño de ventana
    self.driver = webdriver.Chrome(options=chrome_options)

class TestIngresarDatos:
    def test_compra_completa(self, driver:webdriver.Remote):
        compra_tienda_nube = CompraTiendaNube(driver)
        driver.get("https://pruebasautomation.mitiendanube.com/productos/guante-wilson/")
        driver.maximize_window()
        compra_tienda_nube.btn_cookies()
        compra_tienda_nube.btn_agregar_producto()
        compra_tienda_nube.click_ir_a_carrito()
        compra_tienda_nube.click_btn_compra()
        compra_tienda_nube.primeros_datos("Pruebas@gmail.com", "1174")
        compra_tienda_nube.datos_para_la_compra("Andres","Cardzoa","prueba","17","P","Suggar cane")
        compra_tienda_nube.btn_ir_al_pago()
        compra_tienda_nube.ingresa_iframe()
        compra_tienda_nube.btn_metodo_pago()
        compra_tienda_nube.documento_compra("12345678")
        compra_tienda_nube.switch_to_default_content()
        compra_tienda_nube.finalizar_compra()
        compra_tienda_nube.compra_finalizada()
        