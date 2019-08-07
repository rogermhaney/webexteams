
import requests
import json

url = 'https://api.ciscospark.com/v1/rooms'

headers = {
	"Authorization": "Bearer MGE1YWZlMTUtYzlhOC00ZWUzLTllYjQtYjBkMmUxNTVmMGNhNDc1ZjVmOTgtMTE0_PF84_e022b5d5-fdca-4b8a-9d1c-1f7f4d958cd7",
	"Content-Type": "application/json"
	}

payload = {
	"title": "API Test x67"
	}

response = requests.post(url, data=json.dumps(payload), headers=headers)

newRoomId = response.json()['id']

print(response.json())
print(newRoomId)