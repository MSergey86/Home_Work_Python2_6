import requests

class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, path):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        res = requests.put(f'{url}?path={path}', headers=headers)
        print(f"Папка \"{path}\" на яндекс диске создана")
        return res