import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
import re
from unicodedata import normalize

WDW = 10 #Tiempo WebDriverWait

class Menu():

    def __init__(self,driver):

        self.driver = driver

    def sinTildes(self,texto):

        # -> NFD y eliminar diacríticos
        texto = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", texto), 0, re.I
            )

        # -> NFC
        texto = normalize( 'NFC', texto)

        return texto
        
    def clickOpcionMenu(self,opcionMenu,tiempo):
        '''Realiza un click en el objeto html definido. Inserta un valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        alias: nombre del paso a mostrar en el reporte de pytest.\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        
        fx = Funciones(self.driver)
        objHm = ObjHome

        try:
            fx.input("Opcion",By.XPATH,objHm.buscadorMenuInput,opcionMenu,tiempo)
            opcionMenuBis = opcionMenu.split(" ")

            for clave in opcionMenuBis:
                if fx.existeObjeto(By.XPATH,"//ul[@id='resultados-busqueda']//a[contains(@href,'/"+self.sinTildes(clave)+"')]//span[@class='nav-label'][contains(.,'"+opcionMenu+"')]",tiempo):
                    obj = fx._buscaObjeto(By.XPATH,"//ul[@id='resultados-busqueda']//a[contains(@href,'/"+self.sinTildes(clave)+"')]//span[@class='nav-label'][contains(.,'"+opcionMenu+"')]")
                    obj.click()
                
            print("Damos click en: {}".format(opcionMenu))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo dar click en: " + opcionMenu)