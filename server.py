import http.server
import importlib
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs
class GetHandler(BaseHTTPRequestHandler):

 def do_GET(self):
    try:
        url=urlparse(self.path)
        """
        if(url.path.endswith('/')):
         print("/ index file request")
         f = open("onecom/index.html","rb")
         self.send_response(200)
         self.send_header("Content-type","text/html")
         self.end_headers()
         self.wfile.write(f.read())
         f.close()
        """
        if(url.path.endswith('py')):
         print("Python file request")
         tmpPath=url.path[1:len(url.path)-3].replace('/','.')
         i=importlib.import_module(tmpPath)
         requestHandler=i.RequestHandler()
         requestHandler.getResponse(self)
        elif(url.path.endswith('html')) :
         print("Html file request")
         f=open(url.path[1:],"rb")
         self.send_response(200)
         self.send_header("Content-type", "text/html")
         self.end_headers()
         self.wfile.write(f.read())
         f.close()
        else :
         print("Index file request")
         if(url.path.endswith('/')): f = open(url.path[1:]+"index.html","rb")
         else : f = open(url.path[1:]+"/index.html","rb")
         f = open(url.path[1:]+"/index.html","rb")
         self.send_response(200)
         self.send_header("Content-type","text/html")
         self.end_headers()
         self.wfile.write(f.read())
         f.close()
        return
    except IOError:
        self.send_error(404, "File Not Found: %s" % self.path)


def run(server_class=HTTPServer,handler_class=GetHandler):
 server_address = ('', 8000)
 httpd = server_class(server_address, handler_class)
 print("Server started")
 httpd.serve_forever()
run()
