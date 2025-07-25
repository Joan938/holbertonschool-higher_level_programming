from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def do_GET(self):
        """
        Handle GET requests for endpoints:
          /         -> plain text welcome
          /data     -> JSON data sample
          /status   -> plain text OK
          /info     -> JSON with version and description
        Other paths -> 404 Not Found plain text
        """
        # Root endpoint
        if self.path == '/':
            self._set_headers(200, 'text/plain')
            message = 'Hello, this is a simple API!'
            self.wfile.write(message.encode('utf-8'))

        # JSON Data endpoint
        elif self.path == '/data':
            payload = {'name': 'John', 'age': 30, 'city': 'New York'}
            response_text = json.dumps(payload)
            self._set_headers(200, 'application/json')
            self.wfile.write(response_text.encode('utf-8'))

        # Status endpoint
        elif self.path == '/status':
            self._set_headers(200, 'text/plain')
            self.wfile.write(b'OK')

        # Info endpoint
        elif self.path == '/info':
            payload = {
                'version': '1.0',
                'description': 'A simple API built with http.server'
            }
            response_text = json.dumps(payload)
            self._set_headers(200, 'application/json')
            self.wfile.write(response_text.encode('utf-8'))

        # Undefined endpoints
        else:
            self._set_headers(404, 'text/plain')
            self.wfile.write(b'Endpoint not found')


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting http.server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print('Server stopped.')


if __name__ == '__main__':
    run()
