from flask import Flask,render_template,redirect,url_for,flash
from wt_forms import *
from models import *
from passlib.hash import pbkdf2_sha256
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
from flask_socketio import SocketIO,send

#app config
app=Flask(__name__)

app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://yeeuhnjesvgfbb:6e58599eb9da0288df9cbec9e29fdcb7b5373b55d712f892dd7298de389cdcc5@ec2-174-129-210-249.compute-1.amazonaws.com:5432/d9709ll1mlvkn7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
socketio = SocketIO(app)

db=SQLAlchemy(app)

#config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"
login_manager.login_message = u"Bonvolu ensaluti por uzi tiun paĝon."
login_manager.login_message_category = "info"

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return "please login to enter into chat room"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


"""registration route"""
@app.route('/',methods=['GET','POST'])
def index():
    form=RegistrationForm()
    #add username to the DB if validation succeed
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        hash = pbkdf2_sha256.hash(password)
        user1=User(username=username,password=hash)
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('index.html',form=form)

def login_fresh():
    '''
    This returns ``True`` if the current login is fresh.
    '''
    pass


"""login route"""
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        login_user(user)
        """fresh login"""
        if(login_fresh()):
            flash('hope you like this','success')
            return redirect(url_for('first_timer'))
        elif(current_user.is_authenticated):
            flash('you are now logged in successfully','success')
            print(user.username)
            return redirect(url_for('chatroom'))
    return render_template('login.html',form=form)

@app.route('/first_timer',methods=['GET'])
@login_required
def first_time():
    return "<h2>welcome first timer</h2>"


@app.route('/after_login',methods=['GET'])
@login_required
def after_login():
    """"""
    #if not current_user.is_authenticated:
        #return "please login to enter into chat room"
    return render_template('after_login.html')

@app.route('/chatroom',methods=['GET'])
@login_required
def chatroom():
    """"""
    #if not current_user.is_authenticated:
        #return "please login to enter into chat room"
    return render_template('chatroom.html',username=current_user.username)


@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('you are now logged out successfully','success')
    return redirect(url_for('login'))

if(__name__=='__main__'):
    socketio.run(app,debug=True)
    #app.run(debug=True,port=9000)
