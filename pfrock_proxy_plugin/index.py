#!/usr/bin/env python
# coding=utf8
from pfrock.core.constants import ROUTER_PATH
from pfrock.core.plugin import PfrockPlugin
from pfrock_proxy_plugin.proxy import get_proxy_handler

KEY_URL = 'url'
KEY_HOST = 'host'


class PfrockProxyPlugin(PfrockPlugin):
    def get_handler(self, options, **kwargs):
        # url path
        url_path = kwargs.get(ROUTER_PATH)

        url = options[KEY_URL] if KEY_URL in options else ""
        host = options[KEY_HOST] if KEY_HOST in options else ""
        if url and url_path:
            return get_proxy_handler(url_path, url, host)
        return None
