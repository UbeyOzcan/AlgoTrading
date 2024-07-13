from src.Conn import TradingApp
import time

app = TradingApp()
app.connect("127.0.0.1", 7496, 0)

time.sleep(5)

app.disconnect()
