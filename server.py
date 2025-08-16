from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Charger les frames en mémoire
with open("frames.txt") as f:
    frames = f.read().split("===FRAME===")

class AsciiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/rick":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            try:
                while True:
                    for frame in frames:
                        self.wfile.write((frame + "\n").encode("utf-8"))
                        self.wfile.flush()
                        time.sleep(0.1)  # 10 FPS
            except BrokenPipeError:
                pass
        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), AsciiHandler)
    print("Serveur ASCII lancé sur http://localhost:8080/rick")
    server.serve_forever()
