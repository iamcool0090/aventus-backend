# ipfs/ipfs.py

import ipfsApi
import requests

download_file_url = 'http://127.0.0.1:5001/api/v0/cat'

class IPFS:
    def __init__(self):
        self.api_client = ipfsApi.Client('127.0.0.1', 5001)

    def upload_file(self, file_path):
        return self.api_client.add(file_path)

    def download_file(self, file_hash):
        params = {
        'stream-channels': 'true',
        'encoding': 'json',
        'arg': {file_hash}
        }

        response = requests.post(download_file_url, params=params)     
        if response.status_code == 200:
            return response.text
        else:
            response.raise_for_status()


