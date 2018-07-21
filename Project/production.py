from .common import *

with open('/etc/secret.txt') as f:
	SECRET_KEY = f.read().strip()

DEBUG = False
