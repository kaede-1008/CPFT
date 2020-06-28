# -*- coding: utf-8 -*-
# python -m http.server 8080 --cgi
import http.server
http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler)
