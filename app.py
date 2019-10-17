from flask import Flask,render_template
from wt_forms import *
from models import *
from flask_sqlalchemy import SQLAlchemy

#app config
app=Flask(__name__)

app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)

class User(db.Model):
    '''user model'''
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40),unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.password}')"

@app.route('/',methods=['GET','POST'])
def index():
    form=RegistrationForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        user1=User(username=username,password=password)
        db.session.add(user1)
        db.session.commit()
        return "inserted successfully"
    return render_template('index.html',form=form)





if(__name__=='__main__'):
    app.run(debug=True,port=9000)
