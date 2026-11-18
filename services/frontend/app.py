import json
from http.server import BaseHTTPRequestHandler, HTTPServer

FRONTEND_VERSION = "1.1.1"


class FrontendHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        if self.path == "/info":
            response = {
                "service": "frontend",
                "version": FRONTEND_VERSION,
            }

            body = json.dumps(response).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Not Found")

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


def main():
    server = HTTPServer(("0.0.0.0", 8080), FrontendHandler)
    print("Frontend service listening on port 8080")
    server.serve_forever()


if __name__ == "__main__":
    main()
