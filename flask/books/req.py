# coding=utf-8

from flask import Flask
app = Flask(__name__)

import books

@app.route("/")
def do_home():
	h = books.home()
	return h

@app.route("/books")
def do_books():
	b = books.books()
	return b

@app.route("/book/<string:book_id>")
def do_book(book_id):
	b = books.book(book_id)
	return b

@app.route("/students")
def do_students():
	s = books.students()
	return s

@app.route("/student/<string:student_id>")
def do_student(student_id):
	return books.student(student_id)