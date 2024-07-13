import twsapi.source.pythonclient.ibapi as ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class TradingApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, wrapper=self)



