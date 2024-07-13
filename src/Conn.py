import twsapi.source.pythonclient.ibapi as ibapi


def get_version():
    print("TWS API version:", ibapi.__version__)
