#Single view mapped to root
from app import app

@app.route('/')
def homepage():
	return 'Home Page by emerald'