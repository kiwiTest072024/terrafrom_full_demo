from http.server import BaseHTTPRequestHandler, HTTPServer


# Define the HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Send message back to client
        message = "Hello, World!"

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


# Main function to run the server
def run():
    print('Starting server...')

    # Server settings
    server_address = ('', 8000)  # Serve on all available IPs on port 8000
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Run the server
    print('Running server on port 8000...')
    httpd.serve_forever()


# Run the server if this script is executed
if __name__ == '__main__':
    run()
