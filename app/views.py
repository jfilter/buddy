from flask import render_template, request, flash, redirect, Markup, session

from users.lang import lang_array
from app import app


@app.route('/')
@app.route('/index')
def index():
	if 'uid' not in session:
		return render_template('index_reg.html', lang=lang_array)

	uid = session['uid']
	user = User.query.get(uid)
	return render_template('index_intern.html', user=user)

@app.route('/impress')
def impress():
	return render_template('impress.html')

@app.route('/privacy')
def about_us():
	return render_template('privacy.html')

@app.route('/contact')
def contac():
	return render_template('contact.html')

@app.route('/admin')
def admin():
	return 'Admin'

