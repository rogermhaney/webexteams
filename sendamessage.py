import requests
import json

url = 'https://api.ciscospark.com/v1/messages'

headers = {
	"Authorization": "Bearer MGE1YWZlMTUtYzlhOC00ZWUzLTllYjQtYjBkMmUxNTVmMGNhNDc1ZjVmOTgtMTE0_PF84_e022b5d5-fdca-4b8a-9d1c-1f7f4d958cd7",
	"Content-Type": "application/json"
	}

payload = {
	"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vODAzZGRiYjAtYWZjMC0xMWU5LWFkOWEtMmI1ZDU5M2YyYjM5",
    "text" : "This is a test message!"
	}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.json())