create table aluno
(
	cpf bigint not null primary key,
	matricula integer not null,
    nome_inicio varchar(20),
    nome_resto varchar(60),
    data_nascimento date,
    nome_curso varchar(40),
    tipo_curso varchar(20),
    codigo_turma varchar(10),
    email_pessoal varchar(40),
    email_institucional varchar(40),
    email_lista_transmissao varchar(40)
);

INSERT INTO aluno(cpf, matricula, nome_inicio, nome_resto, data_nascimento, nome_curso, tipo_curso, codigo_turma, email_pessoal, email_institucional, email_lista_transmissao)
VALUES (12312312300, 11223344, 'bruno', 'primeiro', '1953-01-01', 'Ciência Computação', 'Graduação', 'CC4TA', 'nome@icloud.com', 'nome@aluno.faculdade.br', 'curso@aluno.faculdade.br'), (11122233, 44112233, 'bruno', 'segundo', '1953-01-01', 'Ciência Computação', 'Graduação', 'CC4TA', 'nome@icloud.com', 'nome@aluno.faculde.br', 'curso@aluno.faculdade.br')