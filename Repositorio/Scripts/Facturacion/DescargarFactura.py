from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Funciones.Menu.Menu import *
from Repositorio.Objetos.Home import *
from Repositorio.Objetos.Facturacion.EmitirFactura import *

class DescargarFactura():
   
   def __init__(self,driver):
      
      self.driver = driver

   def descargarFactura(self,dataTable,tiempo):
      
      driver = self.driver
      
    #Llamamos a la plantilla de excel con los datos de prueba   
      xl = Funexcel_pd(driver)
      
    #datos generales factura
      hojaGeneral = "general"
      filasHojaGeneral = xl.numRow(dataTable,hojaGeneral)

    #Instanciamos variables   
      fx = Funciones(driver)
      menu = Menu(driver)
      objFa = ObjEmitirFactura
      objHm = ObjHome

    #Navegador

      fx.click("Navegador",By.XPATH,objHm.navigator,tiempo)

      menu.clickOpcionMenu(objHm.menuComprobanteVenta,1)

      for j in range(0,filasHojaGeneral):        

         #datos generales factura

         if xl.readData(dataTable,hojaGeneral,"i_factura",j) == "NO":
            continue

         error=xl.readData(dataTable,hojaGeneral,"o_asiento",j)
         fecha = xl.readData(dataTable,hojaGeneral,"i_fecha",j)
         numeroFactura = xl.readData(dataTable,hojaGeneral,"i_numeroFactura",j)

         if error == "Error":
            continue

         fx.click("Click fecha",By.XPATH,objFa.fechaDesdeInput,tiempo)
         fx.input("Fecha desde",By.XPATH,objFa.fechaDesdeInput,fecha,tiempo)
         fx.click("Click fecha",By.XPATH,objFa.fechaDesdeInput,tiempo)
         fx.input("Fecha hasta",By.XPATH,objFa.fechaHastaInput,fecha,tiempo)
         fx.scroll(0,250,tiempo)
         fx.buscar("Factura",By.XPATH,objFa.filtroNumeroComprobanteInput,numeroFactura,tiempo)
         fx.click("Resultado",By.XPATH,"//tr[@class='jqgrow ui-row-ltr']//td[contains(.,'"+numeroFactura+"')]",tiempo)
         fx.scroll(0,200,tiempo)
         fx.click("Click reporte detallado",By.XPATH,objFa.reporteDetalladoBtn,5)

         driver.switch_to.frame(fx._buscaObjeto(By.ID,objFa.modalFactura))

         reporteDetallado = fx.styleObjeto(By.XPATH,objFa.loading,"visibility",3)
         while reporteDetallado == "visible":
            print("Loading")
            reporteDetallado = fx.styleObjeto(By.XPATH,objFa.loading,"visibility",3)
        
         #fx.input("hola",By.XPATH,objFa.hojaInput,"hola",tiempo)  
         
         #reporteDetallado = fx.existeObjeto(By.XPATH,objFa.hojaInput,tiempo)   
         #while reporteDetallado == False:
         #   print("Esperando reporte")
         #   reporteDetallado = fx.existeObjeto(By.XPATH,objFa.hojaInput,tiempo)

         fx.click("Click guardar",By.XPATH,objFa.guardarBtn,3)
         fx.click("Click PDF",By.XPATH,objFa.opcionPdf,3)

         reporteDetallado = fx.existeObjeto(By.XPATH,objFa.hojaInput,tiempo)   
         while reporteDetallado == False:
            print("Esperando descarga")
            reporteDetallado = fx.existeObjeto(By.XPATH,objFa.hojaInput,tiempo)

         driver.switch_to.default_content()
         fx.click("Cerrar",By.XPATH,objFa.cerrarBtn,tiempo)