# -*- coding: utf-8 -*-

from http import HTTPStatus
import http.server
import socketserver
import threading

import core.logger
import version

# This is hardcoded in application and should be to whatever configured
# in developers.eveonline.com application settings page. Sadly, it seems to be
# that listen port can not be changed
ESI_HANDLER_BIND_ADDRESS = ('127.0.0.1', 10233)


class EsiHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self._logger = core.logger.get_logger(__name__)
        ver = version.get_pyevemon_version()
        self.server_version = ver['useragent_str']
        # documentation says we should not override base class's __init__()
        # so at least let it do its work... but we need a logger :)
        super(EsiHttpRequestHandler, self).__init__(request, client_address, server)

    def handle(self):
        # here, instance variables are set by base class's __init__():
        # self.request = request
        # self.client_address = client_address
        # self.server = server
        self._logger.debug('ESI handler: request from {}:{}'.format(
            str(self.client_address[0]), str(self.client_address[1])))
        super(EsiHttpRequestHandler, self).handle()

    def do_GET(self):
        content = '<h1>Hello!</h1>'
        content_utf8 = content.encode('utf-8', errors='ignore')
        #
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', str(len(content_utf8)))
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(content_utf8)
        self.close_connection = True

    def log_message(self, format, *args):
        """
        Override BaseHTTPRequestHandler's logger worker function to redirect
        all logging output where we need to
        :param format: The first argument, FORMAT, is a format string for the
        message to be logged.  If the format string contains any % escapes
        requiring parameters, they should be specified as subsequent arguments
        (it's just like printf!)
        :param args: optional arguments for format
        :return: None
        """
        self._logger.debug('ESI log: {}'.format(format % args))


class EsiCallbackLocalHttpServer(http.server.HTTPServer, socketserver.ThreadingMixIn):
    def __init__(self):
        self._logger = core.logger.get_logger(__name__)
        self._server_address = ESI_HANDLER_BIND_ADDRESS
        self.allow_reuse_address = True
        self.daemon_threads = True
        super(EsiCallbackLocalHttpServer, self).__init__(self._server_address, EsiHttpRequestHandler)


class EsiHandlerThread(threading.Thread):
    def __init__(self):
        super(EsiHandlerThread, self).__init__(name='EsiHandlerThread', daemon=True)
        self._logger = core.logger.get_logger(__name__)
        self.httpserver = EsiCallbackLocalHttpServer()

    def run(self):
        self._logger.info('Starting ESI Callback receiver HTTP server at address: {}:{}'.format(
            str(ESI_HANDLER_BIND_ADDRESS[0]), str(ESI_HANDLER_BIND_ADDRESS[1])))
        self.httpserver.serve_forever()

    def stop(self):
        # Ask TCPServer to stop select() loop on socket
        # and wait for it to shut down
        self._logger.debug('Stopping ESI handler server...')
        self.httpserver.shutdown()
        self._logger.debug('Stopped ESI handler.')


def esi_handler_start() -> EsiHandlerThread:
    thr = EsiHandlerThread()
    thr.start()
    return thr
