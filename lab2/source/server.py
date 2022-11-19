#!/usr/bin/env python3
import http.server
import socketserver
import os

from urllib.parse import urlparse, parse_qs

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        parse = urlparse(self.path)
        
        if parse.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            
            query_params = parse_qs(parse.query)
            
            if query_params.get('cmd', None) == ['time']:            
            	self.wfile.write(b"time\n")
            elif query_params.get('cmd', None) == ['rev']:
            	self.wfile.write(b"rev\n")
            else:
            	self.wfile.write(b"Hello World!\n")
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
