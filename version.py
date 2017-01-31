# -*- coding: utf-8 -*-


def get_pyevemon_version():
    rv = dict()
    #
    # change below with every version update
    rv['version'] = '0.1'
    rv['app_name'] = 'pyevemon'
    rv['app_displayname'] = 'PyEVEMon'
    rv['app_domain'] = 'pyevemon.minlexx.ru'
    rv['author_name'] = 'Lexx Min'
    rv['author_email'] = 'alexey.min@gmail.com'
    #
    # generated from above - do not edit
    rv['version_str'] = '{} version {}'.format(rv['app_name'], rv['version'])
    rv['website_url'] = 'https://{0}/'.format(rv['app_domain'])
    return rv
