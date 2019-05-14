class ProjetoFuncionario:
    def __init__(self,):
        self._idprojeto = ""
        self._idfuncionario = ""
    def _set_idprojeto(self,idprojeto):
        self._idprojeto = idprojeto
    def _get_idprojeto(self):
        return self._idprojeto
    idprojeto = property(_get_idprojeto,_set_idprojeto)
    def _set_idfuncionario(self,idfuncionario):
        self._idfuncionario = idfuncionario
    def _get_idfuncionario(self):
        return self._idfuncionario
    idfuncionario = property(_get_idfuncionario,_set_idfuncionario)