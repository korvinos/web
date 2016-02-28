def app(environ, start_responce):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plan')
    ]
    data = environ['QUERY_STRING'].split('&')
    body = list(map(lambda x: x + '\n', data))
    start_responce(status, headers)
    return body
