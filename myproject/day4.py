from flask import *
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///emp.sqlite3'
app.config['SECRET_KEY']='abc'
db =SQLAlchemy(app)


class Employees(db.Model):
    id =db.Column('employee_id',db.Integer,primary_key =True)
    name =db.Column(db.String(20))
    address =db.Column(db.String(20))

    def __init__(self,name,address):
        self.name=name
        self.address=address


@app.route('/add',methods=['GET','POST'])
def add_emp():
    if request.method =='POST':
        em =Employees(request.form['name'],request.form['address'])
        db.session.add(em)
        db.session.commit()
        return redirect(url_for('display'))
    else:

        return render_template('add.html')

@app.route('/')
def display():
    return render_template('listemp.html',emp=Employees.query.all())

@app.route('/ee/<int:id>')
def em_edt(id):
    s=Employees.query.get(id)
    db.session.commit()
    return render_template('update.html',se=s)

@app.route('/eu/<int:id>',methods=['POST'])
def s_update(id):
    if request.method=='POST':
        ser=Employees.query.get(id)
        
        # db.session.update(ser)
      
        db.session.commit()

        return redirect(url_for('display'))
    
@app.route('/ed/<int:id>')
def l_de(id):
     emp=Employees.query.get(id)
     
     db.session.delete(emp)
     db.session.commit()

     return redirect(url_for('display'))

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)



