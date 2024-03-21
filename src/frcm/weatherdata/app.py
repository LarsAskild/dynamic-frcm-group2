from flask import Flask, render_template, request, session, redirect
from geopy.geocoders import Nominatim
import base64
import hashlib
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'

geolocator = Nominatim(user_agent="geoapi")
location_data = {}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
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
        return {
            'latitude': location.latitude,
            'longitude': location.longitude
        }
    else:
        return {'error': 'Address not found'}, 404