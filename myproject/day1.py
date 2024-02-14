from flask import Flask

app=Flask(__name__)


@app.route('/aa')
def home():
    return "<h1>WELCOME TO FLASK</h1>"


@app.route('/hai/<myname>')
def details(myname):
    return 'Hai my name is '+myname

@app.route('/hai/<int:num>')
def mynum(num):
    return 'Hai my num is %d'%num

def myhome():
    return "my home page"

app.add_url_rule("/myhome","myhome",myhome)


if __name__=="__main__":
    app.run(debug=True)