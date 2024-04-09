from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
from Repositorio.Scripts.LogIn import *
from Repositorio.Scripts.LogOut import *
from Repositorio.Objetos.Compras.MisRecepcionesHome import *

class PO0700():
   
   def __init__(self,driver):
      
      self.driver = driver

   def RecepcionOC(self,dataTable,tiempo):
       
      driver = self.driver
      
      #asignar variables de excel
      xl = Funexcel_pd(driver)
      
      hoja = "Sheet1"
      unidadDeNegocio = xl.readData(dataTable,hoja,"i_unidadDeNegocio",0)
      solicitante = xl.readData(dataTable,hoja,"i_solicitante",0)
      articulosVencidos = xl.readData(dataTable,hoja,"i_articulosVencidos",0)
      numeroOC = xl.readData(dataTable,hoja,"o_numeroOc",0)
      fechaTransaccion = xl.readData(dataTable,hoja,"i_fechaTransaccion",0)
      
      hojaProductos = "productos"
      productoUno = xl.readData(dataTable,hojaProductos,"i_producto",0)
      cantidadUno = xl.readData(dataTable,hojaProductos,"i_cantidad",0)
      
      fx = Funciones(driver)
      objHm = ObjHome
      objHmMr = ObjMisRecepcionesHome
   
   #Ingresamos al home
   
      fx.click("Navegador",By.XPATH,objHm.navegador,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      
   #Mis recepciones
    
      #objeto = self.driver.find_element(By.XPATH,objHm.menuComprasTamano)
      #tamano = objeto.value_of_css_property("height")
      #print(str(tamano))
      fx.click("Compras",By.XPATH,objHm.menuComprasBtn,tiempo)
      #fx.click("Compras",By.XPATH,objHm.menuComprasBtn,tiempo)
      fx.click("Mis recepciones",By.XPATH,objHm.misRecepcionesBtn,tiempo)
      
      
      fx.buscadorSelect(By.XPATH,objHmMr.solicitanteBuscarBtn,objHmMr.solicitanteBuscarLink,objHmMr.solicitanteInput,solicitante,
                        objHmMr.solicitanteBuscarInterBtn,objHmMr.solicitanteResultado,objHmMr.solicitanteAceptarBtn,tiempo)
      fx.selectTexto("Unidad de negocio",By.XPATH,objHmMr.unidadDeNegocioSelect,unidadDeNegocio,tiempo)
      fx.selectTexto("Articulos vencidos",By.XPATH,objHmMr.articulosVencidosSelect,articulosVencidos,tiempo)
      fx.buscadorSelect(By.XPATH,objHmMr.ordenCompraBuscarBtn,objHmMr.ordenCompraBuscarLink,objHmMr.ordenCompraInput,numeroOC,
                        objHmMr.ordenCompraBuscarInterBtn,objHmMr.ordenCompraResultado,objHmMr.ordenCompraAceptarBtn,tiempo)
      
      fx.click("Buscar",By.XPATH,objHmMr.buscarBtn,tiempo)
      fx.existeObjeto(By.XPATH,objHmMr.filasSeleccionadasTitulo,tiempo)
      fx.click("Seleccionar articulo",By.XPATH,"//span[@class='x2hi'][contains(.,'"+productoUno+"')]",tiempo)
      
      fx.assertTrue(fx.getText(By.XPATH,objHmMr.filasSeleccionadas,tiempo),"1","No se seleccionaron filas")
      fx.click("Recibir",By.XPATH,objHmMr.recibirBtn,tiempo)
      
   #Crear recepciones

      fx.existeObjeto(By.XPATH,objHmMr.crearRecepcionesTitulo,tiempo)
      fx.input("Cantidad",By.XPATH,objHmMr.unidadesRecibidasInput,cantidadUno,tiempo)
      fx.input("Fecha transaccion",By.XPATH,objHmMr.fechaTransaccionInput,fechaTransaccion,tiempo)
      fx.click("Enviar",By.XPATH,objHmMr.enviarBtn,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objHmMr.confirmacionMsjTitulo,tiempo),"Confirmación","Error al enviar recepcion")
      
      numeroRecepcion = fx.getNumber(fx.getText(By.XPATH,objHmMr.confirmacionMsj,tiempo))
      xl.writeData(dataTable,hoja,"o_numeroRecepcion",numeroRecepcion)
      
      fx.click("Aceptar",By.XPATH,objHmMr.confirmacionAceptarBtn,tiempo)
      
      print("Se creó Recepcion N°: "+numeroRecepcion)