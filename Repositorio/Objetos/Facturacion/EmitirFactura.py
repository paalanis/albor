class ObjEmitirFactura():

    filtroBtn="//a[@id='filtros-std-toggle-collapse']//i"
    opcionesHomeTitulo="//h3[contains(.,'Opciones')]"
    nuevoComprobanteHome="//h1[contains(@id,'titpagina')]"
    nuevoBtn="//a[contains(@id,'btNuevoRegistro')]"
    
    pasoUno="//label[@class='control-label'][contains(.,'Tipo de Comprobante')]"
    tipoComprobanteSelect="//select[contains(@id,'ID_Tipo_Comprobante')]"
    fechaInput="//input[contains(@class,'fechaclass campo-requerido form-control hasDatepicker masked-date lib-visibilidad-mostrar')]"
    fechaInputWebService="//input[@class='form-control lib-visibilidad-mostrar config-SV terra-mask readonly'][contains(@id,'Comprobante')]"
    numeroFactura="//input[@class='form-control lib-visibilidad-mostrar config-SV terra-mask'][contains(@id,'Comprobante')]"
    clienteInput="//input[contains(@id,'ID_Tercero_Cliente_nombre')]"
    cuitClienteFiscal="//input[@id='ID_Tercero_Cliente_Fiscal_nombre']"
    jurisdiccionSelect="//select[@class='form-control lib-visibilidad-mostrar'][contains(@id,'Jurisdiccion')]"
    tipoVentaSelect="//select[contains(@id,'ID_Tipo_Venta')]"

    divContenedorBotones="//div[@id='contenedor-botones']"
    cancelarBtn="//input[contains(@id,'btCancelar')]"
    siguienteBtn="//input[contains(@id,'btSiguiente')]"

    pasoDos="//h4[contains(.,'Ítems')]"
    cosechaVtaBtn="//input[contains(@id,'btVinc_46')]"
    #nuevoItemBtn="(//span[contains(@class,'fa fa-plus')])[1]"
    nuevoItemBtn="//td[@class='ui-pg-button'][@id='btAdd_DetalleGrid']//span[@class='fa fa-plus']"
    modal="//div[@id='dialog']"
    tipoItemModal="//label[@class='control-label'][contains(.,'Tipo de ítem')]"
    tipoItem="//select[contains(@id,'Comprobante')][@name='ID_IT_Tipo_Comprobante']"
    descripcionLabel="//label[@class='control-label'][contains(.,'Descripción')]"
    descripcionInput="//input[contains(@class,'nombre-descriptivo long-text form-control lib-visibilidad-mostrar config-SV')]"
    unidadesInput="//input[contains(@class,'oculto-guardable form-control cantidad formateado-autonumeric lib-visibilidad-mostrar config-SV')]"
    ivaSelect="//select[@id='IVA']"
    netoGravadoInput="//input[@id='NG']"
    cuentaContableInput="(//input[@type='text'][contains(@id,'codigo')])[7]"
    centroCostoSelect="(//select[@class='campo-requerido combo-detail form-control'][contains(@id,'2')])[1]"
    aceptarBtn="//button[@id='btAceptar_dialog']"
    estadoGrilla="//div[@id='cont-dimensiones']"

    pasoTres="//h4[contains(.,'Vencimientos')]"

    pasoCuatro="//h4[contains(@id,'titulo-asiento')]"
    finalizarBtn="//input[contains(@id,'btFinalizar')]"
    finalizarOtroBtn="//input[contains(@id,'btGuardarYOtro')]"
    totalNoGravado="//input[contains(@id,'Total_NG')]"
    totalIva21="//input[contains(@id,'Total_IVA21')]"
    totalIva105="//input[contains(@id,'Total_IVA105')]"
    totalExento="//input[contains(@id,'Total_EX')]"
    totalFactura="(//input[@id='Importe_Total'])[1]"

    numeroAsiento="//span[contains(@id,'ref-comprobante-automatico')]"

    #Dercargar facturas
    fechaDesdeInput="//input[contains(@id,'FechaDesde')]"
    fechaHastaInput="//input[contains(@id,'FechaHasta')]"
    filtroNumeroComprobanteInput="//input[contains(@id,'gs_Numero_Comprobante')]"
    filaResultado="//tr[@class='jqgrow ui-row-ltr']//td[contains(.,'0010-00000001')]"
    reporteDetalladoBtn="//a[@href='javascript:abrirReporte_VE()'][contains(.,'Reporte Detallado')]"
    tituloReporteDetallado="//span[contains(@class,'ui-dialog-title')]"

    loading="(//span[contains(.,'Loading...')])[2]"
    hojaInput="//input[contains(@id,'visorReporte_ctl05_ctl03_ctl00')]"
    #modalFactura="//iframe[@id='iframeReporte']"
    modalFactura="iframeReporte"

    guardarBtn="//a[@id='visorReporte_ctl05_ctl04_ctl00_ButtonLink']"
    opcionPdf="//a[@title='PDF'][contains(.,'PDF')]"
    cerrarBtn="//button[contains(@class,'ui-dialog-titlebar-close')]"