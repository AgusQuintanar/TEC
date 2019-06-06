def process_group(environ):
    print('process-group', environ)
    return 'localhost:8000'

def application_group(environ):
    print('application-group', environ)
    return ''

def callable_object(environ):
    print('callable-object', environ)
    return 'handle_request'
