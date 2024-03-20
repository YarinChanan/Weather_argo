from flask import Flask, render_template, request, redirect
import requests
import back

app = Flask(__name__)


@app.route('/home',methods = ['GET'])
def home():
    """Return home page"""
    return render_template('home.html')

@app.route('/error',methods = ['GET'])

def error():
    """Return error page"""
    return render_template('error.html')

@app.route('/result',methods = ['GET','POST'])
def result():
    """Return result page"""
    # Get city from home page form
    city = request.form.get("cname")
    try:
        # Backend function
        list_info_days = back.json_creation(city)
        return render_template('result.html',cname=city,list=list_info_days)
    except:
        return redirect('/error')

@app.route('/',methods = ['GET'])
def home_redirect():
    """From root to home."""
    return redirect('/home')
    

if __name__=="__main__":
    app.run(host='0.0.0.0')
