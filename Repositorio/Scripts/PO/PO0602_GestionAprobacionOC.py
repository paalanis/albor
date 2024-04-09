from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
from Repositorio.Objetos.Compras.OrdenComprasHome import *
from Repositorio.Objetos.Compras.OrdenComprasProcesarSolicitud import *



class PO0602():
   
   def __init__(self,driver):
      
      self.driver = driver

   def GestionAprobacionOC(self,tiempo):
       
      driver = self.driver
      
      fx = Funciones(driver)
      objOcPs = ObjOrdenComprasProcesarSolicitud
   
   #Gestionar aprobaciones
   
      fx.click("Gestionar aprobaciones",By.XPATH,objOcPs.gestionarAprobacionBtn,tiempo)
      fx.existeObjeto(By.XPATH,objOcPs.gestionarAprobacionTitulo,tiempo)
      fx.input("Nota al aprobador",By.XPATH,objOcPs.notaAprobadorInput,"",tiempo)
      fx.click("Enviar",By.XPATH,objOcPs.enviarBtn,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objOcPs.confirmacionMsjTitulo,tiempo),"Confirmación","Error al enviar acuerdo para su aprobacion")
      fx.click("Aceptar confirmacion",By.XPATH,objOcPs.confimacionAceptarBtn,tiempo)