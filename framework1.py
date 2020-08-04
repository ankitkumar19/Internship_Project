def application(environ, start_response):
    response_body = [
        '{key}: {value}'.format(key = key, value = value) for key,value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'

    response_headers = [
        ('Content-type','text/plain'),
    ]

    start_response(status,response_headers)

    return [response_body.encode('utf-8')]