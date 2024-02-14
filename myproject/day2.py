from flask import *
app=app=Flask(__name__)


app.secret_key="aaaaaaaa"


@app.route('/')
def emp_reg():
    return render_template('day2reg.html')

@app.route('/su',methods=['GET','POST'])

def emp_details():
    if request.method=='POST':
        res=request.form
        return render_template('my_details.html',data=res)
    # return "success"

@app.route('/cs')
def cook_set():
    res=make_response("<h1>cookies set</h1>")
    res.set_cookie('place','elk')
    return res


@app.route('/cg')
def cook_get():
    res=request.cookies.get('place')
    return res

@app.route('/ss')    
def sess_set():
    res=make_response("<h1>session set <a href='/sg'> view details </a></h1>")
    session['phone']=7654356
    return res 


@app.route('/sg')  
def sess_get():
    if 'phone' in session:
        c=session['phone']
        return "my session value is %d <a href='/sd'> LOGOUT </a>" %c 
    else:
        return 'no session value is found'
 

@app.route('/sd')  
def session_del():
    if 'phone' in session:   
        session.pop('phone',None)
        return 'logout'      
    else:
        return 'no session value is found'
    
@app.route('/up')
def emp_upload():
    return render_template('myfile.html')
  
@app.route('/upsave',methods=['POST'])
def emp_upload_save():
    if request.method=='POST':
        f=request.files['img']
        f.save(f.filename)
        return 'success'

    
if __name__=="__main__":
    app.run(debug=True)