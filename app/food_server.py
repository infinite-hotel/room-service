from http.server import BaseHTTPRequestHandler, HTTPServer

class FoodHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        food_map = {
            "/pizza": "You ordered pizza 🍕!",
            "/sushi": "You ordered sushi 🍣!",
            "/paella": "You ordered paella 🥘!",
            "/burger": "You ordered burger 🍔!",
        }

        response = food_map.get(self.path.lower(), "Unknown item. Try /pizza, /sushi, /paella, or /burger.")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=FoodHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Food server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
