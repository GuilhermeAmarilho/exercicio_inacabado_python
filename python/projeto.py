class Projeto:
    def __init__(self,nome,dataprevisao):
        self._nome = nome
        self._dataprevisao = dataprevisao
        self._id = ""
    def _set_nome(self,nome):
        self._nome = nome
    def _get_nome(self):
        return self._nome
    nome = property(_get_nome,_set_nome)
    def _set_dataprevisao(self,dataprevisao):
        self._dataprevisao = dataprevisao
    def _get_dataprevisao(self):
        return self._dataprevisao
    dataprevisao = property(_get_dataprevisao,_set_dataprevisao)
    def _set_id(self,id):
        self._id = id
    def _get_id(self):
        return self._id
    id = property(_get_id,_set_id)