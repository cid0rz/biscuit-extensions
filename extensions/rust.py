from __future__ import annotations

__version__ = '0.0.1'
__version_info__ = tuple([ int(num) for num in __version__.split('.')])


import subprocess as sp
import typing

if typing.TYPE_CHECKING:
    from biscuit import ExtensionsAPI

class Extension:
    """Rust extension for Biscuit (author: @billyeatcookies)
    
    Extension will automatically install rust-analyzer if not installed.
    
    Contributes:
    - language server configuration for Rust (rust-analyzer)
    """
    
    def __init__(self, api):
        self.api = api

    def run(self):
        try:
            sp.check_call(['rustup', 'component', 'add', 'rust-analyzer'])
        except sp.CalledProcessError:
            self.api.notifications.warning("Rust extension requires rust-analyzer to be installed & in your PATH.")
        self.api.register_langserver('Rust', 'rust-analyzer')
        
