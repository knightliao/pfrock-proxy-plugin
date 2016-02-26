from pfrock.core.register import PfrockPluginRegister
from pfrock_proxy_plugin.index import PfrockProxyPlugin

__version__ = '0.2.1.dev6'

PfrockPluginRegister.register(PfrockProxyPlugin)
