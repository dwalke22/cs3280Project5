#!/usr/bin/env python3
"""
HTTP server for calculating subnet
"""
import http.server
import main

__author__ = "David Walker"
__version__ = "Fall 2020"

class Project2Server(http.server.BaseHTTPRequestHandler):
    '''
    Specialized subclass htat listens at the HTTP socket, dispatching the requests to a handler.
    '''
    def do_GET(self):
        """
        Overriding do_GET()
        """
        self.log_message("path: %s", self.path)
        try:
            path = self.path
            self.log_message("resource: %s", path)
            resource = path[1:]
            print(resource)
            if not resource.startswith('subnet'):
                self.log_message("resource: %s", path)
                self.send_error(404, 'Resource must begin with: operation')


            start = len('subnet') + 1
            query = resource[start:].split('&')
            print(query)

            body = self.process_and_respond(query)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))

        except Exception as exception:
            self.send_error(500, str(exception))

    def process_and_respond(self, query):
        '''
        Processes content for valid query.
        Parameters:
        query - the parameters provided to the query
        '''
        body = main.main(query[0], query[1])
        html = "<!DOCTYPE html><html>"
        html += "<head><title>"
        html += "Response from Project 2"
        html += "</title></head>"
        html += "<body><p><h1>"
        html += body
        html += "</h1></p></body>"
        html += "</html>"
        self.log_message("page built")
        return html

if __name__ == "__main__":
    PORT = 3280
    server = http.server.HTTPServer(('160.10.208.35', PORT), Project2Server)
    print("Project 2 - Webserver running on port {}; Type <Ctrl-C> to stop server.".format(PORT))
    server.serve_forever()
