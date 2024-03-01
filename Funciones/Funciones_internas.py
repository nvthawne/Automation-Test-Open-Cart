import time
import warnings
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

class Funciones1():

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self,tie):
        t = time.sleep(tie)
        return t

    def Pagina(self,Url,Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Página a utilizar: " + str(Url))
        t = time.sleep(Tiempo)
        return t

    def IngresoDatos(self,xpath,Texto,Tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(by=By.XPATH, value=(xpath))
            val.clear()
            val.send_keys(Texto)
            print("Ingresando datos en el campo {} el texto {} ".format(xpath, Texto))
            t = time.sleep(Tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + xpath)

    def EventoClick(self,xpath,Tiempo):
        try:
            val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(by=By.XPATH, value=(xpath))
            val.click()
            t = time.sleep(Tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print ("No se encontró el elemento" + xpath)
            return t

    def EventoValidar(self,xpath,Tiempo):
        try:
            val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(by=By.XPATH, value=(xpath))
            val.click()
            t = time.sleep(Tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print ("No se encontró el elemento" + xpath)
            return t






    def Salida(self):
        print("Prueba finalizada")