from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
from Repositorio.Objetos.Compras.SolicitudComprasHome import *


class PO0203():
   
   def __init__(self,driver):
      
      self.driver = driver

   def IngresoSolicitudCompraManual(self,dataTable,tiempo):
       
      driver = self.driver
      
      #asignar variables de excel
      xl = Funexcel_pd(driver)
      
      hoja = "Sheet1"      
      unidadDeNegocio = xl.readData(dataTable,hoja,"i_unidadDeNegocio",0)
      solicitante = xl.readData(dataTable,hoja,"i_solicitante",0)
      ubicacionEntrega = xl.readData(dataTable,hoja,"i_ubicacionEntrega",0)
      descripcion = xl.readData(dataTable,hoja,"i_descripcion",0)
      
      fx = Funciones(driver)
      objHm = ObjHome
      objHmSC = ObjSolicitudComprasHome
   
   
   #Ingresamos al home
   
      fx.click("Navegador",By.XPATH,objHm.navegador,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      
   #Crear solicitud de compra
    
      fx.click("Compras",By.XPATH,objHm.menuComprasBtn,tiempo)
      fx.click("Solicitudes de compra",By.XPATH,objHm.solicitudesCompraBtn,tiempo)
      fx.click("Preferencias de solicitud",By.XPATH,objHmSC.preferenciasSolicitudBtn,tiempo)
      fx.selectTexto("Unidad de negocio",By.XPATH,objHmSC.unidadDeNegocioSelect,unidadDeNegocio,tiempo)
      fx.buscadorLupa(By.XPATH,objHmSC.solicitanteBuscarBtn,objHmSC.solicitanteInput,solicitante,objHmSC.solicitanteResultado,objHmSC.solicitanteAceptarBtn,tiempo)
      fx.buscadorLupa(By.XPATH,objHmSC.ubicacionEntregaBuscarBtn,objHmSC.ubicacionEntregaInput,ubicacionEntrega,objHmSC.ubicacionEntregaResultado,objHmSC.ubicacionEntregaAceptarBtn,tiempo)
      fx.click("Guardar y cerrar",By.XPATH,objHmSC.guardarCerrarBtn,tiempo)
      
      
   #Comprar por catégoria
      fx.existeObjeto(By.XPATH,objHmSC.categoriasTitulo,tiempo) 
   
      hojaProductos = "productos"
      filas = xl.numRow(dataTable,hojaProductos)
      
      for i in range(0,filas):
         producto = xl.readData(dataTable,hojaProductos,"i_producto",i)
         cantidad = xl.readData(dataTable,hojaProductos,"i_cantidad",i)
         fx.buscar(producto,By.XPATH,objHmSC.buscarProductoInput,producto,3.5)
         fx.existeObjeto(By.XPATH,"//span[@class='x2vp'][contains(.,'"+producto+"')]",tiempo) 
         fx.input("Cantidad",By.XPATH,objHmSC.cantidaInput,cantidad,tiempo)
         fx.click("Agregar al carrito",By.XPATH,objHmSC.agregarCarroBtn,2.5)
   
   #consultar si es necesario controlar el ingreso total de los Productos, para esto no deberian existir Productos pendientes
   
   #Revisar carro
   
      fx.click("Mostrar carro",By.XPATH,objHmSC.carroComprasBtn,tiempo)
      fx.existeObjeto(By.XPATH,objHmSC.totalCarroTitulo,tiempo)
      fx.click("Revisar",By.XPATH,objHmSC.revisarBtn,tiempo)
      fx.input("Descripcion",By.XPATH,objHmSC.descripcionInput,descripcion,tiempo)
      
   #Guardar

      fx.click("Guardar",By.XPATH,objHmSC.guardarBtn,tiempo)
      #agregar assert? se debe validar si se guardó o no?
      fx.softAssertTrue(fx.getText(By.XPATH,objHmSC.mensajeGuardar,tiempo),
                        "Última vez que se guardó","No se guardo el acuerdo","Se guardo solicitud: "+fx.getText(By.XPATH,objHmSC.horaGuardar,tiempo),tiempo)
   
   #tomar el numero del acuerdo en una variable para validar al finalizar con el mensaje
      numeroSolicitud=fx.getNumber(fx.getText(By.XPATH,objHmSC.numeroSolicitud,tiempo))
      print("Numero de solicitud: "+numeroSolicitud)
      #se guarda este dato en la dataTable
      xl.writeData(dataTable,hoja,"o_numeroSolicitud",numeroSolicitud)
      
   #Comprobar fondos
   
      fx.click("Comprobar fondos",By.XPATH,objHmSC.comprobarFondosBtn,tiempo)
      fx.click("Aceptar",By.XPATH,objHmSC.aprobacionAceptarBtn,3)
      fx.assertTrue(fx.getText(By.XPATH,objHmSC.estadoFondosMsj,tiempo),"Aprobada","Fallo la comprobacion de fondos")
      
   #Gestionar aprobaciones
      
      fx.click("Gestionar aprobaciones",By.XPATH,objHmSC.gestionarAprobacionBtn,tiempo)
      fx.click("Etapa",By.XPATH,objHmSC.etapaParticipante,tiempo)
      fx.click("Enviar",By.XPATH,objHmSC.enviarBtn,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objHmSC.confirmacionMsj,tiempo),"Se envió la solicitud "+numeroSolicitud+".","Error al enviar solicitud para su aprobacion")
      fx.click("Aceptar confirmacion",By.XPATH,objHmSC.confimacionAceptarBtn,tiempo)