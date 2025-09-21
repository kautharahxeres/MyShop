from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#creates the database in the instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///work.db'
app.config['SECRET_KEY'] = '@#$%^^'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creates the database table.
class employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))
    level = db.Column(db.String(200), default ='one')

class customer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))
    level = db.Column(db.String(200), default ='one')

#connects the table to the database
with app.app_context():
    db.create_all()

#ROUTING 
@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/register', methods=['POST', 'GET'])  
def register():
    return render_template('register.html')

@app.route('/edit', methods=['POST', 'GET'])  
def edit():
    return render_template('edit.html')

#runs the program and helps execute the end of the program
if (__name__) == "__main__":
    app.run(debug=True)