#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
from urllib.parse import urlparse, parse_qs

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        print(self.path)
        
        url_parsed = urlparse(self.path)
        params = parse_qs(url_parsed.query)

        if url_parsed.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=UTF-8')
            self.end_headers()            
            
            if params.get('str', None):
                text = params.get('str', None)[0]
          	lowercase = 0
                uppercase = 0
                digits = 0
                special = 0

		for char in text:
		    if char.islower():
		        uppercase += 1
		    elif char.isupper():
		        lowercase += 1
		    elif char.isdigit():
		        digits += 1
		    else:
		       	special += 1
		       	
		       	
                self.wfile.write(str.encode(json.dumps({'lowercase': 1, 'uppercase': 1, 'digits': 1, 'special': 1})))
                self.wfile.write(str.encode(f'{text}\n'))
            
        else:
            super().do_GET()

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
