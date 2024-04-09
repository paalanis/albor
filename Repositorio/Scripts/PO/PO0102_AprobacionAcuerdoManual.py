from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *


class PO0102():
   
   def __init__(self,driver):
      
      self.driver = driver

   def AprobacionAcuerdoManual(self,dataTable,tiempo):
       
      driver = self.driver
      
      #asignar variables de excel
      xl = Funexcel_pd(driver)
      
      hoja = "Sheet1"
      numeroAcuerdo = xl.readData(dataTable,hoja,"o_numeroAcuerdo",0)
      estilo = xl.readData(dataTable,hoja,"i_estilo",0)
      estilo = estilo.lower()
      estilo = estilo.capitalize()
      documento = "("+estilo+") "+numeroAcuerdo
      
      fx = Funciones(driver)
      objHm = ObjHome
   
   
   #Ingresamos al home
   
      fx.click("Home",By.XPATH,objHm.logoArcos,tiempo)
      fx.click("Mostrar tareas pendientes",By.XPATH,objHm.mostrarMasPendientesBtn,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objHm.tituloNotificaciones,tiempo),"Notificaciones","No se puedo ingresar al home de Notificaciones")
      fx.buscar(documento,By.XPATH,objHm.buscarInput,documento,tiempo)
            
      objeto = "//button[contains(@title,'Approve  Document "+documento+"')]"
      objeto = fx.buscarIterado(By.XPATH,objeto,objHm.buscarInput,documento,tiempo)
        
      fx.click("Resultado",By.XPATH,objeto,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objHm.mensejaListo,tiempo),"Listo!","Algo falló, no pudo aprobarse el acuerdo")
      