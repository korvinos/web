def app(environ, start_responce):
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain')
    ]
    data = environ['QUERY_STRING'].split('&')
    body = list(map(lambda x: x + '\n', data))
    start_responce(status, response_headers)
    return body
