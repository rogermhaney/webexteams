
import requests
import json

url = 'https://api.ciscospark.com/v1/rooms'

headers = {
	"Authorization": "Bearer YmRkOTU0NzYtOWE0Ny00ZTAzLWFmZmQtYjAyNThjYmRkMWI4YTI5OWNkOWUtYjNk_PF84_e022b5d5-fdca-4b8a-9d1c-1f7f4d958cd7",
	"Content-Type": "application/json"
	}

queryParams = {
	"sortBy" : "lastactivity", 
    "max" : "5"
	}

response = requests.get(url, headers=headers, params=queryParams)


print(response.status_code)
print(response.text)