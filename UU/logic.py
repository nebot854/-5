import json
import time
import requests
import base64
from PIL import Image
from io import BytesIO
#from config import API_KEY, SECRET_KEY

class FusionBrainAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_pipeline(self):
        response = requests.get(self.URL + 'key/api/v1/pipelines', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, pipeline, images=1, width=200, height=200):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'pipeline_id': (None, pipeline),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/pipeline/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/pipeline/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['result']['files']

            attempts -= 1
            time.sleep(delay)
    
    def save_image(self, base64_string, file_path):
        # Загружаем изображение с URL
        decoded_data = base64.b64decode(base64_string)
        image = Image.open(BytesIO(decoded_data))

        # Сохраняем изображение на диск
        image.save(file_path)
        print(f"Image saved to {file_path}")


if __name__ == '__main__':
    api = FusionBrainAPI('https://api-key.fusionbrain.ai/', '001988684F3789181C1564F4F32A5805', 'FA6858C8C9C94D327F72BD7BA504F04F')
    pipeline_id = api.get_pipeline()
    uuid = api.generate("Пушистый кот в очках", pipeline_id)
    files = api.check_generation(uuid)
    
    # Сохраняем первое изображение на диск
    api.save_image(files[0], "generated_image.png")





