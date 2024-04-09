from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.LogIn import *
from Repositorio.Objetos.SeleccionarEmpresa import *

class LogIn():
   
   def __init__(self,driver):
      
      self.driver = driver

   def logIn(self,user,tiempo):
      
      driver = self.driver
      
   #Llamamos a la plantilla de excel con los datos de prueba
   
      xl = Funexcel_pd(driver)
      dataTable = "DataTables//Usuarios.xlsx"
      hoja = "Sheet1"            
      
      url = xl.readData(dataTable,hoja,"url",0)
      #El password debe buscarse acorde al usuario que viene por parametro en la DT definida
      password = xl.buscarValor(dataTable,hoja,"user","password",user)
      
   #Comenzamos con el proceso de logeo
   
      fx = Funciones(driver)
      objlg = ObjLogIn
      objSe = ObjSeleccionaEmpresa
      
      fx.navegar(url,tiempo)
      fx.input("Usuario",By.XPATH,objlg.user,user,tiempo)
      fx.input("Password",By.XPATH,objlg.password,password,tiempo)
      fx.click("Iniciar Sesión",By.XPATH,objlg.loginBtn,tiempo)
      
      fx.assertTrue(fx.getTituloWeb(tiempo),objSe.titulo,"Login' - Fallo")