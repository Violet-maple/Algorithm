# coding: utf-8

import cgi
import time


def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']


class PathDispatcher:
    def __init__(self):
        self.pathmap = {}
    
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'],
                                  environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {key: params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, path), notfound_404)
        return handler(environ, start_response)
    
    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function


_hello_resp = '''\
<html>
  <head>
     <title>Hello {name}</title>
   </head>
   <body>
     <h1>Hello {name}!</h1>
   </body>
</html>'''


def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')


_localtime_resp = '''\
<?xml version="1.0"?>
<time>
  <year>{t.tm_year}</year>
  <month>{t.tm_mon}</month>
  <day>{t.tm_mday}</day>
  <hour>{t.tm_hour}</hour>
  <minute>{t.tm_min}</minute>
  <second>{t.tm_sec}</second>
</time>'''

_upload_file = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>上传文件</title>
</head>
<body>
<form action="" method="post" enctype="multipart/form-data">
<table>
    <tr>
        <td>头像：</td>
        <td><input type="file" name="pichead"></td>
    </tr>
    <tr>
        <td>心情：</td>
       <td><input type="text" name="desc"></td>
    </tr>
    <tr>
        <td></td>
       <td><input type="submit" value="提交"></td>
    </tr>
</table>
</form>
</body>
</html>
"""


def localtime(*args):
    start_response = args[1]
    start_response('200 OK', [('Content-type', 'application/xml')])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')


def upload(*args):
    start_response = args[1]
    start_response('200 OK', [('Content-type', 'application/html')])
    resp = _upload_file
    yield resp


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    
    # Create the dispatcher and register functions
    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/hello', hello_world)
    dispatcher.register('GET', '/localtime', localtime)
    dispatcher.register('POST', '/upload', upload)
    
    # Launch a basic server
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()
