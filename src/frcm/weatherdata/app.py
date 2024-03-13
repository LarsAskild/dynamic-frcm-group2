from flask import Flask, render_template, request
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="geoapi")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    address = request.args.get('address')
    location = geolocator.geocode(address)
    if location:
        return {
            'latitude': location.latitude,
            'longitude': location.longitude
        }
    else:
        return {'error': 'Address not found'}, 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
