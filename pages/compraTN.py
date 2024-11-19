from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_carrito_eliminado import ProductosCarrito


class CompraTiendaNube(ProductosCarrito):
    """
    Clase que contiene los elementos para realizar la compra en
    tienda nube
    """
    
    def __init__(self, driver: webdriver.Remote, wait_time=10):
        self.driver = driver
        self.wait_time = wait_time


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
    def __btn_iniciar_compra(self):
        return self.esperar_por_los_elementos((By.XPATH, "//input[@class='btn btn-primary btn-block']"))
    
    @property 
    def __input_email(self):
        return self.esperar_por_los_elementos((By.ID, "contact.email"))
    
    @property
    def __input_codigo_postal(self):
        return self.esperar_por_los_elementos((By.ID, "shippingAddress.zipcode"))
    
    @property
    def __btn_continuar(self):
        return self.esperar_por_los_elementos((By.XPATH, "//div[contains(@class, 'btn-submit-step')]"))
    
    @property 
    def __input_nombre(self):
        return self.esperar_por_los_elementos((By.ID, "shippingAddress.first_name"))
    
    @property
    def __input_apellido(self):
        return self.esperar_por_los_elementos((By.ID, "shippingAddress.last_name"))
    
    @property
    def __input_direccion(self):
        return self.esperar_por_los_elementos((By.ID, "shippingAddress.address"))
    
    @property
    def __input_nro_direccion(self):
        return self.esperar_por_los_elementos((By.ID, "shippingAddress.number"))
    
    @property
    def __input_depto(self):
        return self.esperar_por_los_elementos((By.ID, "shippingAddress.floor"))
    
    @property
    def __input_barrio(self):
        return self.esperar_por_los_elementos((By.ID, "shippingAddress.locality"))
    
    @property
    def __btn_continuar_compra(self):
        return self.esperar_por_los_elementos((By.XPATH, "//button[span='Continuar para el pago']"))
    
    @property
    def __btn_iframe(self):
        iframe = self.esperar_por_los_elementos((By.ID, "iFrameResizer0"))
        self.driver.switch_to.frame(iframe)

    @property
    def __btn_transferencia(self):
        return self.esperar_por_los_elementos((By.XPATH, "//div[text()='Transferencia bancaria']"))
    
    @property
    def __input_documento_comprado(self):
        return self.esperar_por_los_elementos((By.ID, "payment.wireTransfer.holderIdNumber"))
    

    @property
    def __btn_finalizar_compra(self):
        return self.esperar_por_los_elementos((By.ID,"btnFinishCheckout"))
    

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

    def click_btn_compra(self):
        """
        Metodo que se encarga de iniciar la compra
        """
        self.__btn_iniciar_compra.click()


    def primeros_datos(self, email, codigo_postal):
        """
        Metodo que se encarga de ingresar datos
        Args: 
        email: email de la prueba
        codigo postal: Codigo postal para continuar con la prueba
        """
        self.__input_email.send_keys(email)
        self.__input_codigo_postal.send_keys(codigo_postal)
        self.__btn_continuar.click()

    def datos_para_la_compra(self, nombre, apellido, direccion, nro_direccion, depto, barrio):
        """
        Metodo que se encarga de ingresar datos para la compra
        Args:
        nombre: Nombre de la persona
        apellido: apellido de la persona
        direccion: direccion de entrega
        nro_direccion: direccion de entrega
        deto: numero de depto
        barrio: localidad 
        """
        self.__input_nombre.send_keys(nombre)
        self.__input_apellido.send_keys(apellido)
        self.__input_direccion.send_keys(direccion)
        self.__input_nro_direccion.send_keys(nro_direccion)
        self.__input_depto.send_keys(depto)
        self.__input_barrio.send_keys(barrio)

    def btn_ir_al_pago(self):
        """
        Metodo que se encarga de continuar con la compra y avanza al metodo de pago
        """
        self.__btn_continuar_compra.click()

    def ingresa_iframe (self):
        """
        Metodo que se encarga de interactuar con un iframe
        """
        self.__btn_iframe

    def btn_metodo_pago(self):
        """
        Metodo que se encarga de hacerle click al boton de transferencia
        """
        self.__btn_transferencia.click()

    def documento_compra(self, dni):
        """
        Metodo que se encarga de ingresar el documento del comprador
        Args: DNI
        """
        self.__input_documento_comprado.send_keys(dni)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

        
    def finalizar_compra(self):
        """
        Metodo que se encarga de finalizar con la compra
        """
        self.__btn_finalizar_compra.click()

    def get_title(self):
        """
        Función para obtener el título de la página
        """
        title = self.driver.title
        print(f"El titulo de la pagina es: {title}")
        return title
    
    def compra_finalizada(self):
        """
        Metodo que trael el mensaje indicando que se realizó la compra
        """

        expected_title = "Envío y pago - PruebasAutomation" # El titulo es : Envío y pago - PruebasAutomation
        actual_title = self.get_title()
        assert actual_title == expected_title, f"Title mismatch. Expected {expected_title}, Actual {actual_title}"
        print("Se encontro el titulo correctamente")