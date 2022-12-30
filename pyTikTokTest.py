import requests

headers_by_me = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'referer': "https://www.google.com/"
    }
request = requests.get("https://www.tiktok.com/", headers= headers_by_me)

print(request)