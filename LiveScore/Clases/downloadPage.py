import urllib

from Clases.profilePython import profilePython
from connect import Connect


class DataProc(object):
	def __init__ ( self, parent = None ):				
		self.config = profilePython('../Recursos/config.INI')
		self.dirPage = str(self.config.profile('INFO_GENERAL','URLINDEX'))
		self.proxies = {'http': 'http://'+str(self.config.profile('INFO_PROXY','USERPROXY'))+':'+str(self.config.profile('INFO_PROXY','PASSPROXY'))+'@'+str(self.config.profile('INFO_PROXY','HOSTPROXY'))+':'+str(self.config.profile('INFO_PROXY','PORTPROXY'))}
	
	def  downloadPage(self):	
		# Get a file-like object for the Python Web site's home page.
		page = urllib.urlopen(self.dirPage,proxies=self.proxies)
		#page = urllib.urlopen(self.dirPage)
		# Read from the object, storing the page's contents in 's'.
		textPage = page.read()
		#textPage = 'xcomp[1]=Array(102,"INTERNATIONAL FRIENDLIES","2015-04-03",1,"",2001,1547,"EUROPA LEAGUE: Quarterfinal","2014-04-03",4,"",2002,74,"ENGLAND: Conference National","2014-04-03",1,"1",60,2640,"ENGLAND: U-21 Premier League","2014-04-03",3,"1",60,86,"GERMANY: Regionalliga Nord","2014-04-03",1,"1",74,301,"CZECH REPUBLIC: Pohar CMFS","2014-04-03",2,"",52,94,"DENMARK: Viasat Sport Divisionen","2014-04-03",1,"1",53,1212,"GEORGIA: Umaglesi Liga","2014-04-03",1,"1",73,766,"COPA LIBERTADORES: Group 4","2014-04-04",1,"1",2006,767,"COPA LIBERTADORES: Group 5","2014-04-04",1,"1",2006,916,"LITHUANIA: A Lyga","2014-04-03",1,"1",111,722,"RUSSIA: Premier-Liga Reserves","2014-04-03",2,"1",152,752,"TURKEY: 1. Lig","2014-04-03",1,"1",188,2574,"UKRAINE: Youth League","2014-04-03",1,"1",192,2738,"ARGENTINA: Primera Division, Torneo Final","2014-04-03",1,"1",9,2738,"ARGENTINA: Primera Division, Torneo Final","2014-04-04",1,"1",9,1210,"BOLIVIA: Clausura","2014-04-04",1,"1",25,1047,"COLOMBIA: Apertura","2014-04-04",3,"1",43,1118,"COSTA RICA: Torneo de Verano","2014-04-04",1,"1",47,1296,"KUWAIT: Premier League","2014-04-03",2,"1",102,921,"SINGAPORE: S.League","2014-04-03",2,"1",163,1211,"EGYPT: Premier League","2014-04-03",1,"1",58,1105,"TUNISIA: National A League","2014-04-03",1,"1",187);xgame[1]=Array(422437,"USA","Mexico","","0","04:00","FT","FT","0",0,"0","2","2","2","0","2","2","","",428122,"AZ","Benfica","","1","20:05","-","-1","0",0,"0","-","-","","","","","","",428124,"Basel","Valencia","","1","20:05","-","-1","0",0,"0","-","-","","","","","","",428123,"Lyon","Juventus","","1","20:05","-","-1","0",0,"0","-","-","","","","","","",428125,"Porto","Sevilla","","1","20:05","-","-1","0",0,"0","-","-","","","","","","",389250,"Halifax","Braintree Town","","1","19:45","-","-1","0",0,"0","-","-","","","","","","",404816,"Southampton U-21","Newcastle U-21","","1","14:00","FT","FT","0",1,"0","3","2","3","2","3","2","","",404689,"Everton U-21","Arsenal U-21","","1","19:00","-","-1","0",0,"0","-","-","","","","","","",404735,"Reading U-21","Sunderland U-21","","1","19:00","-","-1","0",0,"0","-","-","","","","","","",391551,"Braunschweig II","St. Pauli II","1","1","18:30","1T","26","0",0,"0","0","2","","","","","","",428392,"Boleslav","Jablonec","1","0","17:00","FT","FT","0",1,"0","1","0","1","0","1","0","","",428391,"Zbrojovka B.","Slavia Praha","1","0","17:00","Pen","Pen","0",1,"0","0","1","0","0","0","0","5","4",399728,"Horsens","Hobro","1","1","17:30","2T","71","0",0,"0","1","0","0","0","","","","",428444,"Sioni","Metalurgi Rustavi","","1","13:00","FT","FT","0",1,"0","2","0","1","0","2","0","","",422040,"Santa Fe Bogota","Atletico-MG","","1","03:00","-","-1","0",0,"0","-","-","","","","","","",422049,"Universidad de Chile","Cruzeiro","","1","03:45","-","-1","0",0,"0","-","-","","","","","","",428445,"Trakai","Atlantas","","1","15:00","FT","FT","0",0,"0","0","0","0","0","0","0","","",402941,"Spartak-D","Ural-D","","1","11:00","FT","FT","0",1,"0","2","0","2","0","2","0","","",402938,"Kuban-D","Tom-D","","1","13:00","FT","FT","0",0,"0","2","2","2","0","2","2","","",405990,"Adanaspor","Samsunspor","1","1","17:00","FT","FT","0",0,"0","1","1","1","1","1","1","","",402441,"Sevastopol-D","Vorskla-D","","1","11:30","FT","FT","0",2,"0","2","3","0","3","2","3","","",419328,"Gimnasia La Plata","Tigre","","1","21:00","-","-1","0",0,"0","-","-","","","","","","",419329,"San Lorenzo","Arsenal S","","1","00:15","-","-1","0",0,"0","-","-","","","","","","",428446,"Blooming","Bolivar","","1","00:30","-","-1","0",0,"0","-","-","","","","","","",419659,"Itagui Ditaires","Deportivo La Equidad","","1","00:00","-","-1","0",0,"0","-","-","","","","","","",419660,"Fortaleza JS","Envigado FC","","1","02:00","-","-1","0",0,"0","-","-","","","","","","",419661,"Patriotas","Deportes Tolima","","1","02:00","-","-1","0",0,"0","-","-","","","","","","",419772,"CS Herediano","Belen Siglo","","1","03:00","-","-1","0",0,"0","-","-","","","","","","",421421,"Khaitan","Al Salmiyah","","1","15:20","Pst","Pst","0",0,"0","?","?","","","","","","",421422,"Al Fehaiheel","Kazma","","1","16:05","FT","FT","0",2,"0","0","1","0","0","0","1","","",424674,"Singapore AF","Woodlands","","1","12:30","FT","FT","0",1,"0","1","0","1","0","1","0","","",424675,"Harimau Muda","Geylang","","1","13:45","FT","FT","0",2,"0","0","3","0","2","0","3","","",381833,"Al Zamalek Cairo","Talaea El Geish","1","1","17:00","2T","90","0",0,"0","1","1","1","1","","","","",425938,"Metlaoui","Etoile du Sahel","","1","14:30","FT","FT","0",2,"0","0","1","0","1","0","1","","");h2hTxt'
		#Tengo que habilitar la conexion a la bd
		#param = [self.config.profile('INFO_DB','DB'),self.config.profile('INFO_DB','USER'),self.config.profile('INFO_DB','PASS'),self.config.profile('INFO_DB','HOST'),self.config.profile('INFO_DB','PORT')]
		#db = Connect(param)
		listaComp = self.ProcesarDatos(textPage,"xcomp[1]",";",5)
		for comp in listaComp:
			url = self.config.profile('INFO_GENERAL','URLFLAG')+str(comp[5])+'.png'
			page = urllib.urlopen(url,proxies=self.proxies)
			#page = urllib.urlopen(url)
			nameFile = str(comp[5])+'.png'
			fichero = open(self.config.profile('INFO_GENERAL','DIRRECURSOS')+'/flags/'+nameFile,'wb')
			fichero.write(page.read())
			
		listaJuegos = self.ProcesarDatos(textPage,"xgame[1]",";h2hTxt",18)
		contjuegos=0
		rango = 0 
		for i in range(len(listaComp)):
			#db.guardarCompetencias(listaComp[i])
			contjuegos = rango
			rango = contjuegos + int(listaComp[i][3])
			for contjuegos in range(contjuegos,rango):
				listaJuegos[contjuegos].append(listaComp[i][0])
		#for i in range(len(listaJuegos)):
			#db.guardarJuegos(listaJuegos[i])
		return listaComp,listaJuegos
		#f.close()

	def ProcesarDatos(self,cadena,tipo,separador,cantElement):
		cadena = cadena.split(tipo)
		cadena = cadena[1].split(separador)
		cadena = cadena[0].replace('=Array(',"")
		cadena = cadena.replace(')',"")
		cadena = cadena.replace(', ','><')
		cadena = cadena.replace('"',"")
		lista = cadena.split(',')
		for i in range(len(lista)):
			lista[i] = lista[i].replace('><',', ')
		cont = 0
		listaAux = []
		listaFinal = []
		for i in range(len(lista)):
			if cont == cantElement:
				listaAux.append(lista[i])
				listaFinal.append(listaAux)
				cont = 0
				listaAux = []
			else:
				listaAux.append(lista[i])
				cont += 1
		return listaFinal