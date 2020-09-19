from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)  #creating instance of FLASK class and store it in app variable

# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:root@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://tmmflljddlgbxh:508185e68131ac6a46f82cdb36efc67ee4eb6f31c8096764939d369ba7d49b4e@ec2-52-207-124-89.compute-1.amazonaws.com:5432/dcjg2fec3dpuq3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)
class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))

@app.route('/')
def index():
	result = Favquotes.query.all()             #fetch all data from table and store in the result variable
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	return render_template('quotes.html')


@app.route('/process', methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =Favquotes(author=author,quote=quote)       #both inputs store in variable called quotedata
	db.session.add(quotedata)
	db.session.commit()


	return redirect(url_for('index')) #here is index because we are returning to index function



