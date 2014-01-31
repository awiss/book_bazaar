def index(self,request):
	error = None
	return self.render_template('home.html', error=error)