from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
from Repositorio.Scripts.LogIn import *
from Repositorio.Scripts.LogOut import *
from Repositorio.Objetos.Compras.OrdenComprasHome import *
from Repositorio.Objetos.Compras.OrdenComprasGestionarOrden import *


class PO0603():
   
   def __init__(self,driver):
      
      self.driver = driver

   def AprobacionOC(self,user,dataTable,tiempo):
       
      driver = self.driver
      
      #asignar variables de excel
      xl = Funexcel_pd(driver)
      
      hoja = "Sheet1"
      numeroOC = xl.readData(dataTable,hoja,"o_numeroOc",0)
      documento = "Orden de compra "+numeroOC
      
      fx = Funciones(driver)
      objHm = ObjHome
      objOcHm = ObjOrdenComprasHome
      objOcGs = ObjOrdenComprasGestionarOrden

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
      
   #Ingresamos al home  
      fx.click("Navegador",By.XPATH,objHm.navegador,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      
   #Ordenes de compras
   
      fx.click("Compras",By.XPATH,objHm.menuComprasBtn,tiempo)
      fx.click("Ordenes compras",By.XPATH,objHm.ordenCompraBtn,tiempo)
      
   #Gestionar ordenes
   
      fx.click("Menú tareas",By.XPATH,objOcHm.menuTareasBtn,tiempo)
      fx.click("Gestionar ordenes",By.XPATH,objOcHm.gestionarOrdenBtn,tiempo)
      
   #Buscar OC

      fx.existeObjeto(By.XPATH,objOcGs.gestionarOrdenesTitulo,tiempo)
      fx.input("Orden",By.XPATH,objOcGs.ordenInput,numeroOC,tiempo)
      fx.click("Buscar",By.XPATH,objOcGs.buscarBtn,tiempo)
      fx.existeObjeto(By.XPATH,objOcGs.resultadoBusquedaTitulo,tiempo)
      fx.click("Orden",By.XPATH,"//table[@class='x1a']//a[@class='xmv'][contains(.,"+numeroOC+")]",tiempo)
      
      fx.assertTrue(fx.getText(By.XPATH,objOcGs.estado,tiempo),"Abierta","Error al aprobar OC - Estado deber ser ABIERTA")
      fx.assertTrue(fx.getText(By.XPATH,objOcGs.estadoFondos,tiempo),"Reservada","Error al aprobar OC - Estado Fondos debe ser RESERVADA")
      