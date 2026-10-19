import http.server
import socketserver
import os
import webbrowser

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"Starting ReviewLens Local Server at http://localhost:{PORT}")
print(f"Serving files from: {DIRECTORY}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("ReviewLens UI is live! Press Ctrl+C to terminate server.")
    # Attempt to open browser automatically
    try:
        webbrowser.open(f"http://localhost:{PORT}")
    except Exception:
        pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
