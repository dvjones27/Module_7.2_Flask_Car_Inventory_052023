import requests

url = "https://car-api2.p.rapidapi.com/api/vin/KNDJ23AU4N7154467"

headers = {
	"X-RapidAPI-Key": "9ec14ba293msh7e92b9cfbc58a6ep158766jsn12343d4471e7",
	"X-RapidAPI-Host": "car-api2.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())