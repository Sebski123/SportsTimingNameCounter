# 
import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'
}
result = ""
baseurl = "https://www.sportstiming.dk/event/16156/participants?page="
for i in range(204,205):
    url = baseurl + str(i)
    print(f"Getting page {i}")
    response = requests.get(url, headers=headers)
    result = response.text


    with open(f"pages/result_{i}.html", "w", encoding="utf-8") as f:
        f.write(result)
    
    

# url = "https://www.sportstiming.dk/event/16156/participants?page=1"

# payload = {}
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'
# }

# response = requests.get(url, headers=headers, data=payload)

# print(response.text)
