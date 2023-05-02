import requests
import time

collection = "0x441121df09c8c7f545a9444ab554ce640b566c4d"
start_id = 1
end_id = 3
wait_time = 0.1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}


for i in range(start_id, end_id + 1):
    print(i)
    url = "https://api.opensea.io/api/v1/asset/" + collection + "/" + str(i) + "?force_update=true"
    print(url)
    response = requests.get(url, headers=headers)
    print(response)
    time.sleep(wait_time)