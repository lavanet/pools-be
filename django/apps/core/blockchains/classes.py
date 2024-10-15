from libs.utils import logger
from .models import Denom


class DenomStore:
    _store = {}

    def __init__(self):
        self.fetch()

    def fetch(self):
        self._store = {denom.ibc_denom: denom for denom in Denom.objects.all()}

    def get(self, ibc_denom):
        denom = self._store.get(ibc_denom)
        if not denom:
            try:
                denom = Denom.create_from_ibc(ibc_denom=ibc_denom)
                self._store[ibc_denom] = denom
            except:
                logger.info('DenomStore.get(): failed to create denom: %s', ibc_denom, exc_info=True)
        return denom
