from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import datetime

HOST = '0.0.0.0'
PORT = 8080

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        body = str(datetime.datetime.now()) + " Hello Webserver. This is GET Method\n"
        print(body)
        self.wfile.write( body.encode(encoding='utf-8') )

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        body = str(datetime.datetime.now()) + " Hello Webserver. This is POST Method\n"
        print(body)
        self.wfile.write( body.encode(encoding='utf-8') )

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), HTTPHandler)
    server.serve_forever()
