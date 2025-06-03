class ObjHome():
    
    titulo="albor Campo - Bienvenido a albor Campo"
    
#pagina inicio

    logoAlbor="//img[@src='/Content/albor/imagenes/logo-encabezado-menu-overlay.png']"
    #nombreUserEmpresa="//div[@class='user-account-btn dropdown']//a[@class='user-profile clearfix enterleave']"
    nombreUserEmpresa="//div[@class='user-account-btn dropdown']//div[@class='flex-container']"
    navigator="//i[contains(@class,'fa fa-bars')]"

#menu dentro de navigator
#_________________________________________________________________

    buscadorMenuInput="//input[contains(@id,'BusquedaMenu')]"
    
    #Esta es un objeto dinámico, se encuentra dentro de la funcion Menu.
    #opcionesMenuBtn="//ul[@id='resultados-busqueda']//a[contains(@href,'/Comprobantes')]//span[@class='nav-label'][contains(.,'Comprobantes de Venta')]"

    menuComprobanteVenta="Comprobantes de Venta"

