import os
import sys
import requests
import json
client_id = "TikMmw1Tk3I8YAmbAXIb"
client_secret = "79SyD7Wwo0"

url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
files = {'image': open('lee.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if rescode == 200:
    
    data = json.loads(response.text)
    faces = data["faces"][0]["celebrity"]["value"]
    print(faces)

else:
    print("Error Code:" + rescode)