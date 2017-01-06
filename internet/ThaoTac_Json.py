import requests, json

print(requests.__file__)
print(dir(requests))

print('Fetching url ...')
url = "https://api.github.com/users/voduytuan/repos"
#url = 'http://localhost:86/api'
response = requests.get(url, verify=False) #Verify is check SSL certificate

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
print(response.status_code)
print(response.headers)
print('COOKIES')
print(response.cookies)
print('TEXT')
print(response.text)

print('JSON')
data = response.json()
print(data)
print('*****^^^*****')
print(data[0]['url'])