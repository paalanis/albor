import pandas as pd
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None

class Funexcel_pd():
    def __init__(self, driver):
        self.driver = driver
        
    def readData(self,path,sheet,header,row):
        '''Función que devuelve un valor de una celda dentro de una hoja de excel específica, según el nombre de la título de la columna y el número de fila indicados.
        Argumentos:\n
        path: ubicación del arcrivo de excel.\n
        sheet: hoja del arcrivo de excel.\n
        header: nombre del encabezado de la columna.\n
        row: fila donde se encuentran los datos. Primera fila de datos 0.
        '''
        data = pd.read_excel(path,sheet,dtype=object)
        val = data[header].values[row]    
        return val
    
    def writeData(self,path,sheet,header,dato,row):
        '''Función que inserta el dato indicado en una hoja de excel específica, según el nombre de la título de la columna y el número de fila indicados.
        Argumentos:\n
        path: ubicación del arcrivo de excel.\n
        sheet: hoja del arcrivo de excel.\n
        header: nombre del encabezado de la columna.\n
        dato: valor a ingresar en la celda.
        '''
        df = pd.read_excel(path,sheet,dtype=object)
        df.at[row,header]=dato
        with pd.ExcelWriter(path,mode="a",if_sheet_exists="overlay") as writer:            
            df.to_excel(writer,sheet_name=sheet,index=False) 
        
    def buscarValor(self,path,sheet,headerBuscado,headerResultado,valorBuscado):
        '''Función que busca el "valorBuscado" dentro de una matriz de datos en una hoja de excel específica. Indicar columna del valor a buscar y columna del resultado. Estas se indican con el título.
        Argumentos:\n
        path: ubicación del arcrivo de excel.\n
        sheet: hoja del arcrivo de excel.\n
        headerBuscado: nombre del encabezado de la columna del dato a buscar.\n
        headerResultado: nombre del encabezado de la columna resultado.\n
        valorBuscado: dato a buscar
        '''
        data = pd.read_excel(path,sheet,dtype=object)
        df = pd.DataFrame(data)
        df
        resultado = df[df[headerBuscado]==valorBuscado][headerResultado]
        #resultado=resultado.index
        return resultado
    
    def numRow(self,path,sheet):
        '''Función que devuelve un la cantidad de filas de una hoja de excel específica, sin tener tener en cuenta los títulos.
        Argumentos:\n
        path: ubicación del arcrivo de excel.\n
        sheet: hoja del arcrivo de excel.
        '''
        data = pd.read_excel(path,sheet,dtype=object)
        df = pd.DataFrame(data)
        rows = df.shape[0]
        return rows