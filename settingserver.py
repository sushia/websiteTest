# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 11:33:36 2018

@author: Sushia
"""

import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 4444), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='yourpemfile.pem', server_side=True)
httpd.serve_forever()