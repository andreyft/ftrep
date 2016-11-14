import os
import re

def wsgi_application(environ, start_response):
    body =[]
    url = os.environ['QUERY_STRING']
    rezult = re.split(r'&', url)
    for i in rezult:
        body.append(i+"\r\n")

    status = '200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]
    start_response(status, headers )
    return [ body ]
