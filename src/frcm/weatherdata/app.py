from flask import Flask, render_template, request, session, redirect
from geopy.geocoders import Nominatim
import base64
import hashlib
import sqlite3


#TEEEST
import datetime
import threading
import time

from frcm.frcapi import FireRiskAPI
from frcm.weatherdata.client_met import METClient
from frcm.weatherdata.extractor_met import METExtractor
from frcm.datamodel.model import Location
#from frcm.weatherdata.app import app, location_data
#TEEET

app = Flask(__name__)
app.secret_key = 'your-secret-key'

geolocator = Nominatim(user_agent="geoapi")
location_data = {}

# TEEST
met_extractor = METExtractor()
#Start the web server in a separate thread
#threading.Thread(target=lambda: app.run(port=8000, debug=True, use_reloader=False)).start()
# TODO: maybe embed extractor into client
met_client = METClient(extractor=met_extractor)
#TEEEET

frc = FireRiskAPI(client=met_client)


@app.route('/')
def index():
    if 'username' in session:
        #avg_FR = session.get('avg_FR')
        return render_template('index.html')#, avg_FR=avg_FR)
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password match in the database
        conn = sqlite3.connect('FireGuard_DB.sql')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authenticator WHERE username=?', (username,))
        user = cursor.fetchone()
        conn.commit()
        conn.close()

        if user is not None and username == user[0] and password == user[1]:
            session['username'] = username
            return redirect('/')  # Redirect to the index page after successful login
        else:
            return render_template('login.html', error='Invalid username or password')
        
    return render_template('login.html')
      
@app.route('/logout')
def logout():
    session.pop('username', None)
    #session.pop('avg_FR', None)  # Clear avg_FR from the session
    return redirect('/login')

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    if 'username' not in session:
        return redirect('/login')
    
    address = request.args.get('address')
    location = geolocator.geocode(address)
    
    if location:
        location_data['latitude'] = location.latitude
        location_data['longitude'] = location.longitude
        
        # TEEEEST
        LocationGiven = Location(latitude=location_data['latitude'], longitude=location_data['longitude'])
        obs_delta = datetime.timedelta(days=2)
        predictions = frc.compute_now(LocationGiven, obs_delta)
        
        avg_FR = 0
        for fire_risk in predictions.firerisks:
            avg_FR += fire_risk.ttf
        avg_FR = avg_FR / len(predictions.firerisks)
        
        
        # Calculate avg_FR
        #avg_FR = calculate_avg_FR()

        #session['avg_FR'] = avg_FR  # Store avg_FR in the session

        return {
            'latitude': location.latitude,
            'longitude': location.longitude,
            'avg_FR': avg_FR  # Include avg_FR in the response
        }
    else:
        return {'error': 'Address not found'}, 404
    
# def calculate_avg_FR(predictions):
#     avg_FR = 0
#     for fire_risk in predictions.firerisks:
#         avg_FR += fire_risk.ttf
#     avg_FR = avg_FR / len(predictions.firerisks)
#     return avg_FR
        