from http import server as SimpleHTTPServer

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        if self.path == "/emanuel":
            self.path = "/emanuel.html"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("Nov/emanuel.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        
if __name__ == "__main__":
    PORT = 8888
    server_address = ("", PORT)
    httpd = SimpleHTTPServer.HTTPServer(server_address, MyHandler)
    print(f"Serving on port {PORT}")
    httpd.serve_forever()