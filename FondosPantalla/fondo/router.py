from fondo.models import Fondos

ROUTED_MODELS = [Fondos]

class Router(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'sampleSchema'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'sampleSchema'
        return None