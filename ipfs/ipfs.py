# ipfs/ipfs.py

import ipfsApi

class IPFS:
    def __init__(self):
        self.api_client = ipfsApi.Client('127.0.0.1', 5001)

    def upload_file(self, file_path):
        return self.api_client.add(file_path)

    def download_file(self, file_hash):
        return self.api_client.cat('QmWvgsuZkaWxN1iC7GDciEGsAqphmDyCsk3CVHh7XVUUHq')
