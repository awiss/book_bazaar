def index(self,request):
	print request
	error = None
	return self.render_template('home.html', error=error)