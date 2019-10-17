from flask import Flask,render_template
from wt_forms import *
from models import *


#app config
app=Flask(__name__)

app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)



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

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        user_d=User.query.filter_by(username=username).first()
        print(user_d.username)
        print(user_d.password)
        if(user_d.password==password):
            return "you are allowed to login"
    return render_template('login.html',form=form)



if(__name__=='__main__'):
    app.run(debug=True,port=9000)
