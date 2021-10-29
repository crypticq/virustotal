import requests
api_key = input(" virustotal key?: ")
url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': api_key}
files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}
response = requests.post(url, files=files, params=params)
print(response.json())
