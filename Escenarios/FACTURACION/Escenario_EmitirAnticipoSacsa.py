import datetime
from Repositorio.Scripts.LogIn import *
from Repositorio.Scripts.LogOut import *
from Repositorio.Scripts.SeleccionarEmpresa import *
from Repositorio.Scripts.Facturacion.EmitirFactura import *
from Repositorio.Scripts.Facturacion.DescargarFactura import *
from Repositorio.Scripts.ExcelPandas import *


def test_EscenarioFcSacsa(driver,tiempo):
   
    T = float(tiempo)
    
    #Llamamos a la plantilla de excel con los datos de prueba
    xl = Funexcel_pd(driver)
    dataTable = "DataTables//FACTURACION//EmitirAnticipoSacsa.xlsx"
    hoja = "Sheet2"
   
    user_a = xl.readData(dataTable,hoja,"usuario",0)
        
    LogIn(driver).logIn(user_a,T)
    SeleccionarEmpresa(driver).seleccionarEmpresa(dataTable,T)
    EmitirFactura(driver).emitirFactura(dataTable,T)
    #DescargarFactura(driver).descargarFactura(dataTable,T)
    LogOut(driver).logOut(T)