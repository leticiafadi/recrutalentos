def index():
    grid = SQLFORM.smartgrid(db.vaga)
    return locals()

 
def editarVaga():
    form = SQLFORM(db.vaga, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Vaga Atulizada: %s' % form.vars.nome
        redirect(URL('listarVagas'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

def adicionarVaga():

    form = SQLFORM(db.vaga)
    if form.process().accepted:
        db.processo.insert(etapa="1",idVaga=form.vars.id)
        session.flash="Vaga Cadastrada com Sucesso !"
        redirect(URL("index"))
    elif form.errors:
        response.flash ="Verifique os Campos do formulário"
    else:
        response.flash = "O formulário está em branco"
    return dict(form=form)

def cancelarVaga():
    db(Vaga.id==request.args(0, cast=int)).delete()
    session.flash = 'Vaga apagada!'
    redirect(URL('listarVagas'))