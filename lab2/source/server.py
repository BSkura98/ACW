#!/usr/bin/env python3
import http.server
import socketserver
import os

from urllib.parse import urlparse, parse_qs
from datetime import datetime

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
            
            query_parameters = parse_qs(parse.query)
            
            if query_parameters.get('cmd', None) == ['time']:            
            	self.wfile.write(str.encode(datetime.now().strftime('%H:%M:%S') + "\n"))
            elif query_parameters.get('cmd', None) == ['rev']:
            	string_to_reverse_param = query_parameters.get('str', None)
            	
            	if string_to_reverse_param:
            		string_to_reverse = string_to_reverse_param[0]
            		reversed_string = string_to_reverse[::-1]
            		self.wfile.write(str.encode(reversed_string) + "\n")
            else:
            	self.wfile.write(b"Hello World!\n")
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
