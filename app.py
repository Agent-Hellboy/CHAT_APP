from flask import Flask,render_template
from wt_forms import *
from flask_bootstrap import Bootstrap
#app config
app=Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='secret'

@app.route('/',methods=['GET','POST'])
def index():
    form=RegistrationForm()
    if form.validate_on_submit():
        return "Great Success"
    return render_template('index.html',form=form)





if(__name__=='__main__'):
    app.run(debug=True,port=9000)
