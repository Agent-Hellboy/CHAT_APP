from flask import Flask,render_template,redirect,url_for
from wt_forms import *
from models import *
from passlib.hash import pbkdf2_sha256


#app config
app=Flask(__name__)

app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)



"""registration route"""
@app.route('/',methods=['GET','POST'])
def index():
    form=RegistrationForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        hash = pbkdf2_sha256.hash(password)
        user1=User(username=username,password=hash)
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('index.html',form=form)


"""login route"""
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        return "you are now logged in"
    return render_template('login.html',form=form)



if(__name__=='__main__'):
    app.run(debug=True,port=9000)
