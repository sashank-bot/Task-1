import requests

API_key = "fcec2dbc68a628cab0ba5f1e05d98b5c"

City = "London"

URL_base  = f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_key}"

response = requests.get(URL_base)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error",response.status_code)
    print(response.text)


print(URL_base)

