import requests
url="http://google.com"

response = requests.get(url)
print(response)

if response.status_code == 200:
    # print(response.text)
    print(response.text[:200])
