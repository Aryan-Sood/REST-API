import requests

#endpoint = "https://httpbin.org"   # this gives a html file as text
endpoint = "http://localhost:8000/api/"   # this gives a json response

get_response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello world"})
print(get_response)