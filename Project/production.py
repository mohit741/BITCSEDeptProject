from .common import *

#SECRET_KEY = 'ehggheght3672w7ttsy74874hdu88&*eh'
with open('/etc/secret.txt') as f:
	SECRET_KEY = f.read().strip()

DEBUG = False
