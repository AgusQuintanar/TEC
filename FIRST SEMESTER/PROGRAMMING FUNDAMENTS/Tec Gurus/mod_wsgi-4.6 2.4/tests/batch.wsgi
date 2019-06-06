import os.path

BASEDIR = os.path.dirname(__file__)
DATAFILE = os.path.join(BASEDIR, 'public_html', '64M')

DATAFILE = '/tmp/data.txt'

data = open(DATAFILE, 'rb').read()

class TestApp(object):
    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [
            ('Content-type', 'application/octet-stream; charset=binary'),
            ('Content-length', str(len(data))),
            ('Content-Disposition', 'attachment; filename="data.txt"'),
        ]
        start_response(status, response_headers)
        return [data]

application = TestApp()
