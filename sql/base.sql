CREATE TABLE departamento(
    id SERIAL NOT NULL,
    nome VARCHAR(50) NOT NULL,
    idgerente INTEGER,
    dataatualizacao TIMESTAMP NOT NULL,
    CONSTRAINT iddepto PRIMARY KEY (id)
);
CREATE TABLE funcionario(
    id SERIAL NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL,
    iddepto INTEGER,
    CONSTRAINT iddeptofk FOREIGN KEY (iddepto)
        REFERENCES departamento
        on delete SET NULL
        on update CASCADE,
    CONSTRAINT idfunc PRIMARY KEY (id)
);
ALTER TABLE departamento add 
	CONSTRAINT idgerentefk FOREIGN KEY (idgerente)
        REFERENCES funcionario
        on delete SET NULL
        on update CASCADE;
CREATE TABLE projeto(
    id SERIAL NOT NULL,
    nome VARCHAR(50) NOT NULL,
    dataprevista TIMESTAMP NOT NULL,
    CONSTRAINT idpk PRIMARY KEY (id)
);
CREATE TABLE projetofuncionario(
    idprojeto INTEGER NOT NULL,
    idfuncionario INTEGER NOT NULL,
    CONSTRAINT idprojetofk FOREIGN KEY (idprojeto)
        REFERENCES projeto
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT idfuncionariofk FOREIGN KEY (idfuncionario)
        REFERENCES funcionario
        ON DELETE CASCADE
        ON UPDATE CASCADE
);