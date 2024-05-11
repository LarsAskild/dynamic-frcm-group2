import datetime
import threading
import time
import sqlite3

from frcm.frcapi import FireRiskAPI
from frcm.weatherdata.client_met import METClient
from frcm.weatherdata.extractor_met import METExtractor
from frcm.datamodel.model import Location
from frcm.weatherdata.app import app, location_data

# sample code illustrating how to use the Fire Risk Computation API (FRCAPI)
if __name__ == "__main__":

    #met_extractor = METExtractor()
    #Start the web server in a separate thread
    threading.Thread(target=lambda: app.run(port=8000, debug=True, use_reloader=False)).start()
    # TODO: maybe embed extractor into client
    #met_client = METClient(extractor=met_extractor)
    
    
    #frc = FireRiskAPI(client=met_client)
    while(True):
        
        
        #if('latitude' in location_data and 'longitude' in location_data):
            '''LocationGiven = Location(latitude=location_data['latitude'], longitude=location_data['longitude'])
            obs_delta = datetime.timedelta(days=2)
            predictions = frc.compute_now(LocationGiven, obs_delta)
            location_data.clear()
            
            def calculate_avg_FR():
                avg_FR = 0
                for fire_risk in predictions.firerisks:
                    avg_FR += fire_risk.ttf
                avg_FR = avg_FR / len(predictions.firerisks)
                return avg_FR

            avg_FR = calculate_avg_FR()
            print("Average Fire Risk: ")
            print(avg_FR)'''
            
            
            # def calculate_avg_FR():
            #     avg_FR = 0
            #     for fire_risk in predictions.firerisks:
            #         avg_FR += fire_risk.ttf
            #     avg_FR = avg_FR / len(predictions.firerisks)
            #     return avg_FR

        
        #time.sleep(0.5)    

    print(location_data) # test purposes
    
    

    # location = Location(latitude=60.383, longitude=5.3327)  # Bergen
    # location = Location(latitude=59.4225, longitude=5.2480)  # Haugesund

    # Fails
    # location = Location(latitude=62.5780, longitude=11.3919)  # Røros
    # location = Location(latitude=69.6492, longitude=18.9553)  # Tromsø

    # how far into the past to fetch observations

    

    #predictions = frc.compute_now(LocationGiven, obs_delta)

    #print(predictions)
  