from PyQt4.Qt import SIGNAL, SLOT, pyqtSlot, QTableWidgetItem, Qt, QIcon
from PyQt4.QtGui import QMainWindow
from threading import Timer

from Clases.downloadPage import DataProc
from Vistas.Ui_mainWindow import Ui_MainWindow
from Vistas.ayudaDialog import AyudaDialog
from Clases.profilePython import profilePython

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.actionDescargar, SIGNAL('triggered()'),SLOT('descargarDatos()'))
        self.connect(self.actionConfigurar, SIGNAL('triggered()'),SLOT('configurar()'))
        self.connect(self.actionActualizar, SIGNAL('triggered()'),SLOT('actualizar()'))
        self.connect(self.actionSalvar_Comp, SIGNAL('triggered()'),SLOT('salvarConfComp()'))
        self.connect(self.actionCrear_Archivo, SIGNAL('triggered()'),SLOT('crearArchivo()'))
        self.connect(self.actionDetener, SIGNAL('triggered()'),SLOT('actualizar(True)'))
        self.connect(self.actionAyuda, SIGNAL('triggered()'),SLOT('mostrarAyuda()'))
        self.connect(self.btnGuardarInfGeneral, SIGNAL('clicked()'),SLOT('guardarInfGeneral()'))
        self.connect(self.btnGuardarInfRed, SIGNAL('clicked()'),SLOT('guardarInfRed()'))
        self.connect(self.btnGuardarInfBD, SIGNAL('clicked()'),SLOT('guardarInfBD()'))
        self.connect(self.btnCancelarInfGeneral, SIGNAL('clicked()'),SLOT('actualizarVistaConfig()'))
        self.connect(self.btnCancelarInfBD, SIGNAL('clicked()'),SLOT('actualizarVistaConfig()'))
        self.connect(self.btnCancelarInfRed, SIGNAL('clicked()'),SLOT('actualizarVistaConfig()'))
        self.connect(self.tbCompeticion.selectionModel(), SIGNAL('selectionChanged(QItemSelection, QItemSelection)'),SLOT('actualizarJuegos()'))
        self.dockWConfig.setHidden(True)
        self.tbCompeticion.setColumnHidden(3,True)
        self.downloadP = DataProc()
        self.listaJuegos = []
        self.listaCompeticiones = []
        self.rowCompSelected = 0
        self.config = profilePython('../Recursos/config.INI')
        self.actualizarVistaConfig()
    
    @pyqtSlot()
    def salvarConfComp(self):
        #f = open(str(self.config.profile('INFO_GENERAL','DIRRECURSOS'))+'/config.INI','r')
        comp = ""
        trad = ""
        for i in range(self.tbCompeticion.rowCount()):
            if self.tbCompeticion.item(i,0).checkState() == Qt.Checked:
                comp+= self.tbCompeticion.item(i,1).text()+';'
                if self.tbCompeticion.item(i,2).text():
                    trad+= self.tbCompeticion.item(i,2).text()+';'
                else:
                    trad+= self.tbCompeticion.item(i,1).text()+';'
        self.config.set_profile('INFO_COMP','COMPONLINE',comp)
        self.config.set_profile('INFO_COMP','COMPTRADUC',trad)
        self.config.save_profile(False)   
    
    @pyqtSlot()       
    def actualizarVistaConfig(self):
        self.leditBDName.setText(str(self.config.profile('INFO_DB','DB')))
        self.leditBDHost.setText(str(self.config.profile('INFO_DB','HOST')))
        self.leditBDUser.setText(str(self.config.profile('INFO_DB','USER')))
        self.leditBDPass.setText(str(self.config.profile('INFO_DB','PASS')))
        self.leditBDPort.setText(str(self.config.profile('INFO_DB','PORT')))
        self.leditPxHost.setText(str(self.config.profile('INFO_PROXY','HOSTPROXY')))
        self.leditPxPass.setText(str(self.config.profile('INFO_PROXY','PASSPROXY')))
        self.leditPxPort.setText(str(self.config.profile('INFO_PROXY','PORTPROXY')))
        self.leditPxUser.setText(str(self.config.profile('INFO_PROXY','USERPROXY')))
        self.leditDirFichConf.setText(str(self.config.profile('INFO_GENERAL','DIRFICHEROCONF')))
        self.leditDirRecursos.setText(str(self.config.profile('INFO_GENERAL','DIRRECURSOS')))
        self.leditDirSalvaDatos.setText(str(self.config.profile('INFO_GENERAL','DIRFICHEROSDATOS')))
        self.leditTiempoAct.setText(str(self.config.profile('INFO_GENERAL','TIEMPOACT')))
        self.leditUrlFlags.setText(str(self.config.profile('INFO_GENERAL','URLFLAG')))
        self.leditUrlIndex.setText(str(self.config.profile('INFO_GENERAL','URLINDEX')))
    
    @pyqtSlot()
    def guardarInfGeneral(self):
        self.config.set_profile('INFO_GENERAL','URLINDEX',str(self.leditUrlIndex.text()))
        self.config.set_profile('INFO_GENERAL','URLFLAG',str(self.leditUrlFlags.text()))
        self.config.set_profile('INFO_GENERAL','DIRRECURSOS',str(self.leditDirRecursos.text()))
        self.config.set_profile('INFO_GENERAL','DIRFICHEROCONF',str(self.leditDirFichConf.text()))
        self.config.set_profile('INFO_GENERAL','DIRFICHEROSDATOS',str(self.leditDirSalvaDatos.text()))
        self.config.set_profile('INFO_GENERAL','TIEMPOACT',str(self.leditTiempoAct.text()))
        self.config.save_profile(False)
    @pyqtSlot()    
    def guardarInfRed(self):
        self.config.set_profile('INFO_PROXY','USERPROXY',str(self.leditPxUser.text()))
        self.config.set_profile('INFO_PROXY','PASSPROXY',str(self.leditPxPass.text()))
        self.config.set_profile('INFO_PROXY','HOSTPROXY',str(self.leditPxHost.text()))
        self.config.set_profile('INFO_PROXY','PORTPROXY',str(self.leditPxPort.text()))
        self.config.save_profile(False)
        
    @pyqtSlot()
    def guardarInfBD(self):
        self.config.set_profile('INFO_DB','DB',str(self.leditBDName.text()))
        self.config.set_profile('INFO_DB','USER',str(self.leditBDUser.text()))
        self.config.set_profile('INFO_DB','PASS',str(self.leditBDPass.text()))
        self.config.set_profile('INFO_DB','HOST',str(self.leditBDHost.text()))
        self.config.set_profile('INFO_DB','PORT',str(self.leditBDPort.text()))
        self.config.save_profile(False)
        
    @pyqtSlot()
    def mostrarAyuda(self):
        uiD = AyudaDialog(self)
        uiD.show()
     
    @pyqtSlot()
    def actualizar(self,stop = False):
            #Esperamos un ratito, o hasta que termine el hilo,
        self.descargarDatos()
        if not stop:
            t = Timer(60.0, self.actualizar)
            t.start()
            print "Actualizando Datos"
   
    @pyqtSlot()
    def detenerActualizacion(self):
        print "Trabajo" 
        
    @pyqtSlot()    
    def actualizarJuegos(self):
        cont = 0
        if self.tbCompeticion.currentItem():
            row = self.tbCompeticion.currentItem().row()
            idCompeticion = self.tbCompeticion.item(row, 3).text()
        else:
            row = 0
            idCompeticion = self.listaCompeticiones[0][0]
        
        self.tbJuegos.setRowCount(0)
        for k in self.listaJuegos:
            if k[19] == idCompeticion:
                self.tbJuegos.setRowCount(self.tbJuegos.rowCount()+1)
                itemHora = QTableWidgetItem()
                itemHora.setData(Qt.DisplayRole,k[5])
                self.tbJuegos.setItem(cont, 0,itemHora)
                itemTiempo = QTableWidgetItem()
                itemTiempo.setData(Qt.DisplayRole,k[7])
                self.tbJuegos.setItem(cont, 1,itemTiempo)
                itemEq1 = QTableWidgetItem()
                itemEq1.setData(Qt.DisplayRole,k[1])
                self.tbJuegos.setItem(cont, 2,itemEq1)  
                itemResult = QTableWidgetItem()
                cad = k[11]+':'+k[12]
                itemResult.setData(Qt.DisplayRole,cad)
                self.tbJuegos.setItem(cont, 3,itemResult)  
                itemEq2 = QTableWidgetItem()
                itemEq2.setData(Qt.DisplayRole,k[2])
                self.tbJuegos.setItem(cont, 4,itemEq2)
                cont += 1
    
    def getCompConfig(self):
        listaAux = []
        listaAuxT = []
        if (str(self.config.profile('INFO_COMP','COMPONLINE'))):
            listaAux = str(self.config.profile('INFO_COMP','COMPONLINE')).split(';')
            listaAuxT = str(self.config.profile('INFO_COMP','COMPTRADUC')).split(';')
        return listaAux, listaAuxT 
            
    def existComp(self,nombre):
        compConf,compConfT =  self.getCompConfig()
        cont = 0
        for k in compConf:
            if k == nombre:
                return compConfT[cont]
            cont += 1
        return False
    
    @pyqtSlot()    
    def actualizarCompeticiones(self):
        cont = 0
        self.tbCompeticion.setRowCount(0)
        for k in self.listaCompeticiones:
            self.tbCompeticion.setRowCount(self.tbCompeticion.rowCount()+1)
            nameFile = str(k[5])+'.png'
            dirIco = str(self.config.profile('INFO_GENERAL','DIRRECURSOS'))+'/flags/'+nameFile
            itemBandera = QTableWidgetItem(QIcon(dirIco),"",1)
            competicion = self.existComp(k[1])
            itemCompeticionT = QTableWidgetItem()
            if competicion:
                itemBandera.setCheckState(Qt.Checked)
                itemCompeticionT.setData(Qt.DisplayRole,competicion)
            else:
                itemBandera.setCheckState(Qt.Unchecked)
                itemCompeticionT.setData(Qt.DisplayRole,"")
            itemBandera.setData(Qt.DisplayRole,"")
            self.tbCompeticion.setItem(cont, 0,itemBandera)
            self.tbCompeticion.setItem(cont, 2,itemCompeticionT)
            itemCompeticion = QTableWidgetItem()
            itemCompeticion.setData(Qt.DisplayRole,k[1])
            self.tbCompeticion.setItem(cont, 1,itemCompeticion)  
            itemID = QTableWidgetItem()
            itemID.setData(Qt.DisplayRole,k[0])
            self.tbCompeticion.setItem(cont, 3,itemID) 
            cont += 1
        self.tbCompeticion.selectRow(self.rowCompSelected)
    
    @pyqtSlot()
    def descargarDatos(self):
        self.listaCompeticiones,self.listaJuegos = self.downloadP.downloadPage()
        if (self.tbCompeticion.currentItem()):
            self.rowCompSelected = self.tbCompeticion.currentItem().row()   
        else:
            self.rowCompSelected = 0
        self.actualizarCompeticiones()
        self.actualizarJuegos()
        
    @pyqtSlot()
    def configurar(self):
        self.dockWConfig.setHidden(False)
        
    @pyqtSlot()    
    def crearArchivo(self):
        cad = ""
        for i in range(self.tbCompeticion.rowCount()):
            if self.tbCompeticion.item(i,0).checkState() == Qt.Checked:
                if self.tbCompeticion.item(i,2).text()!="":
                    cad += self.tbCompeticion.item(i,2).text()+':  '
                else:
                    cad += self.tbCompeticion.item(i,1).text()+':  '
                idCompeticion = self.tbCompeticion.item(i,3).text() 
                for k in self.listaJuegos:
                    tiempo =""
                    result =""
                    if k[19] == idCompeticion:
                        if k[7] == '-1':
                            tiempo = k[5]
                            t = tiempo.split(':')
                            hora = int(t[0])-5
                            if (hora<0):
                                hora = 24 + hora
                            tiempo = str(hora) +":"+t[1]
                        else:
                            result = k[11] + '-'+ k[12]
                            if k[7].isdigit() and int(k[7])>0 and int(k[7])<=120:
                                tiempo = k[7] +"'"
                            else:
                                tiempo = k[7]
                        cad += k[1] +" vs "+ k[2] +"  "+tiempo+"  "+ result  +"   "
        
        f = open(str(self.config.profile('INFO_GENERAL','DIRFICHEROSDATOS'))+'livescoreFutbol.txt','w')
        f.write(cad)
        f.close()
        
        