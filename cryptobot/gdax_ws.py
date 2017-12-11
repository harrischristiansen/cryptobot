import gdax, time

class gdaxWS(object):
	def __init__(self):
		self._client = gdaxWSClient()
		self._client.start()

	@property
	def priceLTC(self):
		while self._client.price_ltc == 0:
			time.sleep(0.5)
		return self._client.price_ltc

	def close(self):
		self._client.close()

class gdaxWSClient(gdax.WebsocketClient):
	def on_open(self):
		self.url = "wss://ws-feed.gdax.com/"
		self.products = ["LTC-USD"]
		self.message_count = 0
		self.price_ltc = 0
	def on_message(self, msg): # https://docs.gdax.com/#overview
		if 'price' in msg and 'type' in msg:
			if msg["type"] == "match":
				self.price_ltc = float(msg["price"])

if __name__ == "__main__":
	wsClient = gdaxWS()
	while (True):
		print(wsClient.priceLTC)
		time.sleep(1)
	wsClient.close()
