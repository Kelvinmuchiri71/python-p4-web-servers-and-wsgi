#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response

@Request.application                                       #mathod which tells our code to run any code inside of the function in the browser at the location specified with our development server
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple

    #run simple() method runs a server for a one-page application
    #requirements: hostname(localhost), port and an application

    run_simple(                                              
        hostname='localhost',
        port=5555,
        application=application
    )