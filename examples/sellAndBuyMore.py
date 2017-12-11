'''
	@Harris Christiansen (code@harrischristiansen.com)
	Cryptobot - https://github.com/harrischristiansen/cryptobot
	sellAndBuyMore.py: Sell some currency on the next price rise, and buy more when the price dips
'''

import logging
logging.basicConfig(level=logging.DEBUG)

from cryptobot import Cryptobot
from getarguments import getarguments

cmd_args = getarguments() # Get Command Line Arguments

bot = Cryptobot(cmd_args['gdax_key'], cmd_args['gdax_secret'], cmd_args['gdax_pass']) # Create Instance of Cryptobot

while True: # Run Bot Forever
	bot.sellAfterRise(0.001)
	bot.buyAfterDrop(0.001)
