from flask import *

app=Flask(__name__)

@app.route('/a')
def admin():
    return 'ADMIN'

@app.route('/t')
def teacher():
    return 'TEACHER'

@app.route('/')
def student():
    return 'STUDENT'

@app.route('/user/<name>')
def user(name):
    if name=="adm":
        return redirect(url_for('admin'))
    if name=="tea":
        return redirect(url_for('teacher'))
    if name=="stu":
        return redirect(url_for('student'))
    



@app.route('/page/<uname>')  
def mypage(uname):
    return render_template('day1.html',name=uname)

@app.route('/tb/<int:num>')  
def mytable(num):
    return render_template('day1.html',n=num,name='mul table of')



if __name__=="__main__":
    app.run(debug=True)