
import http.server 
import socketserver 
from var import *


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        self.directory = PATHDIR
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
 

def run_http_server():
    handler = MyHttpRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        httpd.serve_forever()
