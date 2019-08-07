import requests
import json

url = 'https://api.ciscospark.com/v1/memberships'

headers = {
	"Authorization": "Bearer YmRkOTU0NzYtOWE0Ny00ZTAzLWFmZmQtYjAyNThjYmRkMWI4YTI5OWNkOWUtYjNk_PF84_e022b5d5-fdca-4b8a-9d1c-1f7f4d958cd7",
	"Content-Type": "application/json"
	}

queryParams = {
	"sortBy" : "lastactivity", 
    "max" : "5",
	"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vZGQ5YTI4OTMtMWE2ZC0zNTIzLWFjYzktYjJlNDZjNWIzMTc2"
	}

response = requests.get(url, headers=headers, params=queryParams)

print(response.json())