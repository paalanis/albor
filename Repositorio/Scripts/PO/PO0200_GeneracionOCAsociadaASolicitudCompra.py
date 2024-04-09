from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
from Repositorio.Objetos.Compras.OrdenComprasHome import *
from Repositorio.Objetos.Compras.OrdenComprasProcesarSolicitud import *



class PO0200():
   
   def __init__(self,driver):
      
      self.driver = driver

   def GeneracionOCAsociadaASolicitudCompra(self,dataTable,tiempo):
       
      driver = self.driver
      
      #asignar variables de excel
      xl = Funexcel_pd(driver)
      
      hoja = "Sheet1"
      unidadDeNegocio = xl.readData(dataTable,hoja,"i_unidadDeNegocio",0)
      solicitud = xl.readData(dataTable,hoja,"o_numeroSolicitud",0)
      tipo = xl.readData(dataTable,hoja,"i_tipo",0)
      descripcionOc = xl.readData(dataTable,hoja,"i_descripcionOc",0)      
      
      fx = Funciones(driver)
      objHm = ObjHome
      objOcHm = ObjOrdenComprasHome
      objOcPs = ObjOrdenComprasProcesarSolicitud
   
   
   #Ingresamos al home  
      fx.click("Navegador",By.XPATH,objHm.navegador,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      
   #Ordenes de compras
   
      fx.click("Compras",By.XPATH,objHm.menuComprasBtn,tiempo)
      fx.click("Ordenes compras",By.XPATH,objHm.ordenCompraBtn,tiempo)
      
   #Procesar solicitudes

      fx.click("Menú tareas",By.XPATH,objOcHm.menuTareasBtn,tiempo)      
      fx.click("Procesar solicitudes",By.XPATH,objOcHm.procesarSolicitudBtn,tiempo)      
      fx.existeObjeto(By.XPATH,objOcPs.procesarSolicitudTitulo,tiempo)
      fx.selectTexto("Unidad de negocio",By.XPATH,objOcPs.unidadDeNegocioSelect,unidadDeNegocio,tiempo)
      fx.input("Solicitud",By.XPATH,objOcPs.solicitudInput,solicitud,tiempo)
      fx.limpiaObjeto("Borrar comprador",By.XPATH,objOcPs.compradorInput,tiempo)
      fx.click("Buscar",By.XPATH,objOcPs.buscarBtn,tiempo)
   
   #Agregar al generador de documentos 
   
      #validamos que si el boton "Agregar al generador de documentos esta "enabled"
      #agregarBtn=fx._buscaObjeto(By.XPATH,objOcPs.agregarBtn)
      #print(agregarBtn)
      #if agregarBtn.is_enabled() != True:
      fx.click("Seleccionar todos",By.XPATH,objOcPs.seleccionarTodosBtn,tiempo)      
      fx.click("Agregar al generador",By.XPATH,objOcPs.agregarBtn,tiempo)      
      fx.existeObjeto(By.XPATH,objOcPs.lineasSeleccionadasTitulo,tiempo)
      fx.selectTexto("Tipo",By.XPATH,objOcPs.tipoSelect,tipo,tiempo)
      fx.click("Aceptar",By.XPATH,objOcPs.lineasAceptarBtn,tiempo)
   
   #Generador de documentos
   
      fx.existeObjeto(By.XPATH,objOcPs.generadorDocumentosTitulo,tiempo)
      fx.click("Editar",By.XPATH,objOcPs.editarBtn,tiempo)
   
   #Editar generador de documentos
   
      fx.existeObjeto(By.XPATH,objOcPs.editarGeneradorTitulo,tiempo)
      fx.click("Crear",By.XPATH,objOcPs.crearBtn,tiempo)
      fx.existeObjeto(By.XPATH,objOcPs.crearMensajeTitulo,tiempo)
      
      mensaje = fx.getText(By.XPATH,objOcPs.crearMensaje,tiempo)
      numeroOC = fx.getNumber(mensaje)
      
      fx.assertTrue(mensaje, "Se creó el documento (Orden de compra) "+numeroOC+".","Error al crear OC")
      #se guarda este dato en la dataTable
      xl.writeData(dataTable,hoja,"o_numeroOc",numeroOC)
      
      fx.click("Aceptar",By.XPATH,objOcPs.crearAceptarBtn,tiempo)
      
   #Editar OC creada
   
      fx.existeObjeto(By.XPATH,objOcPs.editarDocumentoTitulo,tiempo)
      fx.input("Descripcion",By.XPATH,objOcPs.descripcionInput,descripcionOc,tiempo)
      
   #Guardar
   
      fx.click("Guardar",By.XPATH,objOcPs.guardarBtn,tiempo)
      #agregar assert? se debe validar si se guardó o no?
      fx.softAssertTrue(fx.getText(By.XPATH,objOcPs.mensajeGuardar,tiempo),
                        "Última vez que se guardó","No se guardo el acuerdo","Se guardo acuerdo: "+fx.getText(By.XPATH,objOcPs.horaGuardar,tiempo),tiempo)
   
   #Comprobar fondos
    
      fx.click("Comprobar Fondos",By.XPATH,objOcPs.comprobarFondosBtn,tiempo)
      fx.existeObjeto(By.XPATH,objOcPs.aprobacionMsjTitulo,tiempo)
      fx.click("Aceptar",By.XPATH,objOcPs.aprobacionAceptarBtn,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objOcPs.estadoFondosMsj,tiempo),"Aprobado","Error al comprobar fondos")

      
      