import json
class WeatherData:
    def __init__(self, hours, temperature, windspeed,):
        self.hours = hours
        self.temperature = temperature
        self.windspeed = windspeed
        
    def display(self, country):
        print(f"in {country} at {self.hours} hours ")
        print(f"\tThe temperature is {self.temperature}")
        print(f"\tThe windspeed is {self.windspeed}") 

def data_from_file(all_data):
    obj=[]
    for data in all_data["dataseries"]:
        temperature = data["temp2m"]
        windspeed = data["wind10m"]["speed"]
        hours = data["timepoint"]    
    
        weatherdata = WeatherData(hours=hours, temperature=temperature, windspeed=windspeed)
        obj.append(weatherdata)
    
    return obj  
     

def main():
    with open('classes-weather-data/beginning/api_output.json', 'r') as f:
        all_data = json.load(f)
    
    country = "Nairobi"
    full_data = data_from_file(all_data) 
    for weather_data in full_data:
        weather_data.display(country)  

    for data in all_data['dataseries']:
        print(data['temp2m'])

main()

