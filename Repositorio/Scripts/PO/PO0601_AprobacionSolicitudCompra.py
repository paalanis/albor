from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
from Repositorio.Scripts.LogIn import *
from Repositorio.Scripts.LogOut import *


class PO0601():
   
   def __init__(self,driver):
      
      self.driver = driver

   def AprobacionSolicitudCompra(self,user,dataTable,tiempo):
       
      driver = self.driver
      
      #asignar variables de excel
      xl = Funexcel_pd(driver)
      
      hoja = "Sheet1"
      numeroSolicitud = xl.readData(dataTable,hoja,"o_numeroSolicitud",0)
      documento = "Requisition "+numeroSolicitud
      
      fx = Funciones(driver)
      objHm = ObjHome
      
   #Ingresamos al home del aprobador
      
      fx.click("Home",By.XPATH,objHm.logoArcos,tiempo)
      fx.click("Mostrar tareas pendientes",By.XPATH,objHm.mostrarMasPendientesBtn,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objHm.tituloNotificaciones,tiempo),"Notificaciones","No se puedo ingresar al home de Notificaciones")
      fx.buscar(documento,By.XPATH,objHm.buscarInput,documento,tiempo)
            
      objeto = "//a[contains(@title,' Approve "+documento+"')]"
      objeto = fx.buscarIterado(By.XPATH,objeto,objHm.buscarInput,documento,tiempo)
      
      fx.click("Resultado",By.XPATH,objeto,tiempo)
      
   #cambiamos a la ventana que se abre para aprobar
      self.driver.switch_to.window(self.driver.window_handles[1])
      fx.click("Aprobar",By.XPATH,objHm.nuevaVentanaAprobarBtn,tiempo)
      fx.click("Enviar",By.XPATH,objHm.enviarBtn,tiempo)
      self.driver.switch_to.window(self.driver.window_handles[0])
      
   #Se realiza logOut para ingresar nuevamente con el usuario de testing y comprobar la aprobación
      LogOut.logOut(self,tiempo)
      LogIn.logIn(self,user,tiempo)
      
   #Ingresamos al home del usuario de testing
   
      documento = numeroSolicitud
   
      fx.click("Home",By.XPATH,objHm.logoArcos,tiempo)
      fx.click("Mostrar tareas pendientes",By.XPATH,objHm.mostrarMasPendientesBtn,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objHm.tituloNotificaciones,tiempo),"Notificaciones","No se puedo ingresar al home de Notificaciones")
      fx.buscar(documento,By.XPATH,objHm.buscarInput,documento,tiempo)
            
      objeto="//a[contains(@title,' Solicitud "+documento+" aprobada')]"
      objeto = fx.buscarIterado(By.XPATH,objeto,objHm.buscarInput,documento,tiempo)

      fx.assertTrue(fx.getText(By.XPATH,objeto,tiempo),"Solicitud "+documento+" aprobada","Algo falló, no pudo aprobarse la solicitud")
      