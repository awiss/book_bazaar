import os
import urlparse
from sqlalchemy import create_engine
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
from controllers.home import index
from controllers.book import add,view_book
from types import MethodType
import models
from sqlalchemy.orm import sessionmaker


class Bazaar(object):

    # This function does some magic, pass in a route and a function, and 
    # it handles the werkzeug endpoint crap for you.

    # Note: Any function bound using this will be treated as a method on the Bazaar object,
    # and thus be passed self as a parameter
    def bind_route(self,route,controller):
        self.url_map.add(Rule(route,endpoint=controller.__name__))
        setattr(self,'on_'+controller.__name__,MethodType(controller,self))


    def __init__(self, config):
        engine = create_engine(config['host']+config['db'])
        self.mysql = engine.connect()
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                 autoescape=True)

        models.metadata.create_all(self.mysql)
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.mysql_session = Session()
        self.url_map = Map()
        self.bind_route('/',index)
        self.bind_route('/add',add)
        self.bind_route('/add_book',add)
        self.bind_route('/book/<book_id>',view_book)

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException, e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(mysql_host='mysql://root@localhost/', mysql_db='book_bazaar', with_static=True):
    app = Bazaar({
        'host':     mysql_host,
        'db':       mysql_db
    })

    

    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)