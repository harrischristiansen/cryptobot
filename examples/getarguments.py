'''
	@Harris Christiansen (code@harrischristiansen.com)
	Cryptobot - https://github.com/harrischristiansen/cryptobot
	getarguments.py: Parse and return command line arguments
'''
import os
import argparse

def getarguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-k', '--gdax-key', metavar='str', type=str, default=os.environ.get('GDAX_KEY', ''), help='GDAX API Key')
	parser.add_argument('-s', '--gdax-secret', metavar='str', type=str, default=os.environ.get('GDAX_SECRET', ''), help='GDAX b64secret')
	parser.add_argument('-p', '--gdax-pass', metavar='str', type=str, default=os.environ.get("GDAX_PASS", ''), help='GDAX Passphrase')
	args = vars(parser.parse_args())

	return args