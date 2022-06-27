import requests
url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'

if __name__ == "__main__":
    response  = requests.get(url)
    if response.status_code == 200:
        print("下載成功")
        print(response.text)
    else:
        print("下載失敗")