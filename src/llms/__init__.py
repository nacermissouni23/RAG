from importlib import import_module
try:
    conf = import_module("src.configs.real_config")
except ImportError:
    conf = import_module("src.configs.config")

if conf.GPT_api_key != '':
    from .api_model import GPT

from .local_model import Mock