class Departamento:
    def __init__(self,nome):
        self._nome = nome
        self._gerente = ""
        self._id = ""
        self._dataatualizacao = ""
    def _set_nome(self,nome):
        self._nome = nome
    def _get_nome(self):
        return self._nome
    nome = property(_get_nome,_set_nome)
    def _set_gerente(self,gerente):
        self._gerente = gerente
    def _get_gerente(self):
        return self._gerente
    gerente = property(_get_gerente,_set_gerente)
    def _set_id(self,id):
        self._id = id
    def _get_id(self):
        return self._id
    id = property(_get_id,_set_id)
    def _set_dataatualizacao(self,dataatualizacao):
        self._dataatualizacao = dataatualizacao
    def _get_dataatualizacao(self):
        return self._dataatualizacao
    dataatualizacao = property(_get_dataatualizacao,_set_dataatualizacao)