#!/usr/bin/python3
""" Task 03: HTTP Server """

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from json import dumps

class RequestHandler(BaseHTTPRequestHandler):
    """ Request Handler """

    def do_GET(self):
        """ Handle GET request """
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/":
            self._send_response(200, "text/plain", "Hello, this is a simple API!")
        elif parsed_path.path == "/data":
            self._send_response(200, "application/json", {"name": "John", "age": 30, "city": "New York"})
        elif parsed_path.path == "/status":
            self._send_response(200, "text/plain", "OK")
        elif parsed_path.path == "/info":
            self._send_response(200, "application/json", {"version": "1.0", "description": "A simple API built with http.server"})
        else:
            self._send_response(404, "text/plain", "Endpoint not found")

    def _send_response(self, status_code, content_type, content):
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        if isinstance(content, dict):
            content = dumps(content)
        self.wfile.write(content.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    """ Run the server """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

run()
