# -*- coding: utf-8 -*-
Curriculo = db.define_table('curriculo',
Field('nome', 'string', label='Nome', notnull=True),
Field('cpf', 'string', label='CPF', notnull=True, unique=True),
Field('contato', 'list:string', label='Contato', notnull=True),
Field('endereco', 'list:string', label='Endereço'),
Field('form_academica', 'list:string', label='Formação Academica'),
Field('foto', 'upload', label='Foto'),
Field('experiencia', 'list:string', label='Experiencia Profissional'),
Field('data_nascimento', 'date', label='Data de Nascimento'),
Field('objetivo_setor', 'string', label='Setor')
)

Entrevista = db.define_table('entrevista',
Field('obsNegativas', 'list:string', label='Pontos Negativos'),
Field('obsPositivas', 'list:string', label='Pontos Positivos'),
Field('idCurriculo', 'reference curriculo')
)

Dinamica = db.define_table('dinamica',
Field('nome', 'string', label='Nome'),
Field('descricao', 'string', label='Contato'),
Field('tipo', 'boolean', label='Tipo de Dinamica'),
Field('obsNegativas', 'list:string', label='Pontos Negativos'),
Field('obsPositivas', 'list:string', label='Pontos Positivos'),
Field('idCurriculo','reference curriculo')
)

Teste = db.define_table('teste',
Field('nome', 'string', label='Nome'),
Field('descricao', 'string', label='Contato'),
Field('tipo', 'boolean', label='Tipo de Dinamica'),
Field('obsNegativas', 'list:string', label='Pontos Negativos'),
Field('obsPositivas', 'list:string', label='Pontos Positivos'),
Field('idCurriculo', 'reference curriculo')
)

Vaga = db.define_table('vaga',
Field('nome', 'string', label='Nome'),
Field('form_academica', 'string', label='Formação Academica'),
Field('experiencia', 'list:string', label='Experiencia Profissional'),
Field('localTrabalho', 'string', label='Local de Trabalho'),
Field('horarioTrabalho', 'string', label='Horario de Trabalho'),
Field('salarioOferecido', 'float', label='Salario Oferecido'),
Field('qtdVagas', 'integer', label='Quantidade de Vagas'),
Field('qtdCandidatos', 'integer', label='Quantidade de Candidatos'),
Field('responsavelVaga', 'string', label='Responsável pela Vaga')
)

Processo = db.define_table('processo',
Field('etapa', 'integer'),
Field('idVaga', 'reference vaga'),
Field('prazo', 'date')
)

ProcessoCurriculo = db.define_table('processoCurriculo',
Field('idCurriculo', 'reference curriculo'),
Field('idProcesso', 'reference processo')
)


