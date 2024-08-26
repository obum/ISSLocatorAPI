import requests  # Use requests library to make requests to API ENDPOINTS
from sun_rise_set_postion import sunset, sunrise, MY_LAT, MY_LONG
from datetime import datetime
import smtplib
import time

my_email = "obumanichebe@gmail.com"
my_password = "stevengerad"

# GET ISS POSITION
response = requests.get(url='http://api.open-notify.org/iss-now.json')  # make sure internet connection is activated.
# print(response.status_code)
response.raise_for_status()

data = response.json()
longitude = round(float(data['iss_position']['longitude']), 2)
latitude = round(float(data['iss_position']['latitude']), 2)
iss_position = longitude, latitude


def is_iss_possition_overhead():
    # GET ISS POSITION
    response = requests.get(
        url='http://api.open-notify.org/iss-now.json')  # make sure internet connection is activated.
    # print(response.status_code)
    response.raise_for_status()

    data = response.json()
    longitude = round(float(data['iss_position']['longitude']), 2)
    latitude = round(float(data['iss_position']['latitude']), 2)

    if (MY_LAT - 5 <= latitude <= MY_LAT + 5) and (MY_LONG - 5 <= longitude <= MY_LONG + 5):
        return True
    else:
        print(f'iss longitude:{longitude}, iss latitude: {latitude}')
        print(f'my longitude:{MY_LONG}, my latitude: {MY_LAT}')
        print(f'longitude diff:{MY_LONG - longitude}, latitude diff: {MY_LAT - latitude}')
        return False


print(is_iss_possition_overhead())


# GET MY POSITION SUNRISE AND SUNSET TIME

# print(iss_position)
# print(sunset)
# print(sunrise)

# CHECK for Darkness

# current_hour = datetime.now().hour
# if (current_hour <= sunrise) or (current_hour > sunset):
#     print(True)
# else:
#     print(False)
#
# # CHECK for if ISS position is Over head
# my_position = (MY_LONG, MY_LAT)
#
# print(iss_position, my_position)
#
# if (abs(iss_position[0] - my_position[0]) <= 5) and (abs(iss_position[1] - my_position[1]) <= 5):
#     print(True)
# else:
#     print(False)


def is_in_dark():
    current_hour = datetime.now().hour
    my_position = (MY_LONG, MY_LAT)
    if (current_hour <= sunrise) or (current_hour > sunset):
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_possition_overhead() and is_in_dark():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="bumski10.0a@gmail.com",
                                msg="Subject: Iss Tracker\n\nLook up into the sky the ISS is over head")
