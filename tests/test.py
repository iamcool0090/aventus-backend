from ipfs.ipfs import IPFS

ipfs = IPFS()

def test_upload_file():
    try:
        file_hash = ipfs.upload_file('tests/sample.txt')[0]["Hash"]
        assert file_hash == 'QmUjE3kn917vN12GJgG4FhMfuvWXhfJvynq8nGBcFs8bmH'
    except Exception as e:
        print(f"File upload test failed: {e}")

def test_download_file():
    file_data = ipfs.download_file('QmUjE3kn917vN12GJgG4FhMfuvWXhfJvynq8nGBcFs8bmH')
    # Replace with meaningful assertion based on expected content
    assert file_data == 'Is IPFS Working ??'


test_upload_file()
test_download_file()