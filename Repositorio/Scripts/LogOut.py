from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.LogOut import *

class LogOut():
   
   def __init__(self,driver):
      
      self.driver = driver

   def logOut(self,tiempo):
      
      driver = self.driver      
 
   #Comenzamos con el proceso de logout
   
      fx = Funciones(driver)
      objlg = ObjLogOut
      
      fx.click("Usuario",By.XPATH,objlg.usuarioBtn,tiempo)
      fx.click("Cerrar Sesion",By.XPATH,objlg.cerrarSesionBtn,tiempo)
      
      fx.assertTrue(fx.getTituloWeb(tiempo),objlg.titulo,"Logout' - Fallo")