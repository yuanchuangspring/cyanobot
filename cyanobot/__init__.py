from .Adapter import *
from .Bot import *
from .Logger import *
from .Plugins import *
import pyfiglet

name='cyanobot'

__version__ = '0.0.1.2'
VERSION = __version__

__all__ = [
    'Adapter',
    'Bot',
    'Logger'
]

result = pyfiglet.figlet_format(text="CyanoBot", font='stop')
print(result)

