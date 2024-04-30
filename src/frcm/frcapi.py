import datetime
import json
from frcm.datamodel.model import FireRiskPrediction, Location, WeatherData, Observations, Forecast
from frcm.weatherdata.client import WeatherDataClient
import frcm.fireriskmodel.compute
import sqlite3

class FireRiskAPI:

    def __init__(self, client: WeatherDataClient):
        self.client = client
        self.timedelta_ok = datetime.timedelta(days=1) # TODO: when during a day is observations updated? (12:00 and 06:00)
        # TODO (NOTE): Short term forecast updates every 3rd hour with long term forecast every 12th hour at 12:00 and 06:00
        self.interpolate_distance = 720

    def compute(self, wd: WeatherData) -> FireRiskPrediction:

        return frcm.fireriskmodel.compute.compute(wd)

    def compute_now(self, location: Location, obs_delta: datetime.timedelta) -> FireRiskPrediction:
    
        # Connect to the database
        conn = sqlite3.connect('FireGuard_DB.sql')
        cursor = conn.cursor()    

        time_now = datetime.datetime.now()
        start_time = time_now - obs_delta
        latitude = location.latitude
        longitude = location.longitude

        
        observations = self.client.fetch_observations(location, start=start_time, end=time_now)
        print(observations)
        forecast = self.client.fetch_forecast(location)

        wd = WeatherData(created=time_now, observations=observations, forecast=forecast)
        prediction = self.compute(wd)

        # Extract firerisks from prediction
        risk_list = [firerisk.ttf for firerisk in prediction.firerisks]

        # Prepare data for insertion into database
        data = json.loads(wd.to_json())
        data_to_insert = [(entry["temperature"], entry["humidity"], entry["wind_speed"], entry["timestamp"]) for entry in data["observations"]["data"]]

        # Check if records already exist with the same primary key
        for entry, firerisk in zip(data_to_insert, risk_list):
            lat, lon, temp, humidity, wind_speed, timestamp = (latitude, longitude,) + entry
            cursor.execute(
            'SELECT EXISTS(SELECT 1 FROM weatherdata WHERE latitude=? AND longitude=? AND timestamp=?)',
            (lat, lon, timestamp)
        )
        exists = cursor.fetchone()[0]

        if not exists:
            # Insert data into database  
            cursor.execute(
                'INSERT INTO weatherdata (latitude, longitude, temperature, humidity, wind_speed, timestamp, firerisk) '
                'VALUES (?, ?, ?, ?, ?, ?, ?)',
                (lat, lon, temp, humidity, wind_speed, timestamp, firerisk)
            )
            print("Entries have been added to database")
        else:
            print("Entries already exist in database")
       
        conn.commit()
        conn.close()
        
        return prediction

    def compute_now_period(self, location: Location, obs_delta: datetime.timedelta, fct_delta: datetime.timedelta):
        pass

    def compute_period(self, location: Location, start: datetime, end: datetime) -> FireRiskPrediction:
        pass

    def compute_period_delta(self, location: Location, start: datetime, delta: datetime.timedelta) -> FireRiskPrediction:
        pass

 
