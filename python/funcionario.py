class Funcionario:
    def __init__(self,nome,email):
        self._nome = nome
        self._departamento = ""
        self._id = ""
        self._email = email
    def _set_nome(self,nome):
        self._nome = nome
    def _get_nome(self):
        return self._nome
    nome = property(_get_nome,_set_nome)
    def _set_departamento(self,departamento):
        self._departamento = departamento
    def _get_departamento(self):
        return self._departamento
    departamento = property(_get_departamento,_set_departamento)
    def _set_id(self,id):
        self._id = id
    def _get_id(self):
        return self._id
    id = property(_get_id,_set_id)
    def _set_email(self,email):
        self._email = _email
    def _get_email(self):
        return self._email
    email= property(_get_email,_set_email)