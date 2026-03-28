
import http.server
import socketserver

PORT = 8001

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '../html/hello_world.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()