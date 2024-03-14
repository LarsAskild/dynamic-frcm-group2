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

        time_now = datetime.datetime.now()
        start_time = time_now - obs_delta

        observations = self.client.fetch_observations(location, start=start_time, end=time_now)

        #print(observations)

        forecast = self.client.fetch_forecast(location)

        #print(forecast)

        wd = WeatherData(created=time_now, observations=observations, forecast=forecast)

        #print(wd.to_json())

        prediction = self.compute(wd)

        print("DATATATATA")
        # data blir gjort om til dictionary
        data = json.loads(wd.to_json())
        
        #Dette er måten å bla gjennom JSON
        for entry in data["observations"]["data"]:
            print(f"Temperature: {entry['temperature']}")
            
        #TODO: Implementere korrekt loop ovenfor
        #print(data)
        conn = sqlite3.connect('../FireGuard_DB.sql')
        cursor = conn.cursor()

        #TODO Send til database. sqlite-> cursor -> insert
        data_to_insert = [( entry["temperature"], entry["humidity"], entry["wind_speed"], entry["timestamp"]) for entry in data["observations"]["data"]]
        
        cursor.executemany('''
        INSERT INTO weatherdata (location, temperature, humidity, wind_speed, timestamp) VALUES (?, ?, ?, ?, ?)''',location, data_to_insert)
        
        conn.commit()
        conn.close()
        return 

    def compute_now_period(self, location: Location, obs_delta: datetime.timedelta, fct_delta: datetime.timedelta):
        pass

    def compute_period(self, location: Location, start: datetime, end: datetime) -> FireRiskPrediction:
        pass

    def compute_period_delta(self, location: Location, start: datetime, delta: datetime.timedelta) -> FireRiskPrediction:
        pass


