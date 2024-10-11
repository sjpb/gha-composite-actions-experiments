from http.server import BaseHTTPRequestHandler, HTTPServer

response = None

OPTIONS = ('continue', 'abort')
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global response
        choice = self.path.lstrip('/')
        if choice in OPTIONS:
            response = choice
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'You chose ' + choice.encode())

def run_server():
    global response
    server = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print('Starting server...')
    # while response is None:
    server.handle_request()
    server.server_close()
    print(response)
    return response

if __name__ == '__main__':
    run_server()
