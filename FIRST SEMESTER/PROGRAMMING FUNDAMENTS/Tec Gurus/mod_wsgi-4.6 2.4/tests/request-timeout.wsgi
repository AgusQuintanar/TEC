import os
import sys
import time
import threading
import traceback
import mod_wsgi

def event_handler(name, **kwargs):
    if name == 'request_started':
        request_data = mod_wsgi.request_data()
        request_data.update(kwargs)
        request_data['python_thread_id'] = threading.get_ident()

    elif name == 'process_stopping':
        if kwargs['shutdown_reason'] == 'request_timeout':
            print('SHUTDOWN')

            current_time = time.time()

            stacks = dict(sys._current_frames().items())
            active = dict(mod_wsgi.active_requests.items())

            for request_id, request_data in active.items():
                python_thread_id = request_data['python_thread_id']
                application_start = request_data['application_start']
                request_environ = request_data['request_environ']
                request_uri = request_environ['REQUEST_URI']

                running_time = current_time - application_start

                print()

                print('THREAD_ID', python_thread_id)
                print('REQUEST_ID', request_id)
                print('REQUEST_URI', request_uri)
                print('RUNNING_TIME', running_time)

                if python_thread_id in stacks:
                    print('STACK-TRACE')
                    traceback.print_stack(stacks[python_thread_id])

mod_wsgi.subscribe_events(event_handler)

def application(environ, start_response):
    sleep_duration = environ.get('HTTP_X_SLEEP_DURATION', 0)
    sleep_duration = float(sleep_duration or 0)

    status = '200 OK'
    output = b'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    if sleep_duration:
        time.sleep(sleep_duration)

    yield output
