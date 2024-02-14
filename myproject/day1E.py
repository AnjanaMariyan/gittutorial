from flask import *

app=Flask(__name__)




# @app.route('/login',methods=['GET'])  
# def reg():
#     uname=request.args.get('fname')
#     place=request.args.get('place')
#     return 'success'+uname



@app.route('/login',methods=['POST'])  
def reg():
    uname=request.form['fname']
    place=request.form['place']
    return 'success'+uname



if __name__=="__main__":
    app.run(debug=True)