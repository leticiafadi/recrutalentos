def index():
    return dict()

def listarCurriculo():
   cv = SQLFORM.grid(db.curriculo)
   return locals()
@auth.requires_login()
def addCurriculo():
    form = SQLFORM(Curriculo)
    if form.process().accepted:
        session.flash="Currículo cadastrado com sucesso"
        redirect(URL("index"))
    elif form.errors:
        response.flash ="Nâo foi possivel cadastrar o currículo"
    else:
        response.flas = "Currículo vazio!"
    return dict(form=form)

#def editarCurriculo():