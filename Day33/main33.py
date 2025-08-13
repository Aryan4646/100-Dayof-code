import requests
MY_LAT = 12.971599
MY_LNG = 77.594566

# response= requests.get(url= "http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()     # Raise exception if status code not equal to 200
# print(response.status_code)
# data = response.json()          # Will give the data that is received
# print(data)

parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG
}

response = requests.get(url= "https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(data)
print(sunrise)
