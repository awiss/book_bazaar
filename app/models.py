from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()
users = Table('users', metadata,
	Column('id', Integer, primary_key=True),
	Column('name', String(50)),
	Column('password_hash',String(256)),
	Column('fullname', String(50)),
)
books = Table('books',metadata,
	Column('id', Integer, primary_key=True),
	Column('contact',String(50)),
	Column('price',Integer),
	Column('title',String(100)),
	Column('author',String(100)),
	Column('isbn',String(50)),
	Column('condition',String(100)),
	Column('subject',String(10)),
	Column('course_num', String(10)),
)