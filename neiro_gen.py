import requests
import base64
import time
from random import randint

message = input('Введите ваш запрос')

prompt = {
          "modelUri": "art://b1g3f13cj7d6d3ss2md9/yandex-art/latest",
          "generationOptions": {
            "seed": randint(10000, 20000000),
          },
          "messages": [
            {
              "weight": 1,
              "text": message
            }
          ]
      }

url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"

headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNy07LcVvM2d6W_-sH-4jfymTfPqrkNUfEEw1R"
    }

response = requests.post(url= url, headers=headers, json=prompt)
result = response.json()
print(result)

operation_id = result['id']

operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"

while True:
    operation_response = requests. get(operation_url, headers=headers)
    operation_result = operation_response.json()
    if 'response' in operation_result:
        image_base64 = operation_result['response']['image']
        break
    else:
        print('Ожидайте, изображение не готово')
        time.sleep(5)

image_data = base64.b64decode(image_base64)
with open('image.jpg', 'wb') as image_file:
    image_file.write(image_data)

print('Изображение готово, иди посмотри')