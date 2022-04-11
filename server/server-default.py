### ### ### ### ###
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import sys 

from time import sleep
from time import localtime
from time import asctime

import threading


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b'<b>Hello from hostname:</b> ' + socket.gethostname().encode() + b'<br><br>')
        self.wfile.write(b'<b>Text arg: </b> ' + str(string_arg).encode() + b'<br><br>')
        self.wfile.write(b'<b>Time: </b> ' + str(asctime(localtime())).encode() + b'<br><br>')
        if self.path.endswith('/favicon.ico'):
          print("TEST")

string_arg = sys.argv[1]
SERVER_PORT = 8000

def worker1(number):
  while True:
    print(str(asctime(localtime())))
    sleep(1)  
    
def worker2(number):
  while True:
    print("TEST2")
    sleep(1)  

def main():
  threading.Thread(target=worker1, args=(1,)).start()
  threading.Thread(target=worker2, args=(1,)).start()
  
  httpd = HTTPServer(('0.0.0.0', SERVER_PORT), SimpleHTTPRequestHandler)
  print('Listening on port %s ...' % SERVER_PORT)
  httpd.serve_forever()
  
main()