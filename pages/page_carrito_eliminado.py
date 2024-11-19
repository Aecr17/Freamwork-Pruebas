from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

class ProductosCarrito:
    """
    Clase que contiene los elementos para ingresar al carrito y eleminar el producto
    """
    def __init__(self, driver: webdriver.Remote, wait_time=10):
        self.driver = driver
        self.wait_time = wait_time


    def esperar_por_los_elementos(self, locator):
        try:
            wait = WebDriverWait(self.driver, self.wait_time)
            element = wait.until(EC.presence_of_element_located(locator))
            element = wait.until(EC.visibility_of(element))
            element = wait.until(EC.element_to_be_clickable(locator))
            return element
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error al encontrar el elemento {locator}: {e}")
            return None


    @property 
    def __aceptar_cookies(self):
        return self.esperar_por_los_elementos((By.XPATH, "//a[@data-amplitude-event-name='cookie_banner_acknowledge_click']"))
    @property
    def __agregar_carrito(self):
        return self.esperar_por_los_elementos((By.XPATH, "//input[contains(@class, 'js-addtocart')]"))
    
    @property
    def __ingresar_carrito(self):
        return self.esperar_por_los_elementos((By.XPATH, "//div[@id='ajax-cart']"))
    
    @property
    def __borrar_producto(self):
        return self.esperar_por_los_elementos((By.XPATH,"//button[@type='button' and @data-component='line-item.remove']"))
    
    @property
    def __carrito_de_compra_vacio(self):
        return self.esperar_por_los_elementos((By.XPATH, "//div[@data-component='cart.empty-message']"))

    def btn_cookies(self):
         """
         Metodo que se encarga de hacerle click a las cookies
         """
         self.__aceptar_cookies.click()

    def btn_agregar_producto(self):
        """
        Metodo que se encarga de agregar al carrito un producto
        """
        self.__agregar_carrito.click()
    
    def click_ir_a_carrito(self):
        """
        metodo que se encarga de ir al carrito
        """
        self.__ingresar_carrito.click()
    
    def eliminar_producto_del_carrito(self):
        """
        Metodo que se encarga de eliminar el producto del carrito de compras
        """
        self.__borrar_producto.click()

    def visualizar_carrito(self):
        if self.__carrito_de_compra_vacio.text:
            texto = self.__carrito_de_compra_vacio.text
            assert texto == "El carrito de compras está vacío."
            print(texto)
        else:
            print("El carrito de compras no esta vacio o el texto no es correcto!")


