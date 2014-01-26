from flask import render_template, request, flash, redirect, Markup
from app import app
from models import db, User

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/impress')
def impress():
	return 'll'

@app.route('/privacy')
def about_us():
	return 'privacy'

@app.route('/contact')
def contac():
	return 'contac '

@app.route('/admin')
def admin():
	return 'Admin'

@app.route('/activate/<token>')
def activate(token):
	return 'Token is %s' %token

@app.route('/register', methods = ['POST'])
def register():
	new_user = User(** (request.form.to_dict(flat=True))) # converting to normal dict

	try:
		db.session.add(new_user)
		db.session.commit()
	except:
		message = Markup("Something went wrong. Please try again.")
		flash(message)
		return redirect('/')
	message = Markup("You successfully registerd!")
	flash(message)
	return redirect('/')

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'