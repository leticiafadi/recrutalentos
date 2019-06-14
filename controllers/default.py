 -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.view_title = "Recrutalentos Home Page"
    return dict(message='')


def about():
    response.view_title = 'About'
    return dict()


def tou():
    response.view_title = 'Terms of Use'
    return dict()


def privacy():
    response.view_title = 'Privacy Policy'
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    

    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@request.restful()
def api():
    response.view = 'generic.json'

    def GET(tablename, id):
        if not tablename == 'curriculo':
            raise HTTP(400)
        return dict(curriculo = db.curriculo(id))
    return locals()

def tou():
    return dict()
