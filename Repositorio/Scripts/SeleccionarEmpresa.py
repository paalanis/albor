from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
from Repositorio.Objetos.SeleccionarEmpresa import *

class SeleccionarEmpresa():
   
   def __init__(self,driver):
      
      self.driver = driver

   def SeleccionarEmpresa(self,dataTable,tiempo):
      
      driver = self.driver
      
      #asignar variables de excel
      xl = Funexcel_pd(driver)
      
      hoja = "Sheet2"
      user_a = xl.readData(dataTable,hoja,"usuario",0)
      empresa = xl.readData(dataTable,hoja,"empresa",0)
      
   #Comenzamos con el proceso de logeo
   
      fx = Funciones(driver)
      objSe = ObjSeleccionaEmpresa
      objHm = ObjHome

      fx.click("Empresa",By.XPATH,"//label[contains(.,'"+empresa+"')]",tiempo)
      fx.click("Seleccionar",By.XPATH,objSe.seleccionarBtn,tiempo)      
      fx.assertTrue(fx.getTituloWeb(tiempo),objHm.titulo,"Seleccionar empresa'")
      fx.assertTrue(fx.getText(By.XPATH,objHm.nombreUserEmpresa,tiempo),user_a+" "+empresa,"La empresa no es la correcta'")
      