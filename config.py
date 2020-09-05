import os

class Config(object):
	# For security, I guess?
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	# For the google maps API
	GOOGLEMAPS_KEY = os.environ.get('GOOGLEMAPS_KEY') or 'AIzaSyDENIJmzfu_BrlZHZrCr-khc0y2U_RH3Pk'

