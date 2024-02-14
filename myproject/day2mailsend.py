from flask import *
from flask_mail import *  #pip install flask-mail
app=Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="suzume9847@gmail.com"
app.config['MAIL_PASSWORD']='xnwi jtdw gevv oaop'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)


@app.route('/')
def send_myemail():
    msg=Message('subject',sender="suzume9847@gmail.com",recipients=['anjanamariyan@gmail.com'])
    msg.body="my flask  msg"
    mail.send(msg)
    return 'success'


if __name__=='__main__':
    app.run(debug=True)