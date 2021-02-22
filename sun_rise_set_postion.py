### --- Using a Sunrise and Sunset Api to get the TIME for sunrise or sunset --- ###
### --- of a particular poition  given a lat and lng position. ----------------- ###

import requests
from datetime import datetime

MY_LAT = 6.52
MY_LONG = 3.38

#    Set parameter to parse into the API get function.
parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0  # from sunrise API docx formatted key is set to '0' to change the time returned to 24hrs format instead of a 12hrs format.
}
response = requests.get('http://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(':')[0])
sunset = int(data['results']['sunset'].split("T")[1].split(':')[0])

# use the split() method to get the HOURS of sunrise and sunset
# print(sunrise)
# print(sunset)
# print(datetime.now().hour)
