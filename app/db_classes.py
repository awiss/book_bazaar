from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class User(Base):
	__tablename__ = 'users'

	id 				= Column(Integer, primary_key=True)
	name 			= Column(String)
	fullname 	= Column(String)
	password 	= Column(String)

	def __repr__(self):
	  return "<User(name='%s', fullname='%s', password='%s')>" % (
	                       self.name, self.fullname, self.password)

class Book(Base):
	__tablename__ = 'books'
	
	id 					= Column(Integer, primary_key=True)
	contact 		= Column(String)
	price 			= Column(Integer)
	title 			= Column(String)
	author			= Column(String)
	isbn 				= Column(String)
	condition		=	Column(String)
	subject			= Column(String)
	course_num 	= Column(String)

	def __repr__(self):
	  return "<Book(title='%s', contact='%s', price='%s')>" % (
	                       self.title, self.contact, self.price)