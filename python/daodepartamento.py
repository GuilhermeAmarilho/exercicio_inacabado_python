from departamento import Departamento
from datetime import datetime
import psycopg2
class DepartamentoDAO:
    def __init__(self):
        self._conn = psycopg2.connect("dbname=python host=localhost user=postgres password=postgres port=5432")
    def inserir(self,dep):
        cur = self._conn.cursor()
        cur.execute("INSERT INTO departamento (nome,dataatualizacao) VALUES (%s,now())",[dep.nome])
        cur.close()
        self._conn.commit()
        self._conn.close()
    def deletar(self,id):
        cur = self._conn.cursor()
        cur.execute("DELETE FROM departamento where id = %s",[id])
        self._conn.commit()
        cur.close()
        self._conn.close()

b = DepartamentoDAO()
b.inserir(Departamento("erre aga"))