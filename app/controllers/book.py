from db_classes import Book
from werkzeug.utils import redirect
def add(self,request):
	if(request.method == 'GET'):
		return self.render_template('add_book.html')
	else:
		print request.form
		# price is stored in integer cents
		price = int(request.form['price'].replace('.',''))

		book = Book(
			contact=request.form['contact'],
			price=price,
			title=request.form['title'],
			author=request.form['author'],
			isbn=request.form['isbn'],
			condition=request.form['condition'],
			subject=request.form['subject'],
			course_num=request.form['course_num']
		)
		self.mysql_session.add(book)
		self.mysql_session.commit()
		return redirect('/')

def view_book(self,request,book_id):
	#Todo
	return redirect('/')
