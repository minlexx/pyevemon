# -*- coding: utf-8 -*-

import base64
from http import HTTPStatus
import http.server
import socketserver
import threading
import time
import urllib.parse

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
        """
        This handles HTTP GET request.
        When called from EVE-SSO it should receive query-string like this:
        ?code=x9Y6F7K9Ij9KjRF0fxAVxJVZcLSiwkqfAq13aHIOyuyWoUbyN3jzP3_ZY1y3SchB0&state=MTQ5NTI3NzY5OC4yNjk3NTA0
        :return: None
        """
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
        # Does it work...?
        self._logger.debug('Stopping ESI handler server...')
        self.httpserver.shutdown()
        self._logger.debug('Stopped ESI handler.')


def esi_handler_start() -> EsiHandlerThread:
    """
    Client code should only use this function to start
    http server that receives EVE Online SSO Oauth2 reply.
    :return: EsiHandlerThread instance, to probably call stop() on it
    """
    thr = EsiHandlerThread()
    thr.start()
    return thr


def esi_get_oauth_request_parameters() -> str:
    ret = dict()
    ret['response_type'] = 'code'
    ret['redirect_uri'] = 'http://localhost:10233/'
    ret['client_id'] = 'a67b73af98c64158a158a85d850b01a3'
    ret['scope'] = 'publicData esi-calendar.read_calendar_events.v1 ' \
                   'esi-location.read_location.v1 esi-location.read_ship_type.v1 ' \
                   'esi-mail.read_mail.v1 esi-skills.read_skills.v1 ' \
                   'esi-skills.read_skillqueue.v1 esi-wallet.read_character_wallet.v1 ' \
                   'esi-search.search_structures.v1 esi-clones.read_clones.v1 ' \
                   'esi-characters.read_contacts.v1 esi-universe.read_structures.v1 ' \
                   'esi-bookmarks.read_character_bookmarks.v1 ' \
                   'esi-killmails.read_killmails.v1 ' \
                   'esi-corporations.read_corporation_membership.v1 ' \
                   'esi-assets.read_assets.v1 esi-planets.manage_planets.v1 ' \
                   'esi-fleets.read_fleet.v1 esi-fittings.read_fittings.v1 ' \
                   'esi-markets.structure_markets.v1 esi-characters.read_loyalty.v1 ' \
                   'esi-characters.read_opportunities.v1 ' \
                   'esi-characters.read_chat_channels.v1 esi-characters.read_medals.v1 ' \
                   'esi-characters.read_standings.v1 esi-characters.read_agents_research.v1 ' \
                   'esi-industry.read_character_jobs.v1 esi-markets.read_character_orders.v1 ' \
                   'esi-characters.read_blueprints.v1 esi-characters.read_corporation_roles.v1'
    ret['state'] = base64.urlsafe_b64encode(str(time.time()).encode())
    sss = urllib.parse.urlencode(ret)
    return sss
