from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import datetime
import logging

HOST = '0.0.0.0'
PORT = 8080

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# # setting stdio handler to logger
# handler_stdio = logging.StreamHandler()
# handler_stdio.setFormatter(logging.Formatter("%(asctime)s %(threadName)s %(levelname)8s %(message)s"))
# logger.addHandler(handler_stdio)

# setting docker handler to logger
handler_docker = logging.FileHandler(filename="/proc/1/fd/1")
handler_docker.setFormatter(logging.Formatter("%(asctime)s %(threadName)s %(levelname)8s %(message)s"))
logger.addHandler(handler_docker)

logger.debug("message test debug")
logger.info("message test info")
logger.warning("message test warn")
logger.error("message test error")

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logger.info("This is Get -- start --")
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        body = str(datetime.datetime.now()) + " Hello Webserver. This is GET Method\n"
        print(body)
        self.wfile.write( body.encode(encoding='utf-8') )
        logger.info("This is Get -- end --")

    def do_POST(self):
        logger.info("This is Post -- start --")
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        body = str(datetime.datetime.now()) + " Hello Webserver. This is POST Method\n"
        print(body)
        self.wfile.write( body.encode(encoding='utf-8') )
        logger.info("This is Post -- end --")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), HTTPHandler)
    server.serve_forever()
