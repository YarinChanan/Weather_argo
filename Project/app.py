from flask import Flask, render_template, request, redirect
import requests
import back
import os, json
from datetime import datetime

app = Flask(__name__)

def save_search_query(location):
    """
    Append search query data to a single JSON file.

    Args:
    data (dict): Weather data from the API.
    location (str): User provided location.
    """
    file_path = 'search_history.json'  # Name of the file where data will be saved
    entry = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Include time for each entry
        'location': location
    }

    # Check if the file exists and has content
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r+') as file:
            # Load existing data
            file_data = json.load(file)
            # Append new data
            file_data.append(entry)
            # Set file's current position at the beginning
            file.seek(0)
            # Convert back to JSON and save
            json.dump(file_data, file, indent=4)
    else:
        # Create a new file or overwrite an empty one
        with open(file_path, 'w') as file:
            # Save the new data as a list
            json.dump([entry], file, indent=4)

@app.route('/home',methods = ['GET'])
def home():
    """Return home page"""
    bg_color = os.environ.get('BG_COLOR', '#eee')  # Default to eee if the environment variable is not set
    return render_template('home.html',bg_color=bg_color)

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
        save_search_query(city)
        return render_template('result.html',cname=city,list=list_info_days)
    except:
        return redirect('/error')
    

@app.route('/',methods = ['GET'])
def home_redirect():
    """From root to home."""
    return redirect('/home')
    

if __name__=="__main__":
    app.run(host='0.0.0.0')