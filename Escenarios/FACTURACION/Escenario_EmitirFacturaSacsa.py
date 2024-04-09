import datetime
from Repositorio.Scripts.LogIn import *
from Repositorio.Scripts.LogOut import *
from Repositorio.Scripts.SeleccionarEmpresa import *
from Repositorio.Scripts.ExcelPandas import *


def test_Escenario1(driver,tiempo):
   
    T = float(tiempo)
    
    #Llamamos a la plantilla de excel con los datos de prueba
    xl = Funexcel_pd(driver)
    dataTable = "DataTables//FACTURACION//EmitirFacturaSacsa.xlsx"
    hoja = "Sheet2"
   
    user_a = xl.readData(dataTable,hoja,"usuario",0)
        
    LogIn(driver).logIn(user_a,T)
    SeleccionarEmpresa(driver).SeleccionarEmpresa(dataTable,T)
    LogOut(driver).logOut(T)