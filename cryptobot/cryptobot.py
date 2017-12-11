'''
	@Harris Christiansen (code@harrischristiansen.com)
	Cryptobot - https://github.com/harrischristiansen/cryptobot
	Cryptobot: Automated cryptocurrency trading bot
'''

import gdax
import logging
import time

from . import gdax_ws

class Cryptobot(object):

	def __init__(self, gdax_key, gdax_b64secret, gdax_pass):
		if len(gdax_key) < 30 or len(gdax_b64secret) < 60 or len(gdax_pass) < 5:
			raise ValueError('Error: Currently only the GDAX API is supported, please provide GDAX credentials')

		self.gdax_ws = gdax_ws.gdaxWS()
		self.gdax_pub = gdax.PublicClient()
		self.gdax_auth = gdax.AuthenticatedClient(gdax_key, gdax_b64secret, gdax_pass)
		logging.debug("Connected to GDAX!")

	def waitForDrop(self, dropPercent): # decimal value of % price drop to wait for
		maxPrice = self.gdax_ws.priceLTC
		while maxPrice*(1-dropPercent) < self.gdax_ws.priceLTC:
			logging.debug("Waiting for Drop - Max: %f, Target: %f, Current: %f" % (maxPrice, maxPrice*(1-dropPercent), self.gdax_ws.priceLTC))
			time.sleep(1)
			if self.gdax_ws.priceLTC > maxPrice:
				maxPrice = self.gdax_ws.priceLTC

		return maxPrice*(1-dropPercent)

	def waitForRise(self, risePercent): # decimal value of % price rise to wait for
		minPrice = self.gdax_ws.priceLTC
		while minPrice*(1+risePercent) > self.gdax_ws.priceLTC:
			logging.debug("Waiting for Rise - Min: %f, Target: %f, Current: %f" % (minPrice, minPrice*(1+risePercent), self.gdax_ws.priceLTC))
			time.sleep(1)
			if self.gdax_ws.priceLTC < minPrice:
				minPrice = self.gdax_ws.priceLTC

		return minPrice*(1+risePercent)

	def buyAfterDrop(self, dropPercent):
		buyPrice = self.waitForDrop(dropPercent)
		print("Received signal to BUY: %f" % buyPrice)
		print(self.gdax_auth.buy(price=("%.2f" % buyPrice), size='0.01', product_id='LTC-USD'))
		return True

	def sellAfterRise(self, risePercent):
		sellPrice = self.waitForRise(risePercent)
		print("Received signal to SELL: %f" % sellPrice)
		print(self.gdax_auth.sell(price=("%.2f" % sellPrice), size='0.01', product_id='LTC-USD'))
		return True
