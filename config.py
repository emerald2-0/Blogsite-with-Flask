#Configurations to use
import os
class Configuration(object):
	"""docstring for Configuration"""
	APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
	"""
	def __init__(self, arg):
		super(Configuration, self).__init__()
		self.arg = arg
	"""