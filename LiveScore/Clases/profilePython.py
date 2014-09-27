import os
import time

class profilePython(object):
    '''
    Clase que implementa el mecanismo de utilizacion de ficheros
    de configuracion.
    '''
    def __init__(self, filename):
        '''Inicializacion.'''
        self.__fichero = filename
        self.__lineas_fichero = []
        self.__cargar_fichero()
    
    def __esvacio(self,cadena):
        '''
        Metodo que devuelve True si la cadena pasada como parametro
        esta vacia y False en caso contrario.
        '''
        if cadena is None: return True
        try:
            if len(str(cadena)) == 0: return True
        except:
            pass
        return False
  
    def __cargar_fichero(self):
        '''
        Carga del fichero en memoria.
        '''
        try:
            # Abrimos el fichero.
            fichero = open(os.path.realpath(self.__fichero),'r')
            seguir = True
        except:
            seguir = False
        if seguir:
            # Volcamos el contenido del fichero a una estructura.
            while True:
                f = fichero.readline()
                if not f: break
                if not self.__esvacio(f):
                    # Quitamos retornos de carro y demas.
                    f = f.replace("\n","")
                    f = f.replace("\r","")
                    f = f.strip()
                    # Lo anadimos a la lista de lineas.
                    self.__lineas_fichero.append(f)
            # Cerramos el fichero.
            fichero.close()
  
    def __posicionar(self, seccion, clave = None):
        '''
        Metodo para posicionarse en la seccion, clave (opcional).
        Devuelve True, posicion de la clave (si encuentra la clave).
        Devuelve True, posicion de la seccion (si encuentra seccion y clave  None)
        Devuelve False, -1 (si no encuentra seccion).
        Devuelve False, posicion de la seccion (si no encuentra clave).
        '''    
        # Buscamos la seccion
        encontrado = False
        puntero = 0
        for i in self.__lineas_fichero:
            puntero += 1
            if i.strip() == '['+str(seccion)+']':
                encontrado = True
                break
        if not encontrado: return False, -1
        if clave is not None:
            # Buscamos la clave.
            encontrado = False
            for i in range(puntero,len(self.__lineas_fichero)):
                # Buscamos el caracter '='.
                linea = self.__lineas_fichero[i].split('=')
                if len(linea) == 1:
                    # Nos vamos. La clave no esta en esta seccion.
                    break
                if len(linea) == 2:
                    # Miramos si es lo que buscamos.
                    if str(linea[0]).strip() == str(clave).strip():
                        # Devolvemos posicion.
                        return True, i
            # La clave no existe. Devolvemos posicion de la seccion.
            return False, puntero
        else:
            # Devolvemos la posicion de la seccion.
            return True, puntero
      
    def profile(self, seccion, clave, por_defecto = None):
        '''
        Metodo para obtener valor de clave en seccion.
        '''
        # La seccion y clave no pueden estar vacios.
        if self.__esvacio(seccion) or self.__esvacio(clave): return por_defecto
        # Buscamos la clave.
        seguir, posicion = self.__posicionar(seccion, clave)
        if seguir:
            # Obtenemos el valor de la clave.
            linea = self.__lineas_fichero[posicion].split('=')
            try:
                return str(linea[1]).strip()
            except:
                return por_defecto
        else: return por_defecto
      
    def set_profile(self, seccion, clave = None, valor = None):
        '''
        Metodo para crear secciones y claves (y darles valores).
        '''
        # Si no hay seccion, nos vamos.
        if self.__esvacio(seccion): return
        # Incluimos una seccion.
        # Si la seccion no existe, se crea.
        seguir, posicion = self.__posicionar(seccion)
        if not seguir:
            self.__lineas_fichero.append('['+str(seccion).strip()+']')
        # Asignamos o incluimos si no existe, el valor
        # de una clave a una seccion.
        if not self.__esvacio(clave):
            # Vemos si la (seccion,clave) ya existe.
            seguir, posicion = self.__posicionar(seccion,clave)
        # Formateamos valor.
            if valor is None: valor = ''
            # Si existe, damos nuevo valor.
            if seguir:
                self.__lineas_fichero[posicion] = str(clave).strip()+' = '+\
                str(valor).strip()
            else:
                # Si no existe, creamos una nueva clave con su valor.
                if posicion != -1:
                    # Insertamos nueva clave
                    clave_valor = str(clave).strip()+' = '+str(valor).strip()
                    self.__lineas_fichero.insert(posicion,clave_valor)

    def save_profile(self, backup = True):
        '''
        Metodo para salvar datos en fichero profile. Si backup es True
        se crea una copia de seguridad del mismo. Devuelve True si se
        guardo el fichero y False en caso contrario.
        '''
        # Formamos etiqueta identificacion.
        etiqueta = '_backup_'+str(time.time()).strip()
        try:
            if backup:
                # Renombramos fichero.
                os.rename(os.path.realpath(self.__fichero),\
                self.__fichero+etiqueta)
        except: pass
        ret = True
        try:
            # Creamos fichero.
            fichero = open(os.path.realpath(self.__fichero),'w')
            # Guardamos cada una de las lineas.
            for i in self.__lineas_fichero:
                linea = str(i) + '\r\n'
                fichero.write(linea)
            # Cerramos fichero.
            fichero.close()
        except: ret = False
        # Devolvemos estado.
        return ret
