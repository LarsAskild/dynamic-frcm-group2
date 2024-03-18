from flask import Flask, render_template, request, session, redirect
from geopy.geocoders import Nominatim
import base64

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

        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect('/')
        else:
            return render_template('login.html')  # Add appropriate error message
        
    return render_template('login.html')  # Display login page

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

"""
from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import base64

app = Flask(__name__)
geolocator = Nominatim(user_agent="geoapi")
location_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
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

#if __name__ == '__main__':
#   app.run(debug=True, port=8000)
"""