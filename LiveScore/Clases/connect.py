import mysql.connector

class Connect:
	
	def __init__(self, param):
		self.conn = mysql.connector.connect(database=param[0],user=param[1],password=param[2], host=param[3],port=param[4])
		self.cur = self.conn.cursor()

	def guardarCompetencias(self,param):
		try:
			self.cur.execute("INSERT INTO tb_competicion (id, nombre,fecha) VALUES (%s, %s, %s)",(param[0],param[1],param[2]))
		except (mysql.connector.errors.IntegrityError) as err:
			self.cur.execute("UPDATE tb_competicion SET id = %s, nombre = %s, fecha = %s WHERE id = %s ",(param[0],param[1],param[2],param[0]))
		self.conn.commit()

	def guardarJuegos(self,param):
		try:
			self.cur.execute("INSERT INTO tb_juego (id, equipo1,equipo2,hora,tiempo,minuto,eqganador,goltiemporealeq1,goltiemporealeq2,goleq1t1,goleq2t1,goleq1final,goleq2final,goleq1pen,goleq2pen,idcompeticionfk) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)",(param[0],param[1],param[2],param[3],param[4],param[5],param[6],param[7],param[8],param[9],param[10],param[11],param[12],param[13],param[14],param[19]))
		except (mysql.connector.errors.IntegrityError) as err:
			self.cur.execute("UPDATE tb_juego SET id = %s, equipo1 = %s, equipo2 = %s, hora = %s, tiempo = %s,minuto = %s,eqganador = %s,goltiemporealeq1 = %s,goltiemporealeq2 = %s,goleq1t1 = %s,goleq2t1 = %s,goleq1final = %s,goleq2final = %s,goleq1pen = %s,goleq2pen = %s,idcompeticionfk = %s WHERE id = %s ",(param[0],param[1],param[2],param[3],param[4],param[5],param[6],param[7],param[8],param[9],param[10],param[11],param[12],param[13],param[14],param[19],param[0]))
		self.conn.commit()

	def executeConsult(self,consult):
		self.cur.execute(consult)
		self.conn.commit()

	def closseConnect(self):
		self.cur.close()
		self.conn.close()