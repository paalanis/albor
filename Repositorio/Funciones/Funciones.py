import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import StaleElementReferenceException
import re


WDW = 10 #Tiempo WebDriverWait
TB = 1 #Tiempo interno de busqueda en tablas
ITERACIONES = 50 #Cantidad de iteraciones en busquedas con persistencia

class Funciones():

    def __init__(self,driver):

        self.driver = driver
        self.act = ActionChains (driver)

    def _buscaObjeto(self,tipo,objeto):
        '''Busca un objeto html dentro del DOM, espera a que exista el tiempo de WDW, realiza scroll hasta el. Retorna un objeto.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.
        '''
        
        try:
               #print("Se busca objeto: " + objeto)
               obj = WebDriverWait(self.driver,WDW).until(EC.visibility_of_element_located((tipo,objeto)))
               self.act.scroll_to_element(obj).perform()
               obj = self.driver.find_element(tipo,objeto)
               return obj
        except StaleElementReferenceException as e:
           print(e.msg)
           print("No existe el objeto " + objeto)

    def existeObjeto(self,tipo,objeto,tiempo):
        '''Comprueba si un objeto html existe en el DOM, devuelve True or False.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            time.sleep(tiempo)
            obj = self.driver.find_element(tipo,objeto)
            obj = obj.is_displayed()
            return True
        except:
            return False

    def limpiaObjeto(self,alias,tipo,objeto,tiempo):
        '''Limpia el valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        alias: nombre del paso a mostrar en el reporte de pytest.\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            obj = self._buscaObjeto(tipo,objeto)
            obj.clear()
            print("Se limpia el campo: {}".format(alias))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo limpiar el campo: " + alias)

    def navegar(self,url,tiempo):
        '''Navega a la URL indicada.
        Argumentos:\n
        url: 'https://....com'.\n
        tiempo: tiempo de espera entre pasos.
        '''
        self.driver.get(url)
        self.driver.maximize_window()
        print("Url abierta: " + str(url))
        t = time.sleep(tiempo)
        return t

    def input(self,alias,tipo,objeto,texto,tiempo):
        '''Inserta un valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        alias: nombre del paso a mostrar en el reporte de pytest.\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        texto: valor a ingresar en el campo.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            obj = self._buscaObjeto(tipo,objeto)
            #obj.clear()
            obj.send_keys(texto)
            print("Se completa el campo: {}".format(alias))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo completar el campo: " + alias)

    def click(self,alias,tipo,objeto,tiempo):
        '''Realiza un click en el objeto html definido. Inserta un valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        alias: nombre del paso a mostrar en el reporte de pytest.\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            obj = self._buscaObjeto(tipo,objeto)
            obj.click()
            print("Damos click en: {}".format(alias))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo dar click en: " + alias)

    def selectTexto(self,alias,tipo,objeto,texto,tiempo):
        '''Seleccion por texto visible en un objeto de tipo SELECTInserta un valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        alias: nombre del paso a mostrar en el reporte de pytest.\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        texto: valor a seleccionar.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            obj = self._buscaObjeto(tipo,objeto)
            obj=Select(obj)
            obj.select_by_visible_text(texto)
            print("Seleccionamos la opción: {}".format(alias))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo seleccionar: " + texto)

    def getText(self,tipo,objeto,tiempo):
        '''Obtiene del objeto el texto visibleInserta un valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            time.sleep(tiempo)
            obj = self._buscaObjeto(tipo,objeto)
            obj.text
            texto = obj.text
            #print("Texto: " + texto)
            return texto
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo obtener el texto")

    def getTituloWeb(self,tiempo):
        '''Obtiene el tÍtulo del DOMInserta un valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            time.sleep(tiempo)
            titulo = self.driver.title
            return titulo
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo obtener el titulo")

    def getNumber(self,texto):
        '''Obtiene el contenido numérico dentro de una cadena de textoInserta un valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        texto: cadena de texto.
        '''
        str = re.findall("(\d*\.\d+|\d+\d*)", texto)
        numeracion = "".join(str)
        return numeracion

    def buscadorSelect(self,tipo,
                       objBuscador,
                       objBuscadorLink,
                       objInput,
                       textoInput,
                       objBuscadorInt,
                       objResultado,
                       objAceptarBtn,
                       tiempo):
        '''Realiza una búsqueda avanzada en objetos de tipo SELECT SEARCH en los cuales figure el link "Buscar" dentro de las opcionesInserta un valor dentro un objeto determinado de tipo INPUT.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objBuscadorLink: objeto HTML, (flecha del objeto SELECT).\n
        objInput: objeto INPUT donde realizar la búsqueda avanzada.\n
        textoInput: valor a ingresar en el campo INPUT.\n
        objBuscadorInt: botón de búsqueda interno.\n
        objResultado: objeto generado por el resultado de búsqueda.\n
        objAceptarBtn: botón aceptar interno.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            self.click("Buscar",tipo,objBuscador,tiempo)
            self.click("Link",tipo,objBuscadorLink,tiempo)

            obj = self._buscaObjeto(tipo,objInput)
            obj.clear()
            obj.send_keys(textoInput)
            print("Texto a buscar: {}".format(textoInput))

            self.click("Buscar interno",tipo,objBuscadorInt,tiempo)

            time.sleep(TB)
            self.click("Rusultado busqueda",tipo,objResultado,tiempo)
            self.click("Aceptar",tipo,objAceptarBtn,tiempo)

            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("Se produjo un error en la busqueda de: " + textoInput)

    def buscadorLupa(self,tipo,
                       objBuscador,
                       objInput,
                       textoInput,
                       objResultado,
                       objAceptarBtn,
                       tiempo):
        '''Realiza una búsqueda avanzada en objetos de tipo INPUT SEARCH con opción de búsqueda. Figura una lupa junto al INPUT.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objBuscador: objeto HTML, (lupa).\n
        objInput: objeto INPUT donde realizar la búsqueda avanzada.\n
        textoInput: valor a ingresar en el campo INPUT.\n
        objResultado: objeto generado por el resultado de búsqueda.\n
        objAceptarBtn: botón aceptar interno.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            self.click("Buscar",tipo,objBuscador,tiempo)

            obj = self._buscaObjeto(tipo,objInput)
            obj.clear()
            obj.send_keys(textoInput, Keys.RETURN)
            print("Texto a buscar: {}".format(textoInput))
            
            time.sleep(TB)
            self.click("Rusultado busqueda",tipo,objResultado,tiempo)
            self.click("Aceptar",tipo,objAceptarBtn,tiempo)

            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("Se produjo un error en la busqueda de: " + textoInput)

    def buscar(self,alias,tipo,objeto,texto,tiempo):
        '''Realiza un búsqueda dentro de objetos de tipo INPUT SEARCH sin opción de búsqueda avanzada.
        Argumentos:\n
        alias: nombre del paso a mostrar en el reporte de pytest.\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        texto: valor a buscar.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            obj = self._buscaObjeto(tipo,objeto)
            obj.clear()
            obj.send_keys(texto, Keys.RETURN)
            print("Texto a buscar: {}".format(alias))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo buscar: " + alias)
    
    def buscarIterado(self,tipo,objeto,buscarInput,documento,tiempo):
        '''Realiza un búsqueda dentro de objetos de tipo INPUT SEARCH documentos de forma iterada.
        Argumentos:\n
        alias: nombre del paso a mostrar en el reporte de pytest.\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        buscarInput: objeto HTML donde realizar la busqueda.\n
        documento: texto buscado.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:               
            objetoBool = self.existeObjeto(tipo,objeto,tiempo)
            intentos = 0
            while objetoBool == False:
                 self.buscar("Intento: "+str(intentos)+"/"+str(ITERACIONES)+" de busqueda de: "+documento,tipo,buscarInput,documento,tiempo)
                 intentos += 1
                 if intentos == ITERACIONES:
                    assert objeto==True, "No se encuentra: "+documento
                 objetoBool = self.existeObjeto(tipo,objeto,tiempo)
            return objeto
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo buscar")
    
    def tab(self,tipo,objeto,tiempo):
        '''Realiza un TAB a un objeto determinado.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            obj = self._buscaObjeto(tipo,objeto)
            obj.send_keys(Keys.TAB,Keys.TAB)
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo hacer TAB")

    def scroll(self,x,y,tiempo):
        '''Realiza un SCROLL en una direccion a un objeto determinado.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        dir: direccion "up","down","left","right"\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            self.act.scroll_by_amount(x,y).perform()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo hacer SCROLL")

    def scrollElement(self,tipo,objeto,tiempo):
        '''Realiza un SCROLL en una direccion a un objeto determinado.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        dir: direccion "up","down","left","right"\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            obj = self._buscaObjeto(tipo,objeto)
            self.act.scroll_to_element(obj).perform()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as e:
           print(e.msg)
           print("No se pudo hacer SCROLL")

    def assertTrue(self,mensaje,mensajeEsperado,errorMensaje):
        '''Realiza una comprobación entre mensaje dado y esperado. Si no coinciden la prueba se cancela.
        Argumentos:\n
        mensaje: mensaje generado por la aplicación web.\n
        mensajeEsperado: mensaje esperado por nosotros.\n
        errorMensaje: mensaje a mostrar en el reporte de pytest indicando el fallo.
        '''
        mensaje = mensaje.lower()
        mensajeEsperado = mensajeEsperado.lower()
        assert mensaje==mensajeEsperado,errorMensaje

        #print(mensaje.capitalize())

    def softAssertTrue(self,mensaje,mensajeEsperado,errorMensaje,mensajeOk,tiempo):
        '''Realiza una comprobación entre mensaje dado y esperado. Si no coinciden emite un WARNING pero avanza con la prueba.
        Argumentos:\n
        mensaje: mensaje generado por la aplicación web.\n
        mensajeEsperado: mensaje esperado por nosotros.\n
        errorMensaje: mensaje a mostrar en el reporte de pytest indicando el fallo.\n
        mensajeOk: mensaje a mostrar en el reporte de pytest indicando detalle.\n
        tiempo: tiempo de espera entre pasos.
        '''
        if(mensaje!=mensajeEsperado):
            print("{} Se esperaba: {} pero se encontró {}".format(errorMensaje,mensajeEsperado,mensaje))
            time.sleep(tiempo)
            return False        
        else:
            print(mensajeOk)
            time.sleep(tiempo)
            return True
        
    def tamanoOjeto(self,tipo,objeto,tiempo):
        '''Comprueba si un objeto html existe en el DOM, devuelve True or False.\n
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            time.sleep(tiempo)
            obj = WebDriverWait(self.driver,WDW).until(EC.visibility_of_element_located((tipo,objeto)))
            tamano = obj.get_attribute("height")            
            return tamano
        except TimeoutException as e:
            print("Error")

    def getValue(self,tipo,objeto,tiempo):
        '''Obtiene el contenido del atributo Value.\n
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            time.sleep(tiempo)
            obj = self._buscaObjeto(tipo,objeto)
            valor = self.driver.execute_script("return arguments[0].value",obj)            
            return valor
        except TimeoutException as e:
            print(e.msg)
            print("No se pudo obtener value")

    def estadoDisabled(self,tipo,objeto,tiempo):
        '''Comprueba el estado DISABLED de un objeto permitido.\n
        Return Bool.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            time.sleep(tiempo)
            obj = self._buscaObjeto(tipo,objeto)
            estado = self.driver.execute_script("return arguments[0].disabled",obj)            
            return estado
        except TimeoutException as e:
            print(e.msg)
            print("No se pudo obtener value")

    def styleObjeto(self,tipo,objeto,tipoStyle,tiempo):
        '''.\n
        Return String.
        Argumentos:\n
        tipo: By.XPATH, ByID, etc.\n
        objeto: objeto HTML.\n
        tiempo: tiempo de espera entre pasos.
        '''
        try:
            time.sleep(tiempo)
            obj = self._buscaObjeto(tipo,objeto)
            style = self.driver.execute_script("return arguments[0].style."+tipoStyle+"",obj)            
            return style
        except TimeoutException as e:
            print(e.msg)
            print("No se pudo obtener style")