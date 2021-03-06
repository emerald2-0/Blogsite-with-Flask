import datetime, re
#re module for string manipulation (Regex stuff:)
from app import db 

def slugify(s):
	return re.sub('[^\w] +', '-', s).lower()
	#The above line returns a human-readable string as a url format-like

#Entry model as a normal class; extending db model
class Entry(db.Model):
	"""docstring for Entry"""
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	slug = db.Column(db.String(100), unique=True)
	body = db.Column(db.Text)
	created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
	modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


	def __init__(self, *args, **kwargs):
		super(Entry, self).__init__(*args, **kwargs) #Trying to call a parent constructor
		self.generate_slug()

	def generate_slug(self):
		self.slug=''
		if self.title:
			self.slug = slugify(self.title)

	
	def __repr__(self):
		return '<Entry: %s' %self.title