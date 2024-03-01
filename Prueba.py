import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Funciones_internas import Funciones1
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
t = 2

######################### Datos de ingreso ##############
url = "https://opencart.abstracta.us/"
producto = "iphone"

#######################################################

class base_test(unittest.TestCase):

    def setUp(self):
        s = Service("C:\drivers_net\chromedriver.exe")  # driver chrome
        self.driver = webdriver.Chrome(service=s)

    def test_carrito(self):
        driver = self.driver
        f = Funciones1(driver)
        f.Pagina(url,t)
        f.IngresoDatos("//input[contains(@type,'text')]", producto,t) #Ingresar producto en barra busqueda
        f.EventoClick("(//button[contains(@type,'button')])[4]",t) #boton de busqueda
        f.EventoClick("//img[contains(@alt,'iPhone')]",t) #Selección producto
        f.EventoClick("//button[contains(@id,'button-cart')]",t)  # Agregando al carrito
        f.EventoClick("//span[contains(@id,'cart-total')]", t)  # boton carrito
        f.EventoClick("//strong[contains(.,'View Cart')]", t)  # Ingresando carrito
        f.EventoClick("//i[contains(@class,'fa fa-times-circle')]", t)  # Remover producto


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()