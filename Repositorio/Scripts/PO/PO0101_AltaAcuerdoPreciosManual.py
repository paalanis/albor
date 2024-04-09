from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Objetos.Home import *
from Repositorio.Objetos.Compras.AcuerdoComprasHome import *
from Repositorio.Objetos.Compras.AcuerdoCompras import *



class PO0101():
   
   def __init__(self,driver):
      
      self.driver = driver

   def AltaAcuerdoPreciosManual(self,dataTable,tiempo):
       
      driver = self.driver
      
      #asignar variables de excel
      xl = Funexcel_pd(driver)
      
      hoja = "Sheet1"
      estilo = xl.readData(dataTable,hoja,"i_estilo",0)
      unidadDeNegocio = xl.readData(dataTable,hoja,"i_unidadDeNegocio",0)
      proveedor = xl.readData(dataTable,hoja,"i_proveedor",0)
      moneda = xl.readData(dataTable,hoja,"i_moneda",0)
      comprador = xl.readData(dataTable,hoja,"i_comprador",0)
      fechaIn = xl.readData(dataTable,hoja,"i_fechaInicio",0)
      fechaFin = xl.readData(dataTable,hoja,"i_fechaFin",0)
      importeAcuerdo = xl.readData(dataTable,hoja,"i_importeDelAcuerdo",0)
      descripcion = xl.readData(dataTable,hoja,"i_descripcion",0)
      condicionPago = xl.readData(dataTable,hoja,"i_condicionDePago",0)
      categoria = xl.readData(dataTable,hoja,"i_catergoria",0)
      subCategoria = xl.readData(dataTable,hoja,"i_subcategoria",0)
      articulo = xl.readData(dataTable,hoja,"i_articulo",0)
      notaAprobador = xl.readData(dataTable,hoja,"i_notaAprobador",0)
      
      fx = Funciones(driver)
      objHm = ObjHome
      objHmAC = ObjAcuerdoComprasHome
      objAC = ObjAcuerdoCompras
   
   
   #Ingresamos al home
   
      fx.click("Navegador",By.XPATH,objHm.navegador,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      fx.click("",By.XPATH,objHm.mostrarMasMenos,tiempo)
      
   #Crear acuerdo  
    
      fx.click("Compras",By.XPATH,objHm.menuComprasBtn,tiempo)
      fx.click("Acuerdos de compra",By.XPATH,objHm.acuerdoCompraBtn,tiempo)
      fx.click("Menú tareas",By.XPATH,objHmAC.menuTareasBtn,tiempo)
      fx.click("Crear acuerdo",By.XPATH,objHmAC.crearAcuerdoBtn,tiempo)
      fx.buscadorSelect(By.XPATH,objAC.estiloBuscarBtn,objAC.estiloBuscarLink,objAC.estiloInput,estilo,
                        objAC.estiloBuscarInterBtn,objAC.estiloResultado,objAC.estiloAceptarBtn,tiempo)
      fx.selectTexto("Unidad de negocio",By.XPATH,objAC.unidadDeNegocioSelect,unidadDeNegocio,tiempo)
      fx.buscadorLupa(By.XPATH,objAC.proveedorBuscarBtn,objAC.proveedorInput,proveedor,objAC.proveedorResultado,objAC.proveedorAceptarBtn,tiempo)
      fx.buscadorSelect(By.XPATH,objAC.monedaBuscarBtn,objAC.monedaBuscarLink,objAC.monedaInput,moneda,
                        objAC.monedaBuscarInterBtn,objAC.monedaResultado,objAC.monedaAceptarBtn,tiempo)
      fx.buscadorSelect(By.XPATH,objAC.compradorBuscarBtn,objAC.compradorBuscarLink,objAC.compradorInput,comprador,
                        objAC.compradorBuscarInterBtn,objAC.compradorResultado,objAC.compradorAceptarBtn,tiempo)
      fx.click("Crear",By.XPATH,objAC.crearBtn,tiempo)
      
   #Principal
            
      #tomar el numero del acuerdo en una variable para validar al finalizar con el mensaje
      numeroAcuerdo=fx.getNumber(fx.getText(By.XPATH,objAC.numeroAcuerdo,tiempo))
      print("Numero de acuerdo: "+numeroAcuerdo)
      #se guarda este dato en la dataTable
      xl.writeData(dataTable,hoja,"o_numeroAcuerdo",numeroAcuerdo)
      fx.click("Principal",By.XPATH,objAC.principalBtn,tiempo)
      fx.input("Fecha inicio",By.XPATH,objAC.fechaInicioInput,fechaIn,tiempo)
      fx.input("Importe de acuerdo",By.XPATH,objAC.importeAcuerdoInput,importeAcuerdo,tiempo)
      fx.input("Fecha finalizacion",By.XPATH,objAC.fechaFinInput,fechaFin,tiempo)
      fx.input("Descripcion",By.XPATH,objAC.descripcionInput,descripcion,tiempo)
      
   #Condiciones

      fx.click("Condiciones",By.XPATH,objAC.condicionesBtn,tiempo)
      fx.buscadorSelect(By.XPATH,objAC.condicionPagoBuscarBtn,objAC.condicionPagoBuscarLink,objAC.condicionPagoInput,condicionPago,
                        objAC.condicionPagoBuscarInterBtn,objAC.condicionPagoResultado,objAC.condicionPagoAceptarBtn,tiempo)
      
   #Controles
   
      fx.click("Controles",By.XPATH,objAC.controlesBtn,tiempo)
      fx.click("UnCheck Generar ordenes automaticamente",By.XPATH,objAC.generarOrdenesAutoCheck,tiempo)
      fx.click("Principal",By.XPATH,objAC.principalBtn,tiempo)
   
   #Lineas
   
      fx.click("Acciones",By.XPATH,objAC.accionesBtn,tiempo)
      fx.click("Agregar desde catalogo",By.XPATH,objAC.agregarDesdeCatalogoBtn,tiempo)
      
   #Catalogo

      fx.click("Comprar por categoria",By.XPATH,objAC.comprarPorCategoriaBtn,tiempo)
      fx.click("Categoria: "+categoria,By.XPATH,"//a[@class='xmv'][contains(.,'"+categoria+"')]",tiempo)
      fx.click("SubCategoria: "+subCategoria,By.XPATH,"//span[@class='xrs'][contains(.,'"+subCategoria+"')]",tiempo)
      fx.click("Articulo: "+articulo,By.XPATH,"//span[@class='x2vp'][contains(.,'"+articulo+"')]",tiempo)
      fx.click("Agregar a documento",By.XPATH,objAC.agregarADocumentoBtn,tiempo)
      fx.click("Completar",By.XPATH,objAC.completarBtn,tiempo)
   
   #Guardar

      fx.click("Guardar",By.XPATH,objAC.guardarBtn,tiempo)
      #agregar assert? se debe validar si se guardó o no?
      fx.softAssertTrue(fx.getText(By.XPATH,objAC.mensajeGuardar,tiempo),
                        "Última vez que se guardó","No se guardo el acuerdo","Se guardo acuerdo: "+fx.getText(By.XPATH,objAC.horaGuardar,tiempo),tiempo)
      
   #Gestionar aprobaciones
      
      fx.click("Gestionar aprobaciones",By.XPATH,objAC.gestionarAprobacionBtn,tiempo)
      fx.existeObjeto(By.XPATH,objAC.gestionarAprobacionTitulo,tiempo)
      fx.input("Nota al aprobador",By.XPATH,objAC.notaAprobadorInput,notaAprobador,tiempo)
      fx.click("Enviar",By.XPATH,objAC.enviarBtn,tiempo)
      fx.assertTrue(fx.getText(By.XPATH,objAC.confirmacionMsjTitulo,tiempo),"Confirmación","Error al enviar acuerdo para su aprobacion")
      fx.click("Aceptar confirmacion",By.XPATH,objAC.confimacionAceptarBtn,tiempo)