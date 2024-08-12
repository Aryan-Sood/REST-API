import requests

#endpoint = "https://httpbin.org"   # this gives a html file as text
endpoint = "http://localhost:8000/api/"   # this gives a json response

get_response = requests.post(endpoint, json={"title":"HW"})
# print(get_response.json())