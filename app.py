from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key = "No_Secret"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Business.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


db=SQLAlchemy(app)


class Business(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60))
    email=db.Column(db.String(60))
    phone=db.Column(db.String(60))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
@app.route('/')
def index():
    all_data=Business.query.all()
    return render_template('index.html',Business=all_data)
@app.route('/success')
def success():
    return render_template('success.html')
@app.route('/insert',methods=['GET','POST'])
def insert():
    if request.method =="GET":
        return render_template('insert.html')
    else:
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        my_data= Business(name,email,phone)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('success'))


@app.route('/update/<int:id>/',methods=['GET','POST'])
def update(id):
    if request.method == "POST":
        my_data = Business.query.get(id)
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('success',id=id))
    else:
        return render_template('update.html')


@app.route('/delete/<id>/',methods = ["GET","POST"])
def delete(id):
    my_data = Business.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)
# Part of the strucure were from https://www.youtube.com/watch?v=XTpLbBJTOM4
# But I have modified it based on the requirement and the function I want. Thank you for the comment
