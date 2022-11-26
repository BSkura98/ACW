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
            self.wfile.write(str.encode(json.dumps({'lowerCase': 1, 'uppercase': 1, 'digits': 1, 'special': 1})))
            
            if params.get('str', None):
                text = params.get('str', None)[0]
                self.wfile.write(str.encode(f'{text}\n'))
            
        else:
            super().do_GET()

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
