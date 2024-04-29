from Repositorio.Scripts.ExcelPandas import *
from Repositorio.Funciones.Funciones import *
from Repositorio.Funciones.Menu.Menu import *
from Repositorio.Objetos.Home import *
from Repositorio.Objetos.Facturacion.EmitirFactura import *

class EmitirFactura():
   
   def __init__(self,driver):
      
      self.driver = driver

   def emitirFactura(self,dataTable,tiempo):
      
      driver = self.driver
      
   #Llamamos a la plantilla de excel con los datos de prueba   
      xl = Funexcel_pd(driver)
      
   #datos generales factura
      hojaGeneral = "general"
      filasHojaGeneral = xl.numRow(dataTable,hojaGeneral)      
   
   #datos items factura
      hojaConceptoVariable = "conceptoVariable"
      hojaConceptoFijo = "conceptoFijo"
      hojaConceptoMovilidad = "conceptoMovilidad"
      hojaConceptoRecuperos = "conceptoRecuperos"
      hojaConceptoAnticipos = "conceptoAnticipos"
      
   #Instanciamos variables   
      fx = Funciones(driver)
      menu = Menu(driver)
      objFa = ObjEmitirFactura
      objHm = ObjHome      
      
   #Navegador

      fx.click("Navegador",By.XPATH,objHm.navigator,tiempo)

      menu.clickOpcionMenu(objHm.menuComprobanteVenta,1)

      for j in range(0,filasHojaGeneral):

         fx.scroll(0,250,tiempo)         
         fx.click("Nueva factura",By.XPATH,objFa.nuevoBtn,tiempo)

         #datos generales factura
         tipoFactura = xl.readData(dataTable,hojaGeneral,"i_tipoFactura",j)
         fecha = xl.readData(dataTable,hojaGeneral,"i_fecha",j)
         numeroFactura = xl.readData(dataTable,hojaGeneral,"i_numeroFactura",j)
         cliente = xl.readData(dataTable,hojaGeneral,"i_cliente",j)
         jurisdiccion = xl.readData(dataTable,hojaGeneral,"i_jurisdiccion",j)
         tipoVenta = xl.readData(dataTable,hojaGeneral,"i_tipoVenta",j)
         
      #Paso uno --------------------------------------------------------------------------------------------------------------------------------
         fx.existeObjeto(By.XPATH,objFa.pasoUno,tiempo)
         fx.selectTexto("Tipo comprobante",By.XPATH,objFa.tipoComprobanteSelect,tipoFactura,tiempo)
         fx.existeObjeto(By.XPATH,objFa.fechaInput,tiempo)
         fx.click("Click fecha",By.XPATH,objFa.fechaInput,tiempo)
         fx.input("Fecha",By.XPATH,objFa.fechaInput,fecha,tiempo)
         fx.click("Click factura",By.XPATH,objFa.numeroFactura,tiempo)
         fx.input("Numero factura",By.XPATH,objFa.numeroFactura,numeroFactura,tiempo)
         fx.buscar("Cliente",By.XPATH,objFa.clienteInput,cliente,tiempo)
         fx.selectTexto("Jurisdiccion",By.XPATH,objFa.jurisdiccionSelect,jurisdiccion,tiempo)
         fx.selectTexto("Tipo venta",By.XPATH,objFa.tipoVentaSelect,tipoVenta,tiempo)               

         clienteFiscal=fx.getValue(By.XPATH,objFa.cuitClienteFiscal,tiempo)
         while clienteFiscal != cliente:
            clienteFiscal=fx.getValue(By.XPATH,objFa.cuitClienteFiscal,tiempo)
         fx.click("Siguiente",By.XPATH,objFa.siguienteBtn,tiempo)
      
      #Paso dos --------------------------------------------------------------------------------------------------------------------------------
         fx.existeObjeto(By.XPATH,objFa.pasoDos,tiempo)
         
         #CONCEPTO FIJO
         listaFijos = xl.buscarValor(dataTable,hojaConceptoFijo,"t_cliente","i_finca",cliente)
         indexFijos = listaFijos.index
            
         for i in range(0,len(indexFijos)):
            #print(indexFijos)
            #print("largo: "+str(len(indexFijos))+"_ I: "+str(i))
            if (len(indexFijos) != i):
               fx.scroll(0,100,tiempo)
               fx.click("Fijo-Nuevo item",By.XPATH,objFa.nuevoItemBtn,tiempo)

            tipoItem = xl.readData(dataTable,hojaConceptoFijo,"i_tipoItem",indexFijos[i])
            descripcion = xl.readData(dataTable,hojaConceptoFijo,"i_descripcion",indexFijos[i])+"-"+xl.readData(dataTable,hojaGeneral,"i_mesFacturacion",0)+" "+xl.readData(dataTable,hojaConceptoFijo,"i_finca",indexFijos[i]).upper()
            unidades = xl.readData(dataTable,hojaConceptoFijo,"i_unidades",indexFijos[i])
            iva = xl.buscarValor(dataTable,"Traductor_iva","t_alicuota","i_iva",xl.readData(dataTable,hojaConceptoFijo,"t_alicuota",indexFijos[i]))
            for k, v in iva.items():
               iva = v
            netoGravado = xl.readData(dataTable,hojaConceptoFijo,"i_netoGravado",indexFijos[i])
            cuentaContable = xl.readData(dataTable,hojaConceptoFijo,"i_cuentaContable",indexFijos[i])
            centroCosto = xl.buscarValor(dataTable,"Traductor_centroCosto","t_centroCosto","i_centroCosto",xl.readData(dataTable,hojaConceptoFijo,"t_centroCosto",indexFijos[i]))
            for k, v in centroCosto.items():
               centroCosto = v
            
            fx.existeObjeto(By.XPATH,objFa.tipoItemModal,tiempo)
            fx.selectTexto("Fijo-Item",By.XPATH,objFa.tipoItem,tipoItem,tiempo)
            fx.existeObjeto(By.XPATH,objFa.descripcionLabel,tiempo)
            fx.input("Fijo-Descripcion",By.XPATH,objFa.descripcionInput,descripcion,tiempo)
            fx.input("Fijo-Unidad",By.XPATH,objFa.unidadesInput,unidades,tiempo)
            fx.input("Fijo-Gravado",By.XPATH,objFa.netoGravadoInput,netoGravado,tiempo)
            fx.selectTexto("Fijo-Iva",By.XPATH,objFa.ivaSelect,iva,tiempo)
            fx.buscar("Fijo-Cuenta contable",By.XPATH,objFa.cuentaContableInput,cuentaContable,5)
            
            textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)
            while textoCentroCosto == "":
               print("Entro centro de costo: "+textoCentroCosto)             
               fx.selectTexto("Fijo-Centro costo",By.XPATH,objFa.centroCostoSelect,centroCosto,tiempo)
               textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)             

            fx.click("Fijo-Aceptar",By.XPATH,objFa.aceptarBtn,tiempo)


         #CONCEPTO VARIABLE
         listaVariables = xl.buscarValor(dataTable,hojaConceptoVariable,"t_cliente","i_finca",cliente)
         indexVariables = listaVariables.index
         
         for i in range(0,len(indexVariables)):
            #print("largo: "+str(len(indexVariables))+"_ I: "+str(i))
            if (len(indexVariables) != i):
               fx.scroll(0,100,tiempo)
               fx.click("Variable-Nuevo item",By.XPATH,objFa.nuevoItemBtn,tiempo)

            tipoItem = xl.readData(dataTable,hojaConceptoVariable,"i_tipoItem",indexVariables[i])
            descripcion = xl.readData(dataTable,hojaConceptoVariable,"i_descripcion",indexVariables[i])+"-"+xl.readData(dataTable,hojaGeneral,"i_mesFacturacion",0)+" "+xl.readData(dataTable,hojaConceptoVariable,"i_finca",indexVariables[i]).upper()
            unidades = xl.readData(dataTable,hojaConceptoVariable,"i_unidades",indexVariables[i])
            iva = xl.buscarValor(dataTable,"Traductor_iva","t_alicuota","i_iva",xl.readData(dataTable,hojaConceptoVariable,"t_alicuota",indexVariables[i]))
            for k, v in iva.items():
               iva = v
            netoGravado = xl.readData(dataTable,hojaConceptoVariable,"i_netoGravado",indexVariables[i])
            cuentaContable = xl.readData(dataTable,hojaConceptoVariable,"i_cuentaContable",indexVariables[i])
            centroCosto = xl.buscarValor(dataTable,"Traductor_centroCosto","t_centroCosto","i_centroCosto",xl.readData(dataTable,hojaConceptoVariable,"t_centroCosto",indexVariables[i]))
            for k, v in centroCosto.items():
               centroCosto = v   

            fx.existeObjeto(By.XPATH,objFa.tipoItemModal,tiempo)
            fx.selectTexto("Variable-Item",By.XPATH,objFa.tipoItem,tipoItem,tiempo)
            fx.existeObjeto(By.XPATH,objFa.descripcionLabel,tiempo)
            fx.input("Variable-Descripcion",By.XPATH,objFa.descripcionInput,descripcion,tiempo)
            fx.input("Variable-Unidad",By.XPATH,objFa.unidadesInput,unidades,tiempo)
            fx.input("Variable-Gravado",By.XPATH,objFa.netoGravadoInput,netoGravado,tiempo)
            fx.selectTexto("Variable-Iva",By.XPATH,objFa.ivaSelect,iva,tiempo)
            fx.buscar("Variable-Cuenta contable",By.XPATH,objFa.cuentaContableInput,cuentaContable,5)
            
            textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)
            while textoCentroCosto == "":
               print("Esperando centro de costo: "+textoCentroCosto)
               fx.selectTexto("Fijo-Centro costo",By.XPATH,objFa.centroCostoSelect,centroCosto,tiempo)
               textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)

            fx.click("Variable-Aceptar",By.XPATH,objFa.aceptarBtn,tiempo)
            
                     
         #CONCEPTO MOVILIDAD
         listaRecuperos = xl.buscarValor(dataTable,hojaConceptoRecuperos,"t_cliente","t_cliente",cliente)
         indexRecuperos = listaRecuperos.index
         
         for i in range(0,len(indexRecuperos)):
            #print("largo: "+str(len(indexRecuperos))+"_ I: "+str(i))
            if (len(indexRecuperos) != i):
               fx.scroll(0,100,tiempo)
               fx.click("Recuperos-Nuevo item",By.XPATH,objFa.nuevoItemBtn,tiempo)

            tipoItem = xl.readData(dataTable,hojaConceptoRecuperos,"i_tipoItem",indexRecuperos[i])
            descripcion = xl.readData(dataTable,hojaConceptoRecuperos,"i_descripcion",indexRecuperos[i])+"-"+xl.readData(dataTable,hojaGeneral,"i_mesFacturacion",0)
            unidades = xl.readData(dataTable,hojaConceptoRecuperos,"i_unidades",indexRecuperos[i])
            iva = xl.readData(dataTable,hojaConceptoRecuperos,"i_alicuota",indexRecuperos[i])
            netoGravado = xl.readData(dataTable,hojaConceptoRecuperos,"i_netoGravado",indexRecuperos[i])
            cuentaContable = xl.readData(dataTable,hojaConceptoRecuperos,"i_cuentaContable",indexRecuperos[i])
            centroCosto = xl.readData(dataTable,hojaConceptoRecuperos,"i_centroCosto",indexRecuperos[i])


            fx.existeObjeto(By.XPATH,objFa.tipoItemModal,tiempo)
            fx.selectTexto("Recuperos-Item",By.XPATH,objFa.tipoItem,tipoItem,tiempo)
            fx.existeObjeto(By.XPATH,objFa.descripcionLabel,tiempo)
            fx.input("Recuperos-Descripcion",By.XPATH,objFa.descripcionInput,descripcion,tiempo)
            fx.input("Recuperos-Unidad",By.XPATH,objFa.unidadesInput,unidades,tiempo)
            fx.input("Recuperos-Gravado",By.XPATH,objFa.netoGravadoInput,netoGravado,tiempo)
            fx.selectTexto("Recuperos-Iva",By.XPATH,objFa.ivaSelect,iva,tiempo)
            fx.buscar("Recuperos-Cuenta contable",By.XPATH,objFa.cuentaContableInput,cuentaContable,5)
            
            textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)
            while textoCentroCosto == "":
               print("Esperando centro de costo: "+textoCentroCosto)
               fx.selectTexto("Fijo-Centro costo",By.XPATH,objFa.centroCostoSelect,centroCosto,tiempo)
               textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)

            fx.click("Recuperos-Aceptar",By.XPATH,objFa.aceptarBtn,tiempo)


         #CONCEPTO RECUPEROS   
         listaMovilidad = xl.buscarValor(dataTable,hojaConceptoMovilidad,"t_cliente","t_cliente",cliente)
         indexMovilidad = listaMovilidad.index
         
         for i in range(0,len(indexMovilidad)):
            #print("largo: "+str(len(indexMovilidad))+"_ I: "+str(i))
            if (len(indexMovilidad) != i):
               fx.scroll(0,100,tiempo)
               fx.click("Movilidad-Nuevo item",By.XPATH,objFa.nuevoItemBtn,tiempo)

            tipoItem = xl.readData(dataTable,hojaConceptoMovilidad,"i_tipoItem",indexMovilidad[i])
            descripcion = xl.readData(dataTable,hojaConceptoMovilidad,"i_descripcion",indexMovilidad[i])+"-"+xl.readData(dataTable,hojaGeneral,"i_mesFacturacion",0)
            unidades = xl.readData(dataTable,hojaConceptoMovilidad,"i_unidades",indexMovilidad[i])
            iva = xl.readData(dataTable,hojaConceptoMovilidad,"i_alicuota",indexMovilidad[i])
            netoGravado = xl.readData(dataTable,hojaConceptoMovilidad,"i_netoGravado",indexMovilidad[i])
            cuentaContable = xl.readData(dataTable,hojaConceptoMovilidad,"i_cuentaContable",indexMovilidad[i])
            centroCosto = xl.readData(dataTable,hojaConceptoMovilidad,"i_centroCosto",indexMovilidad[i])


            fx.existeObjeto(By.XPATH,objFa.tipoItemModal,tiempo)
            fx.selectTexto("Movilidad-Item",By.XPATH,objFa.tipoItem,tipoItem,tiempo)
            fx.existeObjeto(By.XPATH,objFa.descripcionLabel,tiempo)
            fx.input("Movilidad-Descripcion",By.XPATH,objFa.descripcionInput,descripcion,tiempo)
            fx.input("Movilidad-Unidad",By.XPATH,objFa.unidadesInput,unidades,tiempo)
            fx.input("Movilidad-Gravado",By.XPATH,objFa.netoGravadoInput,netoGravado,tiempo)
            fx.selectTexto("Movilidad-Iva",By.XPATH,objFa.ivaSelect,iva,tiempo)
            fx.buscar("Movilidad-Cuenta contable",By.XPATH,objFa.cuentaContableInput,cuentaContable,5)

            textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)
            while textoCentroCosto == "":
               print("Esperando centro de costo: "+textoCentroCosto)
               fx.selectTexto("Fijo-Centro costo",By.XPATH,objFa.centroCostoSelect,centroCosto,tiempo)
               textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)

            fx.click("Movilidad-Aceptar",By.XPATH,objFa.aceptarBtn,tiempo)


         #CONCEPTO ANTICIPOS 
         listaAnticipos = xl.buscarValor(dataTable,hojaConceptoAnticipos,"t_cliente","t_cliente",cliente)
         indexAnticipos = listaAnticipos.index
         
         for i in range(0,len(indexAnticipos)):
            #print("largo: "+str(len(indexAnticipos))+"_ I: "+str(i))
            if (len(indexAnticipos) != i):
               fx.scroll(0,100,tiempo)
               fx.click("Anticipos-Nuevo item",By.XPATH,objFa.nuevoItemBtn,tiempo)

            tipoItem = xl.readData(dataTable,hojaConceptoAnticipos,"i_tipoItem",indexAnticipos[i])
            descripcion = xl.readData(dataTable,hojaConceptoAnticipos,"i_descripcion",indexAnticipos[i])+" "+xl.readData(dataTable,hojaGeneral,"i_mesFacturacion",0)
            unidades = xl.readData(dataTable,hojaConceptoAnticipos,"i_unidades",indexAnticipos[i])
            iva = xl.readData(dataTable,hojaConceptoAnticipos,"i_alicuota",indexAnticipos[i])
            netoGravado = xl.readData(dataTable,hojaConceptoAnticipos,"i_netoGravado",indexAnticipos[i])
            cuentaContable = xl.readData(dataTable,hojaConceptoAnticipos,"i_cuentaContable",indexAnticipos[i])
            centroCosto = xl.readData(dataTable,hojaConceptoAnticipos,"i_centroCosto",indexAnticipos[i])


            fx.existeObjeto(By.XPATH,objFa.tipoItemModal,tiempo)
            fx.selectTexto("Anticipos-Item",By.XPATH,objFa.tipoItem,tipoItem,tiempo)
            fx.existeObjeto(By.XPATH,objFa.descripcionLabel,tiempo)
            fx.input("Anticipos-Descripcion",By.XPATH,objFa.descripcionInput,descripcion,tiempo)
            fx.input("Anticipos-Unidad",By.XPATH,objFa.unidadesInput,unidades,tiempo)
            fx.input("Anticipos-Gravado",By.XPATH,objFa.netoGravadoInput,netoGravado,tiempo)
            fx.selectTexto("Anticipos-Iva",By.XPATH,objFa.ivaSelect,iva,tiempo)
            fx.buscar("Anticipos-Cuenta contable",By.XPATH,objFa.cuentaContableInput,cuentaContable,5)
            
            textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)
            while textoCentroCosto == "":
               print("Esperando centro de costo: "+textoCentroCosto)
               fx.selectTexto("Fijo-Centro costo",By.XPATH,objFa.centroCostoSelect,centroCosto,tiempo)
               textoCentroCosto = fx.getValue(By.XPATH,objFa.centroCostoSelect,tiempo)

            fx.click("Anticipos-Aceptar",By.XPATH,objFa.aceptarBtn,tiempo)

         totalFactura = fx.getValue(By.XPATH,objFa.totalFactura,tiempo)
         totalFactura = totalFactura.replace('.', '')
         totalFactura = totalFactura[:-3]

         totalFacturaControl = xl.readData(dataTable,hojaGeneral,"i_montoControl",j)
         print("total factura: "+totalFactura)
         print("total control: "+str(totalFacturaControl))

         if not fx.softAssertTrue(totalFactura,totalFacturaControl,"Error al facturar - El total de la factura no coincide con el total de control - Cliente: "+cliente,"total control: "+str(totalFacturaControl)+" - total factura: "+totalFactura,tiempo):
             xl.writeData(dataTable,hojaGeneral,"o_asiento","Error",j)
             xl.writeData(dataTable,hojaGeneral,"o_montoFacturado",totalFactura,j)
             botonesOculto = fx.styleObjeto(By.XPATH,objFa.divContenedorBotones,"overflow",tiempo)
             while botonesOculto == "hidden":
               print("Esperando se habilite el botón cancelar")
               botonesOculto = fx.styleObjeto(By.XPATH,objFa.divContenedorBotones,"overflow",tiempo)             
             fx.click("Cancelar",By.XPATH,objFa.cancelarBtn,tiempo)             
             continue

         botonesOculto = fx.styleObjeto(By.XPATH,objFa.divContenedorBotones,"overflow",tiempo)
         while botonesOculto == "hidden":
            print("Esperando se habilite el botón siguiente")
            botonesOculto = fx.styleObjeto(By.XPATH,objFa.divContenedorBotones,"overflow",tiempo)
         fx.click("Siguiente",By.XPATH,objFa.siguienteBtn,tiempo)

      #Paso tres --------------------------------------------------------------------------------------------------------------------------------

         fx.existeObjeto(By.XPATH,objFa.pasoTres,tiempo)
         botonesOculto = fx.styleObjeto(By.XPATH,objFa.divContenedorBotones,"overflow",tiempo)
         while botonesOculto == "hidden":
            print("Esperando se habilite el botón siguiente")
            botonesOculto = fx.styleObjeto(By.XPATH,objFa.divContenedorBotones,"overflow",tiempo)
         fx.click("Siguiente",By.XPATH,objFa.siguienteBtn,tiempo)

      #Paso cuatro ------------------------------------------------------------------------------------------------------------------------------

         fx.existeObjeto(By.XPATH,objFa.pasoCuatro,tiempo)
         botonesOculto = fx.styleObjeto(By.XPATH,objFa.divContenedorBotones,"overflow",tiempo)
         while botonesOculto == "hidden":
            print("Esperando se habilite el botón finalizar")
            botonesOculto = fx.styleObjeto(By.XPATH,objFa.divContenedorBotones,"overflow",tiempo)
         fx.click("Finalizar",By.XPATH,objFa.finalizarBtn,tiempo)

         fx.existeObjeto(By.XPATH,objFa.nuevoComprobanteHome,tiempo)
         asiento=fx.getText(By.XPATH,objFa.numeroAsiento,tiempo)
         print(str(asiento))
         xl.writeData(dataTable,hojaGeneral,"o_asiento",asiento,j)