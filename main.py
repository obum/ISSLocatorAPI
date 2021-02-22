import requests  # Use requests library to make requests to API ENDPOINTS

response = requests.get(url='http://api.open-notify.org/iss-now.json')  # make sure internet connection is activated.
# print(response.status_code)
response.raise_for_status()

data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = longitude, latitude
print(iss_position  )

